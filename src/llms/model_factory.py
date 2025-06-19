# src/llms/model_factory.py

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.embeddings import Embeddings
from src.config.settings import Settings
from src.llms.chat_models import (
    create_openai_chat_model,
    create_gemini_chat_model,
    create_claude_chat_model
)
from src.llms.embedding_models import (
    create_openai_embedding_model,
    create_gemini_embedding_model,
    create_huggingface_embedding_model
)

import logging
import os


logger = logging.getLogger(__name__)



def get_chat_model(settings: Settings) -> BaseChatModel:
    provider = settings.LLM_CHAT_PROVIDER.lower()

    if provider == "openai":
        return create_openai_chat_model(settings)
    elif provider == "google":
        return create_gemini_chat_model(settings)
    elif provider == "anthropic":
        return create_claude_chat_model(settings)
    else:
        logger.error(f"Unsupported LLM Chat provider: {provider}")
        raise ValueError(f"Unsupported LLM Chat provider: {provider}")




def get_embedding_model(settings: Settings) -> Embeddings:
    provider = settings.LLM_EMBEDDING_PROVIDER.lower()

    if provider == "openai":
        return create_openai_embedding_model(settings)
    elif provider == "google":
        return create_gemini_embedding_model(settings)
    elif provider == "huggingface":
        if settings.HF_API_KEY:
             os.environ["HF_API_KEY"] = settings.HF_API_KEY
        return create_huggingface_embedding_model(settings)
    else:
        logger.error(f"Unsupported LLM Embedding provider: {provider}")
        raise ValueError(f"Unsupported LLM Embedding provider: {provider}")