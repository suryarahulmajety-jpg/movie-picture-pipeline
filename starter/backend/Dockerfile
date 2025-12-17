FROM python:3.10-slim-buster

WORKDIR /app

# Copy requirements
COPY Pipfile Pipfile.lock ./

# Install pipenv and export to requirements.txt, then install with pip
RUN pip install pipenv && \
    pipenv requirements > requirements.txt && \
    pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
