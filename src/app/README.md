# Django LLM Host

This Django project provides a simple web interface to submit prompts to your custom LLM backend and display responses.

## How to use

1. Start the development server:
   
   ```zsh
   source venv/bin/activate
   python manage.py runserver
   ```

2. Open your browser at http://127.0.0.1:8000/

3. Enter a prompt and submit the form to see the (echoed) response.

## Integrating your LLM

- Edit `llmhost/views.py` to call your LLM backend instead of echoing the prompt.
- The form template is at `llmhost/templates/llmhost/llm_form.html`.

## Project structure
- `llmhost/` – Main app for LLM form and logic
- `webapp/` – Django project settings and URLs

## Requirements
- Python 3.8+
- Django 5.x

## Setup
- Run `python -m venv venv && source venv/bin/activate && pip install django` if not already done.
- Run `python manage.py migrate` to set up the database.

---
This project is for development/demo purposes. Do not use DEBUG=True in production.
