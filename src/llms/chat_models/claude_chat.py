# src/llms/chat_models/claude_chat.py

from langchain_anthropic import ChatAnthropic
from langchain_core.language_models.chat_models import BaseChatModel
from src.config.settings import Settings
import logging

logger = logging.getLogger(__name__)

def create_claude_chat_model(settings: Settings) -> BaseChatModel:
    """
    Configures and returns a ChatAnthropic instance.
    """

    if not settings.LLM_CHAT_API_KEY_ANTHROPIC:
        logger.error("ANTHROPIC_API_KEY not configured.")
        raise ValueError("Anthropic (Claude) API key not found.")

    logger.info(f"Creating Claude Chat model: {settings.LLM_CHAT_MODEL_NAME} with temperature {settings.LLM_CHAT_TEMPERATURE}")
    return ChatAnthropic(
        api_key=settings.LLM_CHAT_API_KEY_ANTHROPIC,
        model=settings.LLM_CHAT_MODEL_NAME,
        temperature=settings.LLM_CHAT_TEMPERATURE,

    )