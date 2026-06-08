# Raspberry Pi Cloud Monitoring on AWS

## Project Overview

This project demonstrates a cloud-enabled monitoring solution for a Raspberry Pi. It collects system metrics from the Raspberry Pi and sends them to AWS using an API-driven architecture. The data is stored in DynamoDB and can be queried through AWS Lambda.

## What the project does

- Collects Raspberry Pi metrics: CPU usage, RAM usage, disk usage, temperature, and uptime.
- Sends metrics from the Raspberry Pi to an AWS API Gateway endpoint.
- Uses AWS Lambda to ingest data into DynamoDB.
- Provides a query Lambda function to retrieve recent metrics for visualization or analysis.

## Architecture

1. Raspberry Pi runs `raspberry-pi/metrics_collector.py`.
2. The script posts JSON payloads to an API Gateway endpoint (`/metrics`).
3. API Gateway forwards requests to `aws/lamda/raspi-ingest.py`.
4. `raspi-ingest.py` stores metrics in the DynamoDB table `raspi_metrics`.
5. `aws/lamda/raspi-query.py` can query recent metrics by `device_id`.

## AWS components used

- **API Gateway**
  - Exposes `GET` and `POST` endpoints under `/metrics`.
  - Routes POST requests to the ingest Lambda and GET requests to the query Lambda.

- **AWS Lambda**
  - `raspi-ingest.py`: ingests Raspberry Pi metrics and writes to DynamoDB.
  - `raspi-query.py`: queries DynamoDB for recent metric records and returns JSON.

- **DynamoDB**
  - Table name: `raspi_metrics`
  - Partition key: `device_id` (String)
  - Sort key: `timestamp` (Number)

- **IAM**
  - IAM roles are required for Lambda functions to read/write DynamoDB.
  - Example role JSON files are stored in `aws/IAM/`.

## Raspberry Pi side

The Raspberry Pi script in `raspberry-pi/metrics_collector.py`:

- Reads CPU, RAM, disk usage using `psutil`.
- Reads temperature from `/sys/class/thermal/thermal_zone0/temp`.
- Calculates uptime from system boot time.
- Sends metrics as JSON to the configured `API_URL`.

## Requirements

The Raspberry Pi script depends on:

- `psutil`
- `requests`

See `raspberry-pi/requirements.txt`.

## How to use

1. Configure `API_URL` in `raspberry-pi/metrics_collector.py` to point to your API Gateway POST endpoint.
2. Deploy `raspi-ingest.py` as the ingest Lambda and `raspi-query.py` as the query Lambda.
3. Create the DynamoDB table `raspi_metrics` with the correct keys.
4. Run `metrics_collector.py` on the Raspberry Pi to send metrics.
5. Use the query endpoint to retrieve metrics for display or dashboard use.

## Notes

- This project is meant as a reference implementation for AWS-based Raspberry Pi monitoring.
- The ingest Lambda uses DynamoDB `put_item` to store each payload with a timestamp.
- The query Lambda returns up to 50 recent records for a given `device_id`.

## Next steps

If you want to extend this project, you can add:

- Grafana dashboards using the query endpoint.
- CloudWatch metrics or alarms for threshold notifications.
- A more robust data model with metric aggregation.
- Authentication and authorization on the API Gateway endpoints.
