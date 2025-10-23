"""ASGI config for TomLLM web application."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tomllm.web.webapp.settings")

application = get_asgi_application()