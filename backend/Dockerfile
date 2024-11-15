# Use Python image
FROM python:3.12-slim

RUN apt update -y
RUN apt install build-essential -y

# Create a new system user
RUN useradd -ms /bin/bash appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"

# Set the working directory in the container
WORKDIR /app

# Change to the non-root user
USER appuser

RUN pip install --upgrade pip

# Copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api api
COPY core core
COPY main.py .

# Command to run the application
CMD ["python", "main.py"]
