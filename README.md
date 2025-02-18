# 🥏System `CPU`, `Memory` Monitoring Dashboard🎢

## 🚩OutPut
![python moniter](https://github.com/user-attachments/assets/7d5baf62-d932-482a-9f1f-607508ee0ee8)



Welcome to the System Monitoring Dashboard project! This dashboard provides real-time monitoring of CPU and memory usage through a web interface.

## Table of Contents
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Running Locally](#running-locally)
- [Dockerization](#dockerization)
- [Deploy to kubernetes](#deploy-to-kubernetes)

## Requirements
Make sure you have the following dependencies installed before running the application:

- Python 3.6 or higher
- Flask
- psutil

You can install the required Python packages by running:
```bash
pip install -r requirements.txt

```
## Getting Started
```
git clone https://github.com/your-username/system-monitoring-dashboard.git
cd system-monitoring-dashboard
```
## Running Locally 
```
python app.py
```
# Dockerization
```
docker build -t system-monitoring-dashboard .
```
## Run  the Docker Container
```
docker run -p 5000:5000 system-monitoring-dashboard
```

# Deploy to Kubernetes
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
## check status of your deployment
```
kubectl get deployments
```
## Check the status of pods
```
kubectl get pods
```
## Once the pod are running check the status of service 
```
kubectl get services
```
