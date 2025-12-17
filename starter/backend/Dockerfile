FROM python:3.10-slim-buster

WORKDIR /app

# Install system dependencies for uwsgi
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy Pipfile
COPY Pipfile Pipfile.lock ./

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Install dependencies from Pipfile
RUN pipenv install --system --deploy --ignore-pipfile

# Copy application code
COPY . .

# Set environment variables
ENV FLASK_APP=.
ENV FLASK_RUN_PORT=5000

# Expose port
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
