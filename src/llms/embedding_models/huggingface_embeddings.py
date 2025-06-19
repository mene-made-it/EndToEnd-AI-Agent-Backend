# src/llms/embedding_models/huggingface_embeddings.py

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.embeddings import Embeddings
from src.config.settings import Settings
import logging
import os

logger = logging.getLogger(__name__)

def create_huggingface_embedding_model(settings: Settings) -> Embeddings:
    if settings.HF_API_KEY:
        os.environ["HF_API_KEY"] = settings.HF_API_KEY

    logger.info(f"Creating Hugging Face Embedding model: {settings.LLM_EMBEDDING_MODEL_NAME}")

    try:
        return HuggingFaceEmbeddings(
            model_name=settings.LLM_EMBEDDING_MODEL_NAME,
        )
    except ImportError as e:
        logger.error(f"Dependency missing for Hugging Face Embeddings: {e}")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred while creating Hugging Face Embedding model: {e}")
        raise e