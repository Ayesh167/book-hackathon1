import logging
from qdrant_client import models
from openai import OpenAI
from .__init__ import qdrant_client, OPENAI_API_KEY

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize OpenAI client
try:
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
except Exception as e:
    logging.error(f"Failed to initialize OpenAI client: {e}")
    openai_client = None # Set to None so subsequent calls will fail explicitly

async def get_embedding(text: str) -> list[float]:
    """Generates an embedding for the given text using OpenAI."""
    if not openai_client:
        logging.error("OpenAI client not initialized. Cannot generate embedding.")
        return []
    try:
        response = await openai_client.embeddings.create(input=text, model="text-embedding-ada-002")
        return response.data[0].embedding
    except Exception as e:
        logging.error(f"Error generating embedding for text: '{text[:50]}...': {e}")
        return []

async def similarity_search(collection_name: str, query_text: str, limit: int = 5) -> list[dict]:
    """
    Performs a similarity search on the specified Qdrant collection.

    Args:
        collection_name: The name of the Qdrant collection to search.
        query_text: The text to generate an embedding for and use as the query.
        limit: The maximum number of results to return.

    Returns:
        A list of dictionaries, each representing a search result with payload and score.
    """
    if not qdrant_client:
        logging.error("Qdrant client not initialized. Cannot perform similarity search.")
        return []

    query_vector = await get_embedding(query_text)
    if not query_vector:
        logging.error(f"Could not get embedding for query text: '{query_text[:50]}...'")
        return []

    try:
        search_result = await qdrant_client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=limit,
            query_filter=None, # You can add filters here if needed
            with_payload=True, # Return the stored payload
        )
        results = []
        for hit in search_result:
            results.append({"payload": hit.payload, "score": hit.score})
        logging.info(f"Similarity search successful in collection '{collection_name}' for query '{query_text[:50]}...'")
        return results
    except Exception as e:
        logging.error(f"Error during similarity search in collection '{collection_name}' for query '{query_text[:50]}...': {e}")
        return []