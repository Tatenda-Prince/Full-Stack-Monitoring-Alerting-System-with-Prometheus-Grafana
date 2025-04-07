from flask import Flask, render_template
from prometheus_client import start_http_server, Counter, Summary
import random
import time
import os

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total web requests')
REQUEST_LATENCY = Summary('app_request_latency_seconds', 'Latency of web requests')

# Route
@app.route("/")
@REQUEST_LATENCY.time()
def home():
    REQUEST_COUNT.inc()
    time.sleep(random.uniform(0.1, 0.7))
    return render_template("index.html")

if __name__ == "__main__":
    # Create templates directory if not exists
    os.makedirs("templates", exist_ok=True)

    # Start Prometheus exporter on port 8000
    start_http_server(8000)

    # Start Flask app
    app.run(port=5000)
