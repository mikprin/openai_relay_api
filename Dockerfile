# Step 1: Use official Python image as base
FROM python:3.10-slim

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Set working directory
WORKDIR /app

# Step 4: Copy requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the FastAPI app code into the container
COPY . .

# Step 6: Expose the port (default 8000) for FastAPI
EXPOSE 8000

# Step 7: Run the FastAPI service using uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
