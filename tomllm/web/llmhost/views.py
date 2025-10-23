"""Views for the LLM host application."""

from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import LLMForm


class LLMFormView(FormView):
    """View for handling LLM requests."""

    template_name = "llmhost/llm_form.html"
    form_class = LLMForm
    success_url = reverse_lazy("llmhost:llm-form")

    def form_valid(self, form):
        """Process valid form data."""
        instance = form.save(commit=False)
        # TODO: Call LLM API here to get response
        instance.response = "LLM response will go here"
        instance.save()
        return super().form_valid(form)
