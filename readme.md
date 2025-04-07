# Real-Time Monitoring and Alerting System with Prometheus, Grafana & Alertmanager
![image_alt]()

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