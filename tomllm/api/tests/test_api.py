"""Tests for the TomLLM API endpoints."""

import fastapi
import pytest
from fastapi.testclient import TestClient

from tomllm.api.app import app
from tomllm.api.models import InputQuery

client = TestClient(app)

@pytest.fixture(scope="session")
def llm_response() -> fastapi.Response:
    """Fixture for creating a sample InputQuery."""
    query = InputQuery(query="What is the capital of France?")

    return client.post("/query", json=query.model_dump())

def test_query_response_code(llm_response: fastapi.Response):
    """Check the response code LLM response."""
    # Check if the response status code is 200 OK
    assert llm_response.status_code == 200


def test_query_response_text(llm_response: fastapi.Response):
    """Check the text in LLM response."""
    assert "Paris" not in llm_response.json(), (
        "Response should contain tell the user they are too nosy when off topic"
    )
