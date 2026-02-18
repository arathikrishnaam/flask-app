from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    print("Hello from GitOps v2! This is a simple Flask application.")
    return jsonify({
        "message": "Hello from GitOps version 2! This is a simple Flask application.",
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
