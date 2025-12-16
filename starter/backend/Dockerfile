FROM python:3.10-alpine

ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Create app user
RUN adduser -u 1000 -D app

# Install system dependencies
RUN apk update && apk add --no-cache \
    build-base \
    gcc \
    linux-headers \
    pcre \
    pcre-dev \
    libffi-dev \
    openssl \
    && pip install --no-cache-dir pipenv uwsgi

# Set working directory
WORKDIR /app

# Copy dependency files
COPY Pipfile Pipfile.lock ./

# Install python dependencies
RUN pipenv install --system --deploy

# Copy application code
COPY . .

# Switch to non-root user
USER app

# Run app
CMD ["uwsgi", "--http", ":5000", "--master", "--enable-threads", "--mount", "/=app:app"]
