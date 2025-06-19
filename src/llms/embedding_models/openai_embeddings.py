# src/llms/embedding_models/openai_embeddings.py

from langchain_openai import OpenAIEmbeddings
from langchain_core.embeddings import Embeddings
from src.config.settings import Settings
import logging

logger = logging.getLogger(__name__)

def create_openai_embedding_model(settings: Settings) -> Embeddings:
    api_key = settings.LLM_EMBEDDING_API_KEY_OPENAI or settings.LLM_CHAT_API_KEY_OPENAI
    if not api_key:
        logger.error("OPENAI_API_KEY not configured for embeddings.")
        raise ValueError("OpenAI API key not found for embeddings.")

    logger.info(f"Creating OpenAI Embedding model: {settings.LLM_EMBEDDING_MODEL_NAME}")
    return OpenAIEmbeddings(
        api_key=api_key,
        model=settings.LLM_EMBEDDING_MODEL_NAME,
    )