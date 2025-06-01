from config import Config

from google import genai

client = genai.Client(api_key=Config.GOOGLE_API_KEY)

def call_llm(prompt: str, model: str = "gemini-2.0-flash") -> str:
    return client.models.generate_content(model=model, contents=prompt).text