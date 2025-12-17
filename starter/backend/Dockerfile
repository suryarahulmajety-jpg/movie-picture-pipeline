FROM python:3.10-slim-buster

WORKDIR /app

# Copy application code first
COPY . .

# Install dependencies directly with pip
RUN pip install --no-cache-dir flask flask-cors pytest

# Set environment variables
ENV FLASK_APP=.
ENV FLASK_RUN_PORT=5000

# Expose port
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
