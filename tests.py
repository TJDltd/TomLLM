from fastapi.testclient import TestClient
from src.api import router
from src.models import InputQuery


def test_query():
    client = TestClient(router)

    # Create a sample input query
    input_query = InputQuery(query="What is the capital of France?")

    # Send a POST request to the /query endpoint
    response = client.post("/query", json=input_query.model_dump())

    # Check if the response status code is 200 OK
    assert response.status_code == 200

    # Check if the response contains a string (the expected output)
    assert isinstance(response.json(), str)

    # Optionally, you can check if the response contains expected content
    assert "Paris" in response.json() or "France" in response.json(), (
        "Response should contain the capital of France"
    )
