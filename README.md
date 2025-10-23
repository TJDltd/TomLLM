# TomLLM

A Django web application with FastAPI backend for hosting a custom LLM project.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Setup

1. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:
```bash
git clone https://github.com/TJDltd/TomLLM.git
cd TomLLM
```

3. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate
```

4. Install dependencies:
```bash
uv pip sync uv.lock
```

## Running the Application

The project consists of two parts:
1. Django web interface (port 8000)
2. FastAPI backend (port 8001)

### Using uv run commands

Start the Django development server:
```bash
uv run django
```

Start the FastAPI backend:
```bash
uv run api
```

The web interface will be available at http://localhost:8000

## Docker

You can also run both services using Docker:

1. Build the image:
```bash
docker build -t tomllm-app .
```

2. Run the container:
```bash
docker run -p 8000:8000 -p 8001:8001 tomllm-app
```