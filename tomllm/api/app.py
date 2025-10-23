"""FastAPI application for handling LLM queries."""

from fastapi import FastAPI

from tomllm.api.models import InputQuery
from tomllm.core.llm import call_llm, create_agent

app = FastAPI(title="TomLLM API")


@app.post("/query")
def query(input_query: InputQuery) -> str:
    """Entry point for querying TomLLM."""
    return call_llm(input_query.query, create_agent())


def main() -> None:
    """Run the FastAPI application."""
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
