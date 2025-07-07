"""FastAPI router for handling LLM queries."""
import fastapi

import call_llm
from src.models import InputQuery

router = fastapi.APIRouter()


@router.post("/query")
def query(input_query: InputQuery) -> str:
    """Entry point for querying TomLLM."""
    return call_llm.call_llm(input_query.query, call_llm.create_agent())
