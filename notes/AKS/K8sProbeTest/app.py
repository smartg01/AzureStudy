from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

# Simulate an application that might take time to start or become unhealthy
is_ready = False
is_healthy = True
startup_time = 5  # Simulate startup taking 5 seconds
unhealthy_after = 15 # Simulate becoming unhealthy after 15 seconds

@app.route('/')
def hello():
    return jsonify({"message": "Hello from the demo app!"})

@app.route('/readyz')
def readyz():
    global is_ready
    if time.time() > startup_time:
        is_ready = True
    if is_ready:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "not ready"}), 503

@app.route('/livez')
def livez():
    global is_healthy
    if time.time() > unhealthy_after:
        is_healthy = False
    if is_healthy:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "unhealthy"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)