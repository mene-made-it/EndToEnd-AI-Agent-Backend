# src/llms/chat_models/gemini_chat.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel
from src.config.settings import Settings
import logging

logger = logging.getLogger(__name__)

def create_gemini_chat_model(settings: Settings) -> BaseChatModel:
    """
    Configures and returns a ChatGoogleGenerativeAI instance.
    """

    if not settings.LLM_CHAT_API_KEY_GOOGLE:
        logger.error("GOOGLE_API_KEY not configured.")
        raise ValueError("Google (Gemini) API key not found.")

    logger.info(f"Creating Gemini Chat model: {settings.LLM_CHAT_MODEL_NAME} with temperature {settings.LLM_CHAT_TEMPERATURE}")
    return ChatGoogleGenerativeAI(
        api_key=settings.LLM_CHAT_API_KEY_GOOGLE,
        model=settings.LLM_CHAT_MODEL_NAME,
        temperature=settings.LLM_CHAT_TEMPERATURE,
    )