
# Day 4 - Docker Clean Builds: Using Environment Variables

Learn how to securely use environment variables inside Docker containers.

## Build & Run

```bash
docker build -t flask-env-demo .
docker run -p 5000:5000 -e ENV_MESSAGE="Hello from user!" flask-env-demo
```

## Visit:
http://localhost:5000
