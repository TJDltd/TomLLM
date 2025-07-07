"""Data models for the TomLLM application."""

import pydantic


class InputQuery(pydantic.BaseModel):
    """Model for an input query to the LLM."""

    query: str
