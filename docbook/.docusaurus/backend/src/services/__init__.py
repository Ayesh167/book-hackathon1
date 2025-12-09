import os
from qdrant_client import QdrantClient
from dotenv import dotenv_values

# Load environment variables from .env file
config = dotenv_values(".env")

# Define required environment variables
REQUIRED_ENV_VARS = [
    "QDRANT_HOST",
    "QDRANT_API_KEY",
    "OPENAI_API_KEY"
]

# Validate environment variables
for var in REQUIRED_ENV_VARS:
    if not config.get(var):
        raise ValueError(f"Missing required environment variable: {var}")

# Initialize Qdrant client
qdrant_client = QdrantClient(
    host=config["QDRANT_HOST"],
    api_key=config["QDRANT_API_KEY"],
)

# Export environment variables for other services if needed
QDRANT_HOST = config["QDRANT_HOST"]
QDRANT_API_KEY = config["QDRANT_API_KEY"]
OPENAI_API_KEY = config["OPENAI_API_KEY"]
