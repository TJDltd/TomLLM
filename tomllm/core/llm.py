"""LLM integration for TomLLM."""

from pathlib import Path

from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider

from tomllm.core.settings import Settings

settings = Settings()
BASE_DIR = Path(__file__).parent.parent
CV_FILE_PATH = BASE_DIR / "core" / "CV-22-05-2025.txt"

model = GeminiModel(
    "gemini-2.0-flash",
    provider=GoogleGLAProvider(api_key=settings.GEMINI_API_KEY),
)


def _load_prompt() -> str:
    """Load the system prompt and CV content for the LLM."""
    with open(CV_FILE_PATH) as file:
        cv_content = file.read()

    with open(BASE_DIR / "core" / "prompts" / "system.txt") as file:
        system_prompt = file.read()

    return system_prompt + cv_content


def create_agent() -> Agent:
    """Create an Agent instance with the system prompt and model."""
    return Agent(
        system_prompt=_load_prompt(),
        model=model,
    )


def call_llm(prompt: str, agent: Agent) -> str:
    """Call the LLM synchronously and return the output."""
    return agent.run_sync(prompt).output
