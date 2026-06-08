import psutil
import requests
import time
 
API_URL = "-API-URL-"
 
# Temperature (works on Raspberry Pi OS)
try:
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        temp = round(int(f.read()) / 1000, 1)
except:
    temp = 0
 
payload = {
    "device_id": "raspi-01",
    "cpu": psutil.cpu_percent(interval=1),
    "ram": psutil.virtual_memory().percent,
    "disk": psutil.disk_usage("/").percent,
    "temp": temp,
    "uptime": int(time.time() - psutil.boot_time())
}
 
r = requests.post(API_URL, json=payload)
print(r.status_code, r.text)