import fastapi

import call_llm
from src.models import InputQuery

router = fastapi.APIRouter()


@router.post("/query")
def query(input_query: InputQuery) -> str:
    return call_llm.call_llm(input_query.query, call_llm.create_agent())
