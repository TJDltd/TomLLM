"""URL patterns for the LLM host application."""

from django.urls import path

from . import views

app_name = "llmhost"

urlpatterns = [
    path("", views.LLMFormView.as_view(), name="llm-form"),
]