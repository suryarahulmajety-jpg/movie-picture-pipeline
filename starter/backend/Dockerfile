FROM python:3.10-slim-buster

WORKDIR /app

# Copy Pipfile
COPY Pipfile Pipfile.lock ./

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Install only the packages we need (skip uwsgi which needs gcc)
RUN pipenv install flask flask-cors pytest --skip-lock

# Copy application code
COPY . .

# Set environment variables
ENV FLASK_APP=.
ENV FLASK_RUN_PORT=5000

# Expose port
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
