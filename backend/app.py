
"""NetPulse Python backend."""

from flask import Flask, jsonify, render_template

app = Flask(
    __name__,
    template_folder="templates",
)

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "netpulse-backend",
    })

@app.get("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Keep the development server accessible only from this machine.
    app.run(host="127.0.0.1", port=5000, debug=False)

