"""Configuration for TomLLM project."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Project configuration, including API keys and endpoints."""

    GEMINI_API_KEY: str = "AIzaSyBIyImJorYHJCNwA4Wv0TOIThPXcNpF1Uc"
    API_URL: str = "http://localhost:8001/query"

    class Config:
        """Pydantic settings config."""

        env_prefix = "TOMLLM_"