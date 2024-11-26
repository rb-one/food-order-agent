# Base Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /src

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
RUN mkdir app
COPY app app

# Expose the API port
EXPOSE 8000

# Run FastAPI application with hot reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

