from flask import Flask, render_template, jsonify
import random
import time
import hashlib

app = Flask(__name__)

previous_hash = "0"

# Initial values
last_temp = 55
last_battery = 80
last_signal = 75

last_anomaly_time = 0

def generate_hash(data_string):
    return hashlib.sha256(data_string.encode()).hexdigest()

def smooth_change(value, min_val, max_val, step=2):
    value += random.uniform(-step, step)
    return max(min(value, max_val), min_val)

def generate_data():
    global previous_hash, last_temp, last_battery, last_signal, last_anomaly_time

    last_temp = smooth_change(last_temp, 20, 85)
    last_battery = smooth_change(last_battery, 30, 100, 1)
    last_signal = smooth_change(last_signal, 50, 100, 1.5)

    current_time = time.time()
    anomaly = False

    # Controlled anomaly every ~10 sec
    if current_time - last_anomaly_time > 10:
        anomaly = True
        last_temp += random.uniform(10, 15)
        last_anomaly_time = current_time

    data = {
        "timestamp": time.strftime("%H:%M:%S"),
        "temperature": round(last_temp, 2),
        "battery": round(last_battery, 2),
        "signal": round(last_signal, 2)
    }

    expected_temp = 60

    data_string = f"{data}{previous_hash}"
    current_hash = generate_hash(data_string)

    block = {
        "data": data,
        "expected_temp": expected_temp,
        "previous_hash": previous_hash,
        "hash": current_hash,
        "anomaly": anomaly
    }

    previous_hash = current_hash

    return block

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(generate_data())

if __name__ == "__main__":
    app.run(debug=True)