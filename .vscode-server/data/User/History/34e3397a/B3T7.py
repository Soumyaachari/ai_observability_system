"""     from prometheus_client import Gauge, start_http_server
    from sklearn.ensemble import IsolationForest
    import numpy as np
    import time
    import random

    # --- Step 1: Setup Prometheus metric ---
    qoe_gauge = Gauge("user_qoe_score", "Predicted QoE Score for ISP Customers")

    # --- Step 2: Start Prometheus server on port 8000 ---
    start_http_server(8000)
    print("Prometheus metrics exposed at http://localhost:8000/metrics")

    # --- Step 3: ML Model for anomaly detection ---
    model = IsolationForest(contamination=0.1, random_state=42)

    # Simulated dataset (latency, packet_loss, jitter)
    data = np.array([
        [10, 0.1, 1],
        [20, 0.3, 2],
        [15, 0.2, 1.5],
        [200, 5.0, 10],  # anomaly example
        [12, 0.1, 1]
    ])

    model.fit(data)

    # --- Step 4: Live simulation loop ---
    while True:
        latency = random.uniform(10, 300)
        packet_loss = random.uniform(0, 5)
        jitter = random.uniform(1, 10)

        sample = np.array([[latency, packet_loss, jitter]])
        pred = model.predict(sample)[0]

        qoe_score = max(0, 100 - (latency / 3 + packet_loss * 10 + jitter * 2))
        if pred == -1:  # anomaly detected
            qoe_score -= 20

        qoe_gauge.set(qoe_score)
        print(f"Latency: {latency:.2f}ms | PacketLoss: {packet_loss:.2f}% | Jitter: {jitter:.2f} | QoE: {qoe_score:.2f}")

        time.sleep(2) """

from prometheus_client import start_http_server, Gauge
import random
import time

# Create custom Prometheus metrics to track QoE and latency
qoe_metric = Gauge('user_qoe_score', 'User Quality of Experience Score')
latency_metric = Gauge('network_latency_ms', 'Network latency in milliseconds')

def simulate_metrics():
    """Simulate network observability data."""
    while True:
        qoe_value = random.uniform(60, 100)  # Simulate QoE score
        latency_value = random.uniform(10, 200)  # Simulate latency

        qoe_metric.set(qoe_value)
        latency_metric.set(latency_value)

        print(f"[METRICS] QoE={qoe_value:.2f} | Latency={latency_value:.2f}")
        time.sleep(5)

if __name__ == "__main__":
    # Start up the server to expose metrics at :8000/metrics
    start_http_server(8000)
    print("✅ Metrics server running on http://localhost:8000/metrics")
    simulate_metrics()

