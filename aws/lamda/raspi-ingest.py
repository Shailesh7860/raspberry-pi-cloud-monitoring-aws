import json
import time
import boto3
from decimal import Decimal

table = boto3.resource('dynamodb').Table('raspi_metrics')

def lambda_handler(event, context):

    try:
        body = {}

        # ---------------------------
        # HANDLE POST (Raspberry Pi)
        # ---------------------------
        if event.get("body"):
            body = json.loads(event["body"])

        # ---------------------------
        # SAFE FALLBACK (GET test)
        # ---------------------------
        else:
            body = event.get("queryStringParameters") or {}

        device_id = body.get("device_id", "raspi-01")
        cpu = body.get("cpu", 0)
        ram = body.get("ram", 0)
        disk = body.get("disk", 0)
        temp = body.get("temp", 0)
        
        table.put_item(
            Item={
                "device_id": device_id,
                "timestamp": int(time.time()),
                "cpu": Decimal(str(cpu)),
                "ram": Decimal(str(ram)),
                "disk": Decimal(str(disk)),
                "temp": Decimal(str(temp))
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"ok": True})
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }