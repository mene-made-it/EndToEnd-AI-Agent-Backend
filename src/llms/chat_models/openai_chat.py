# src/llms/chat_models/openai_chat.py

from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel
from src.config.settings import Settings
import logging

logger = logging.getLogger(__name__)

def create_openai_chat_model(settings: Settings) -> BaseChatModel:
    """
    Configures and returns a ChatOpenAI instance.
    """
    if not settings.LLM_CHAT_API_KEY_OPENAI:
        logger.error("OPENAI_API_KEY not configured.")
        raise ValueError("OpenAI API key not found.")

    logger.info(f"Creating OpenAI Chat model: {settings.LLM_CHAT_MODEL_NAME} with temperature {settings.LLM_CHAT_TEMPERATURE}")
    return ChatOpenAI(
        api_key=settings.LLM_CHAT_API_KEY_OPENAI,
        model=settings.LLM_CHAT_MODEL_NAME,
        temperature=settings.LLM_CHAT_TEMPERATURE,
    )