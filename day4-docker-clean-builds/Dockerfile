
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV ENV_MESSAGE="Hello from Docker ENV!"

CMD ["python", "src/app.py"]
