from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services import qdrant_client, OPENAI_API_KEY
from services.qdrant_client import similarity_search
from openai import OpenAI
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Initialize Jinja2Templates to load templates from a "templates" directory
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "..", "templates"))

# Initialize OpenAI client for chat completions
try:
    openai_chat_client = OpenAI(api_key=OPENAI_API_KEY)
except Exception as e:
    logging.error(f"Failed to initialize OpenAI chat client: {e}")
    openai_chat_client = None

@app.get("/")
async def root():
    return {"message": "FastAPI service layer placeholder"}

@app.get("/health")
async def health_check():
    try:
        # Attempt to get collections to verify Qdrant connection
        await qdrant_client.get_collections()
        return {"status": "ok", "qdrant_connection": "successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Qdrant connection failed: {e}")

@app.get("/chatbot", response_class=HTMLResponse)
async def get_chatbot(request: Request):
    """Serves the chatbot UI."""
    return templates.TemplateResponse("chatbot.html", {"request": request})

@app.post("/chat")
async def chat_with_bot(message: dict):
    """
    Receives user messages, performs similarity search, and generates responses.
    """
    user_message = message.get("message")
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    logging.info(f"Received message: {user_message}")

    # 1. Perform similarity search to get context
    try:
        # Assuming a default collection name 'my_collection' for now
        # This should be configurable or passed in the request
        context_results = await similarity_search(collection_name="my_collection", query_text=user_message, limit=3)
        context = " ".join([hit["payload"]["content"] for hit in context_results])
        logging.info(f"Context from Qdrant: {context}")
    except Exception as e:
        logging.error(f"Error during similarity search for chat: {e}")
        context = "No relevant context found."

    # 2. Generate response using OpenAI
    if not openai_chat_client:
        logging.error("OpenAI chat client not initialized.")
        return {"response": "I'm sorry, the chat service is not available."}

    try:
        completion = await openai_chat_client.chat.completions.create(
            model="gpt-3.5-turbo", # Or another suitable model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
                {"role": "user", "content": f"Context: {context}\nQuestion: {user_message}"}
            ]
        )
        bot_response = completion.choices[0].message.content
        logging.info(f"Bot response: {bot_response}")
        return {"response": bot_response}
    except Exception as e:
        logging.error(f"Error generating OpenAI chat completion: {e}")
        raise HTTPException(status_code=500, detail="Error generating response from OpenAI.")
