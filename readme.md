# Real-Time Monitoring and Alerting System with Prometheus, Grafana & Alertmanager

![image_alt](https://github.com/Tatenda-Prince/Full-Stack-Monitoring-Alerting-System-with-Prometheus-Grafana/blob/4dd3804c5c8312ca2bafec5503e73761ff412ed1/screenshots/Screenshot%202025-04-07%20171753.png)

## Project Overview
This project implements a full-stack, real-time monitoring and alerting system using Prometheus, Grafana, Node Exporter, Alertmanager, and a custom Python application. It collects, stores, visualizes, and alerts based on system and application metrics, enabling engineers to proactively respond to anomalies.



## Project Objective
To build an end-to-end monitoring solution that:

1.Collects system and custom app metrics

2.Visualizes key performance indicators (KPIs) in Grafana dashboards

3.Detects anomalies using alert rules

4.Sends real-time notifications via Slack

## Features
1.Monitor CPU, memory, disk, and network usage using Node Exporter

2.Collect and expose custom application metrics (e.g. request counts, latency)

3.Grafana dashboards for system and app-level insights

4.Prometheus alert rules based on usage thresholds

5.Slack notifications via Alertmanager for high CPU or app errors

6.Stress testing support using `stress tool`

## Technology Used
1.Prometheus – Metrics scraping, evaluation & storage

2.Node Exporter – Collects Linux system metrics

3.Grafana – Interactive dashboards and visualization

4.Alertmanager – Routes alerts to Slack

5.Python (Flask) – Custom app metrics exposed via HTTP

6.Slack – Real-time alert notifications

7.Stress – Simulates high CPU load for testing


## Use Case
A Cloud/DevOps team needs real-time insights into server and application health. This system allows them to:

1.Detect when CPU/memory is overutilized

2.Visualize system/app behavior over time

3.Get alerts before outages happen

4.Ensure 99.99% uptime by responding to incidents early


## Prerequisite
1.Ubuntu WSL or Linux environment

2.Docker (optional if containerizing)

3.Slack account and webhook URL

4.Python 3, pip

5.Prometheus, Node Exporter, Grafana, Alertmanager binaries


## Explanation of YAML Files
1.prometheus.yml
```language
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node_exporter'
    static_configs:
      - targets: ['localhost:9100']

  - job_name: 'my_app'
    static_configs:
      - targets: ['localhost:8000']

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['localhost:9093']

rule_files:
  - "alerts.yml"

```
Configures targets to scrape metrics from Prometheus, Node Exporter, and a custom app. Links alert rules and Alertmanager.


2.alerts.yml
```language
groups:
  - name: cpu-alerts
    rules:
      - alert: HighCPUUsage
        expr: 100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100) > 5
        for: 10s
        labels:
          severity: critical
        annotations:
          summary: "🚨 High CPU usage detected on {{ $labels.instance }}"
          description: "CPU usage is above 5% for more than 10 seconds."
```
Defines the alert condition. This one fires when CPU usage >5% for more than 10 seconds.

3.alertmanager.yml
```language
global:
  resolve_timeout: 5m

route:
  receiver: 'slack-notifications'
  group_wait: 10s
  group_interval: 30s
  repeat_interval: 1h

receivers:
  - name: 'slack-notifications'
    slack_configs:
      - api_url: 'https://hooks.slack.com/services/XXXX/XXXX/XXXX'
        channel: '#alerts-channel'
        send_resolved: true
```

Configures Slack as the alert receiver. send_resolved: true allows resolved alerts to also notify.


## Testing the System
1.Run All Services


## Start Prometheus
```language
./prometheus --config.file=prometheus.yml
```

![image_alt](https://github.com/Tatenda-Prince/Full-Stack-Monitoring-Alerting-System-with-Prometheus-Grafana/blob/5878f7ac217ed9e397ae5a9070081b86cc3c09d5/screenshots/Screenshot%202025-04-07%20124918.png)


## Start Node Exporter
```language
./node_exporter
```

![image_alt](https://github.com/Tatenda-Prince/Full-Stack-Monitoring-Alerting-System-with-Prometheus-Grafana/blob/43ad07e9209a8f9b85e060010fc040556861d3c9/screenshots/Screenshot%202025-04-07%20124927.png)


## Start Alertmanager
```language
./alertmanager --config.file=alertmanager.yml
```
![image_alt](https://github.com/Tatenda-Prince/Full-Stack-Monitoring-Alerting-System-with-Prometheus-Grafana/blob/50abb3a82ae98e9e4713261440112bd931f520e7/screenshots/Screenshot%202025-04-07%20133746.png)


## Start Custom App
```language
python app.py
```
![image_alt](https://github.com/Tatenda-Prince/Full-Stack-Monitoring-Alerting-System-with-Prometheus-Grafana/blob/1b28b4f33df2861562b87ec70017dc7011450490/screenshots/Screenshot%202025-04-07%20124904.png)


## Access Grafana Dashboard
2.1.Visit `http://localhost:3000`

2.2.Import or build dashboards using Prometheus as data source

2.3.Monitor CPU, memory, custom metrics

![image_alt]()


## Stress Test the CPU
```language
sudo apt install stress
stress --cpu 4 --timeout 60
```
This simulates high CPU usage. Within 10–30 seconds, you should receive a Slack alert if thresholds are set correctly.

![image_alt]()

2.4.Check for messages in your slack 

![image_alt]()



## Future Enhancements
1.Add email/SMS/Discord notifications

2.Integrate auto-scaling or healing via webhook when alerts fire

3.Export metrics to S3 for long-term analysis

4.Add anomaly detection using ML (e.g., Amazon Lookout for Metrics)

5.Create dashboards for disk, memory, and application error rates

## What I Learned
1.How to design and build a real-time alerting pipeline

2.How Prometheus and Grafana integrate for observability

3.Creating and exposing custom application metrics

4.Writing effective alert rules and testing them

5.Real-world skills for monitoring, incident response, and DevOps best practices


