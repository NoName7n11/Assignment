from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify(status="ok", service="2")

@app.route("/hello")
def hello():
    return jsonify(message="Hello from Service 2")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)

healthcheck = {
    "test": ["CMD", "curl", "-f", "http://localhost:8002/ping"],
    "interval": "10s",
    "retries": 3
}