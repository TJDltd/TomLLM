"""URL configuration for TomLLM web application."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tomllm.web.llmhost.urls")),
]