"""Forms for the LLM host application."""

from typing import ClassVar

from django import forms

from .models import LLMRequest


class LLMForm(forms.ModelForm):
    """Form for creating LLM requests."""

    class Meta:
        """Meta options for LLMForm."""

        model = LLMRequest
        fields: ClassVar[list[str]] = ["prompt"]