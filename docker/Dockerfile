# docker/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the package itself
COPY . .
RUN pip install -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "-m", "my_library"]

