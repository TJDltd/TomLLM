from config import Config

from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider

model = GeminiModel(
    'gemini-2.0-flash', provider=GoogleGLAProvider(api_key=Config.GEMINI_API_KEY)
)

def create_agent():
    return Agent(
        system_prompt='Be concise, reply with one sentence.',
        model=model,
    )

def call_llm(prompt: str, agent: Agent) -> str:
    return agent.run_sync(prompt).output