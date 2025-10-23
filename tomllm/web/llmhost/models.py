"""Models for the LLM host application."""

from typing import ClassVar

from django.db import models


class LLMRequest(models.Model):
    """Model for storing LLM requests."""

    prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for LLMRequest."""

        ordering: ClassVar[list[str]] = ["-created_at"]

    def __str__(self):
        """Return string representation."""
        return f"LLMRequest {self.id}: {self.prompt[:50]}..."