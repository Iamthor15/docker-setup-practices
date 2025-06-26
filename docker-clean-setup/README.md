# 🚀 docker-clean-setup

A clean, production-ready Docker example using Flask, BuildKit secrets, healthchecks, slim images, and good Dockerfile practices.

---

## 🧠 Why this project?

Most real-world Dockerfiles are slow, insecure, or bloated.  
This repo helps you avoid common mistakes:

- ✅ Slim image
- ✅ Multi-stage ready
- ✅ BuildKit secrets
- ✅ HEALTHCHECK
- ✅ .dockerignore and .gitignore

---

## ⚙️ Requirements

- Docker 20.10+
- BuildKit enabled

```bash
export DOCKER_BUILDKIT=1
```

---

## 🚀 Build & Run

```bash
DOCKER_BUILDKIT=1 docker build \
  --secret id=mysecret,src=secrets/dummy-secret.txt \
  -t clean-app .

docker run -p 5000:5000 clean-app
```

Or with Compose:

```bash
docker compose up --build
```

---

## 📦 Folder Structure

```
.
├── app/                # Flask app
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
└── secrets/            # Mount-only, never committed
```

---

## 🧪 Healthcheck

This line in Dockerfile ensures container health is monitored:

```Dockerfile
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1
```

---

## 📢 License

MIT © [Iamthor15](https://github.com/Iamthor15)
