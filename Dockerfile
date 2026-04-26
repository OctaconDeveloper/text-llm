# Use the official llama-cpp-python image which has the backend pre-compiled
FROM ghcr.io/abetlen/llama-cpp-python:latest

# Set working directory
WORKDIR /app

# Install FastAPI and other dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API script
COPY scripts/simple_api.py ./scripts/

# Create models directory (to be mounted as a volume)
RUN mkdir -p models

# Expose the API port
EXPOSE 8001

# Command to run the simple API
CMD ["python3", "scripts/simple_api.py"]
