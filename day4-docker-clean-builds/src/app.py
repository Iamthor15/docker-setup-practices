
import os
from flask import Flask

app = Flask(__name__)
ENV_MESSAGE = os.getenv("ENV_MESSAGE", "Default Message")

@app.route("/")
def home():
    return f"Message from ENV: {ENV_MESSAGE}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
