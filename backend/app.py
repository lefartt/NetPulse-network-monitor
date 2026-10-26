"""NetPulse Python backend starter.

Run with:
    python app.py

This initial version exposes a local health endpoint. Data ingestion, SQLite,
speed tests and dashboard features will be added in later steps.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "netpulse-backend"})


@app.get("/")
def index():
    return (
        "<h1>NetPulse</h1>"
        "<p>Backend starter is running.</p>"
        '<p>Health check: <a href="/health">/health</a></p>'
    )


if __name__ == "__main__":
    # Local-only by default. Enable LAN access deliberately if needed later.
    app.run(host="127.0.0.1", port=5000, debug=False)
