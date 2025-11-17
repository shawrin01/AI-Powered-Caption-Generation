# Base image with Python 3.10
FROM python:3.10-slim

# Install essential system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your BLIP model and server code
COPY blip_model ./blip_model
COPY caption_server.py .
COPY requirements.txt .

# Install Python dependencies (Torch + Transformers etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "caption_server:app", "--host", "0.0.0.0", "--port", "8000"]
