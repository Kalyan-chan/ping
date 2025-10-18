import requests
import os

URL = "https://uvaobot.onrender.com/"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(msg: str):
    if TELEGRAM_TOKEN and CHAT_ID:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": msg}
        )

try:
    r = requests.get(URL, timeout=30)
    if r.status_code == 200:
        print(f"✅ {URL} → {r.status_code}")
    else:
        msg = f"⚠️ {URL} вернул статус {r.status_code}"
        print(msg)
        send_telegram(msg)
except Exception as e:
    msg = f"❌ Ошибка при доступе к {URL}: {e}"
    print(msg)
    send_telegram(msg)
