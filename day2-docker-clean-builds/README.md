
# Day 2 - Docker Clean Builds: Multi-Stage Dockerfile

This example demonstrates how to use a multi-stage Dockerfile to build a small, production-ready Flask app image.

## Build & Run

```bash
docker build -f Dockerfile.multi -t flask-clean-multi .
docker run -p 5000:5000 flask-clean-multi
```

## What's inside?

- Build dependencies are isolated to the build stage
- Smaller image size
- Secure and CI/CD friendly
