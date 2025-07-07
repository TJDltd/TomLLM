from django.shortcuts import render
from src.call_llm import create_agent, call_llm

def llm_form(request):
    response = None
    prompt = ''
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        agent = create_agent()
        response = call_llm(prompt, agent)
    return render(request, 'llmhost/llm_form.html', {'response': response, 'prompt': prompt})
