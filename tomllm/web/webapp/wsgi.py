"""WSGI config for TomLLM web application."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tomllm.web.webapp.settings")

application = get_wsgi_application()