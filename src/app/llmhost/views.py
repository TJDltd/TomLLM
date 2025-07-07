from django.shortcuts import render
import requests
from src.config import Config


def llm_form(request):
    response = None
    prompt = ""
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        if prompt:
            # Call the FastAPI endpoint instead of calling the LLM directly
            api_url = getattr(Config, "API_URL", "http://localhost:8001/query")
            try:
                api_response = requests.post(
                    api_url,
                    json={"query": prompt},
                    timeout=30
                )
                if api_response.status_code == 200:
                    response = api_response.text
                else:
                    response = f"Error: {api_response.status_code} - {api_response.text}"
            except Exception as e:
                response = f"API call failed: {e}"
    return render(request, "llmhost/llm_form.html", {"response": response, "prompt": prompt})
