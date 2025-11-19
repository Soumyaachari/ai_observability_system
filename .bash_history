wsl
pwd
pwd
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
python3 --version
pip3 --version
wsl --list --verbose
code .
sudo apt install python3.12-venv -y
sudo apt install prometheus -y
sudo nano /etc/prometheus/prometheus.yml
cat /etc/prometheus/prometheus.yml
sudo systemctl restart prometheus
sudo systemctl status prometheus
source venv/bin/activate
cd ai_observability/
ls
source venv/bin/activate
pip install prometheus_client
python3 main.py
sudo nano /etc/prometheus/prometheus.yml
sudo systemctl restart prometheus
sudo systemctl status prometheus
sudo prometheus --config.file=/etc/prometheus/prometheus.yml
sudo nano /etc/prometheus/prometheus.yml
sudo systemctl restart prometheus
sudo systemctl status prometheus
curl http://localhost:9090/targets
hostname -I
curl http://localhost:9090/targets
sudo systemctl restart prometheus
sudo systemctl status prometheus
curl http://localhost:9090/api/v1/targets
pip install scikit-learn pandas requests
python anomaly_detector.py
sudo apt-get install -y apt-transport-https software-properties-common wget
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://packages.grafana.com/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/grafana.gpg
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install -y grafana
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
sudo systemctl status grafana-server
curl http://localhost:8000/metrics
python3 alert_receiver.py
sudo nano /etc/alertmanager/alertmanager.yml
sudo find / -name "alertmanager.yml"
deactivate
exit
mkdir ai_observability
cd ai_observability
python3 -m venv venv
python -m venv venv
python3 -m venv venv
source venv/bin/activate
pip install numpy pandas scikit-learn prometheus-client flask matplotlib
nano main.py
python3 main.py
source venv/bin/activate
python3 main.py
cd ai_observability/
source venv/bin/activate
sudo systemctl start prometheus
sudo systemctl start grafana-server
python3 main.py
deactivate
exit
cd ai_observability/
source venv/bin/activate
sudo systemctl start prometheus
sudo systemctl start grafana-server
python3 main.py
