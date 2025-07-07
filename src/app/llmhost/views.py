"""Django view for TomLLM web app, calling FastAPI backend for LLM queries."""

import requests
from django.shortcuts import render

from src.config import Config


def llm_form(request):
    """Render the LLM form and handle prompt submission via FastAPI backend."""
    response = None
    prompt = ""
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        if prompt:
            http_ok = 200
            api_url = getattr(Config, "API_URL", "http://localhost:8001/query")
            try:
                api_response = requests.post(
                    api_url,
                    json={"query": prompt},
                    timeout=30,
                )
                if api_response.status_code == http_ok:
                    response = api_response.text
                else:
                    response = f"Error: {api_response.status_code} - {api_response.text}"
            except Exception as exc:
                response = f"API call failed: {exc}"
    return render(request, "llmhost/llm_form.html", {"response": response, "prompt": prompt})
