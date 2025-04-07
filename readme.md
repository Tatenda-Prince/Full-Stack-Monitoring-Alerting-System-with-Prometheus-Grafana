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
