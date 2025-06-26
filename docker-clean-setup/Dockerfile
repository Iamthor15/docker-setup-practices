# syntax=docker/dockerfile:1.4
FROM python:3.12-slim AS base

# BuildKit secret mount
RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY app/ ./app/
COPY requirements.txt ./

# Use secrets with BuildKit
RUN --mount=type=secret,id=mysecret \
    cat /run/secrets/mysecret && \
    pip install -r requirements.txt

COPY . .

EXPOSE 5000

# Add a healthcheck
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1

CMD ["python", "app/main.py"]
