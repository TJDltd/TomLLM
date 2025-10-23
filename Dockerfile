# Dockerfile for TomLLM: Django web app and FastAPI backend in one container

FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app
ENV PYTHONPATH=/app:/app/src

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Expose ports for Django (8000) and FastAPI (8001)
EXPOSE 8000 8001

# Start both Django and FastAPI using supervisord
RUN pip install supervisor
COPY docker/supervisord.conf /etc/supervisord.conf

CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]
