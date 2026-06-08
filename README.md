# Raspberry Pi Cloud Monitoring System (Prometheus + AWS Managed Metrics)

📌 Overview

Built a lightweight cloud monitoring system for a Raspberry Pi using Prometheus and AWS Managed Prometheus. The system collects system-level metrics (CPU, RAM, temperature, uptime) and stores them in the cloud for long-term monitoring and visualization through Grafana.

---

⚙️ Architecture

Raspberry Pi collects system metrics (CPU, RAM, disk, temperature, network)

Raspberry Pi exposes metrics via a Prometheus exporter (/metrics endpoint)

Local Prometheus server scrapes metrics from the Pi exporter

Prometheus uses remote_write to send metrics to AWS Managed Prometheus

Grafana queries AWS Managed Prometheus for visualization and dashboards

---

🧠 Key Features

Real-time system monitoring from Raspberry Pi

Prometheus-based time-series data collection

Decoupled architecture with local scraping + cloud storage

Scalable cloud metrics backend using AWS Managed Prometheus

Grafana dashboards for visualization and analysis

No inbound network access required (outbound-only data flow)

---

🛠️ Technologies Used

Raspberry Pi (Python system metrics exporter)

Prometheus (local scraping and time-series storage)

Amazon Managed Prometheus (cloud metrics backend)

Grafana (dashboard and visualization layer)

Python (psutil, custom metrics exporter)

AWS IAM (for secure remote_write authentication)

---

📊 What I Learned

How Prometheus scrapes and stores time-series metrics

Difference between push vs pull monitoring models

Using remote_write to integrate local systems with cloud observability

Designing hybrid edge + cloud monitoring systems

Working with AWS Managed Prometheus and Grafana dashboards

Monitoring system-level metrics (CPU, RAM, temperature, uptime)

---

⚠️ Notes

Prometheus runs locally on the Raspberry Pi only for scraping and short-term storage.

Long-term storage and querying is handled by AWS Managed Prometheus.

The system uses outbound-only communication (no need for public IP, VPN, or Tailscale).

This architecture is optimized for learning modern observability patterns used in production systems.
