# keep_alive_one_shot.py
import requests

URL = "https://uvaobot.onrender.com/"

try:
    r = requests.get(URL, timeout=30)
    print(f"{URL} → {r.status_code}")
except Exception as e:
    print("Ошибка:", e)
