import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

table = boto3.resource('dynamodb').Table('raspi_metrics')

def lambda_handler(event, context):

    params = event.get("queryStringParameters") or {}
    device_id = params.get("device_id", "raspi-01")

    response = table.query(
        KeyConditionExpression=Key("device_id").eq(device_id),
        ScanIndexForward=True,
        Limit=50
    )

    items = response.get("Items", [])

    # Convert to Grafana format
    data = []
    for i in items:
        data.append({
            "time": int(i["timestamp"]) * 1000,
            "cpu": float(i.get("cpu", 0)),
            "ram": float(i.get("ram", 0)),
            "disk": float(i.get("disk", 0)),
            "temp": float(i.get("temp", 0))
        })

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(data)
    }