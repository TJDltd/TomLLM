"""LLM call logic for TomLLM project."""

import os

from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider

from src.config import Config
from src.system_prompt import SYSTEM_PROMPT

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CV_FILE_PATH = os.path.join(BASE_DIR, "CV-22-05-2025.txt")

model = GeminiModel("gemini-2.0-flash", provider=GoogleGLAProvider(api_key=Config.GEMINI_API_KEY))


def _load_prompt() -> str:
    """Load the system prompt and CV content for the LLM."""
    with open(CV_FILE_PATH) as file:
        cv_content = file.read()

    return SYSTEM_PROMPT + cv_content


def create_agent() -> Agent:
    """Create an Agent instance with the system prompt and model."""
    return Agent(
        system_prompt=_load_prompt(),
        model=model,
    )


def call_llm(prompt: str, agent: Agent) -> str:
    """Call the LLM synchronously and return the output."""
    return agent.run_sync(prompt).output
