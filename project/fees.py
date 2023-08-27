import time
import requests

from project import settings


def fee_monitoring():
    print("[Telegram bot] Monitoring fees...")
    while True:
        # get btc fees from mempool
        response = requests.get("https://mempool.space/api/v1/fees/recommended")
        if response.status_code == 200:
            data = response.json()
            requests.post("http://localhost:8000/api/manage-fees/", json=data)
        time.sleep(settings.MEMPOOL_LOOP_TIME_SECONDS)
