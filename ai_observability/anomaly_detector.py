import requests
import pandas as pd
from sklearn.ensemble import IsolationForest
import time
import requests


PROMETHEUS_URL = "http://localhost:9090"

def fetch_metrics(metric_name):
    query = f"{metric_name}[1h]"  # last 1 hour of data
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={"query": query})
    result = response.json()["data"]["result"]

    if not result:
        print(f"No data found for {metric_name}")
        return None

    data = []
    for metric in result:
        for value in metric["values"]:
            timestamp, val = value
            data.append(float(val))
    return pd.DataFrame(data, columns=["value"])

def detect_anomaly(df):
    model = IsolationForest(contamination=0.05, random_state=42)
    df["anomaly"] = model.fit_predict(df[["value"]])
    anomalies = df[df["anomaly"] == -1]
    return anomalies

def monitor_loop():
    while True:
        print("🔍 Fetching metrics...")
        df = fetch_metrics("up")  # 'up' is a simple Prometheus metric
        if df is not None:
            anomalies = detect_anomaly(df)
            print(f"Anomalies detected: {len(anomalies)}")
        else:
            print("No metrics available.")
        time.sleep(60)  # run every minute
        
# ---------------- ALERT SECTION ----------------
if anomalies > 0:
    print("🚨 ALERT: QoE anomaly detected! Sending alert...")

    # Simulate sending an alert (REST API)
    try:
        alert_data = {
            "source": "AI Observability System",
            "message": f"{anomalies} anomalies detected in QoE metrics",
            "severity": "high"
        }
        response = requests.post("http://localhost:5000/alert", json=alert_data)
        if response.status_code == 200:
            print("✅ Alert successfully sent!")
        else:
            print(f"⚠️ Alert sending failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error while sending alert: {e}")


if __name__ == "__main__":
    monitor_loop()
