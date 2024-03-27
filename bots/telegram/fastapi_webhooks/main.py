
# main.py

# web framework for building APIs with Python
from fastapi import FastAPI

import httpx

# environment variable dotenv
from dotenv import load_dotenv
import os

load_dotenv()


# ---- API ----

# web framework for building APIs with Python
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/webhook/{token}")
def read_root():
    return {"Hello": "Webhook token"}


# ---- Telegram ----

HOST_URL = os.getenv("TELEGRAM_WEBHOOK_URL")
PORT = os.getenv("TELEGRAM_WEBHOOK_PORT")
TOKEN = os.getenv("TELEGRAM_BOT_API_KEY")
# webhook_security = OnlyTelegramNetworkWithSecret(real_secret="your-secret-from-config-or-env")
# TODO: possible upgrades
#  - move {secret} to path
#  - use OnlyTelegramNetworkWithSecret as dependency:

TELEGRAM_BOT_URL = f"https://api.telegram.org/bot{TOKEN}"
TELEGRAM_SET_WEBHOOK_URL = f"{TELEGRAM_BOT_URL}/setWebhook"
TELEGRAM_GET_WEBHOOK_INFO_URL = f"{TELEGRAM_BOT_URL}/getWebhookInfo"
# TELEGRAM_SEND_MESSAGE_URL = f"{TELEGRAM_BOT_URL}/sendMessage"

"""
An asynchronous function that sends a POST request 
to a specified URL with a given payload.
"""
async def request_json(url, payload):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
    return response

async def get_telegram_webhook_info():
    res = await request_json(TELEGRAM_GET_WEBHOOK_INFO_URL, {})
    print("response: ", res.json())
    return res.json()

async def isset_telegram_webhook_url(webhook_url) -> bool:
    # check if the webhook is already set
    webhook_info = await get_telegram_webhook_info()
    
    print(f"Webhook info: {webhook_info['result']['url']}")
    
    return webhook_info['ok'] and webhook_info['result']['url'] == webhook_url

async def set_telegram_webhook_url() -> bool:
    payload = {"url": f"{HOST_URL}/webhook/{TOKEN}"}
    print("payload: ", payload)
    res = await request_json(TELEGRAM_SET_WEBHOOK_URL, payload)
    print("\n\n req: ", res, "\n\n")
    return res.status_code == 200

async def main():
    webhook_url = f"{HOST_URL}/webhook/{TOKEN}"
    print("webhook_url to check: ", webhook_url)
    
    is_exsits_webhook = await isset_telegram_webhook_url(webhook_url)
    print("is_exsits_webhook: ", "Yes" if is_exsits_webhook else "No")
    
    if not is_exsits_webhook:
        # setting the telegram webhook url
        status = await set_telegram_webhook_url()
        print("telegram webhook status: ", status)

    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())