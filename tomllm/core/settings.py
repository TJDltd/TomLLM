"""Configuration for TomLLM project."""

import os

import dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Project configuration, including API keys and endpoints."""

    dotenv.load_dotenv()

    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    API_URL: str = "http://localhost:8001/query"

    class Config:
        """Pydantic settings config."""

        env_prefix = "TOMLLM_"
