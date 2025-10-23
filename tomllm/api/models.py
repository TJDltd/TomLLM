"""Data models for the TomLLM API."""

from pydantic import BaseModel


class InputQuery(BaseModel):
    """Model for an input query to the LLM."""

    query: str
