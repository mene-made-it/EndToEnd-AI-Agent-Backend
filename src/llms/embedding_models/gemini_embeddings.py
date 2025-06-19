# src/llms/embedding_models/gemini_embeddings.py

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.embeddings import Embeddings
from src.config.settings import Settings
import logging

logger = logging.getLogger(__name__)

def create_gemini_embedding_model(settings: Settings) -> Embeddings:
    api_key = settings.LLM_EMBEDDING_API_KEY_GOOGLE or settings.LLM_CHAT_API_KEY_GOOGLE
    if not api_key:
        logger.error("GOOGLE_API_KEY not configured for embeddings.")
        raise ValueError("Google (Gemini) API key not found for embeddings.")

    logger.info(f"Creating Gemini Embedding model: {settings.LLM_EMBEDDING_MODEL_NAME}")
    return GoogleGenerativeAIEmbeddings(
        google_api_key=api_key,
        model=settings.LLM_EMBEDDING_MODEL_NAME,
    )