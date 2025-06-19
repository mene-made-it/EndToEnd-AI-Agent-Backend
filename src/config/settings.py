# src/config/settings.py

import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

    APP_ENV: str = os.getenv("APP_ENV", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    API_V1_PREFIX: str = "/api/v1"

    LLM_CHAT_PROVIDER: str = os.getenv("LLM_CHAT_PROVIDER", "openai")
    LLM_CHAT_MODEL_NAME: str = os.getenv("LLM_CHAT_MODEL_NAME", "gpt-4o")
    LLM_CHAT_TEMPERATURE: float = float(os.getenv("LLM_CHAT_TEMPERATURE", "0.7"))
    LLM_CHAT_API_KEY_OPENAI: str = os.getenv("LLM_CHAT_API_KEY_OPENAI", "")
    LLM_CHAT_API_KEY_GOOGLE: str = os.getenv("LLM_CHAT_API_KEY_GOOGLE", "")
    LLM_CHAT_API_KEY_ANTHROPIC: str = os.getenv("LLM_CHAT_API_KEY_ANTHROPIC", "")

    LLM_EMBEDDING_PROVIDER: str = os.getenv("LLM_EMBEDDING_PROVIDER", "openai")
    LLM_EMBEDDING_MODEL_NAME: str = os.getenv("LLM_EMBEDDING_MODEL_NAME", "text-embedding-3-small")
    LLM_EMBEDDING_API_KEY_OPENAI: str = os.getenv("LLM_EMBEDDING_API_KEY_OPENAI", "")
    LLM_EMBEDDING_API_KEY_GOOGLE: str = os.getenv("LLM_EMBEDDING_API_KEY_GOOGLE", "")
    HF_API_KEY: str = os.getenv("HF_API_KEY", "")

    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME", "agent_collection")

    LANGGRAPH_CHECKPOINT_PROVIDER: str = os.getenv("LANGGRAPH_CHECKPOINT_PROVIDER", "redis")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")


settings = Settings()