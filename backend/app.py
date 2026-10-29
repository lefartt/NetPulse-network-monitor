
"""NetPulse Python backend."""

import time
from urllib.error import URLError
from urllib.request import Request, urlopen

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


@app.get("/api/network-check")
def network_check():
    """Check external internet connectivity and HTTP response time."""
    url = "https://www.google.com/generate_204"
    request = Request(
        url,
        headers={"User-Agent": "NetPulse/1.0"},
    )

    start_time = time.perf_counter()

    try:
        with urlopen(request, timeout=5) as response:
            response_time_ms = round(
                (time.perf_counter() - start_time) * 1000,
                2,
            )

            return jsonify({
                "connected": response.status == 204,
                "response_time_ms": response_time_ms,
                "status_code": response.status,
            })

    except (URLError, TimeoutError, OSError) as error:
        return jsonify({
            "connected": False,
            "response_time_ms": None,
            "error": str(error),
        }), 200


if __name__ == "__main__":
    # Keep the development server accessible only from this machine.
    app.run(host="127.0.0.1", port=5000, debug=False)

