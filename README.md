# Satellite Digital Twin

# A real-time satellite telemetry monitoring simulation with an interactive dashboard.

## Features

- Live satellite telemetry simulation
- Temperature monitoring
- Battery monitoring
- Signal strength monitoring
- Real-time telemetry graphs
- Satellite orbit animation
- Automatic anomaly detection simulation
- Anomaly counter and event log
- SHA-256 hash-based data integrity tracking
- Previous-hash tracking for telemetry data



## Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript
- Chart.js
- SHA-256
- Canvas API

## How It Works

The Flask backend generates simulated satellite telemetry data for temperature, battery level, and signal strength.

The system introduces controlled temperature anomalies periodically. When an anomaly occurs, the dashboard displays an alert and records it in the event log.

Each telemetry update is linked to the previous update using SHA-256 hashing, providing a simple demonstration of chained data integrity.

The frontend continuously fetches new telemetry data and displays it through live graphs, status indicators, an event log, and an animated orbit simulation.

## Project Structure

```text
satellite-digital-twin/
├── app.py
└── templates/
    └── index.html
```

## Running the Project

Install Flask:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Then open the local Flask address shown in the terminal in your browser.

## Note

This project is a simulation and does not use real satellite telemetry. It demonstrates real-time monitoring, anomaly simulation, data visualization, and chained data integrity using SHA-256.
