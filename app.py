from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from root!")

@app.route("/hello")
def hello():
    return jsonify(message="Hello from /hello!")

@app.route("/healthz")
def health_check():
    return jsonify(
        status="healthy",
        message="Application is running",
        env_test=os.getenv("TEST", "not set")
    ), 200

@app.route("/readiness")
def readiness_check():
    return jsonify(
        status="ready",
        message="Application is ready to serve traffic"
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)