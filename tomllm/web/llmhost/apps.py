"""Django app configuration for LLM host."""

from django.apps import AppConfig


class LLMHostConfig(AppConfig):
    """Configuration for LLM host application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "tomllm.web.llmhost"