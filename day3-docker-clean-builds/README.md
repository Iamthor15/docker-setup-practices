
# Day 3 - Docker Clean Builds: Layer Caching

This example demonstrates how to structure Dockerfiles for efficient layer caching.

## Build & Run

```bash
docker build -t flask-layer-cache .
docker run -p 5000:5000 flask-layer-cache
```

Visit http://localhost:5000 to see: `Docker Layer Caching Demo - Day 3`
