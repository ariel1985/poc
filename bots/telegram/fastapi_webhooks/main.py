
# main.py

# web framework for building APIs with Python
from fastapi import FastAPI

import httpx
from pydantic import BaseModel

# environment variable dotenv
from dotenv import load_dotenv
import os

load_dotenv()

# ---- DataModels ----
class BotMessage(BaseModel):
    token: str
    status: str
    message: dict

# ---- API ----

# web framework for building APIs with Python
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# 
@app.post("/webhook/{token}")
async def webhook(token: str, message: BotMessage):
    data = {"token": token, "status": "success" , "message": message}
    print("data: ", data)
    return data

# ---- Telegram ----

HOST_URL = os.getenv("TELEGRAM_WEBHOOK_URL")
print("----------------------HOST_URL: ", HOST_URL)
PORT = os.getenv("TELEGRAM_WEBHOOK_PORT")
TOKEN = os.getenv("TELEGRAM_BOT_API_KEY")
TELEGRAM_BOT_URL = f"https://api.telegram.org/bot{TOKEN}"
TELEGRAM_SET_WEBHOOK_URL = f"{TELEGRAM_BOT_URL}/setWebhook"
TELEGRAM_GET_WEBHOOK_INFO_URL = f"{TELEGRAM_BOT_URL}/getWebhookInfo"
TELEGRAM_SEND_MESSAGE_URL = f"{TELEGRAM_BOT_URL}/sendMessage"

"""
An asynchronous function that sends a POST request 
to a specified URL with a given payload.
"""
async def request_post(url, payload):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
    return response

async def get_telegram_webhook_info():
    res = await request_post(TELEGRAM_GET_WEBHOOK_INFO_URL, {})
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
    res = await request_post(TELEGRAM_SET_WEBHOOK_URL, payload)
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
    
    print("\n\n", HOST_URL, "\n\n" )
    
    print('\ncurl -X POST -H "Content-Type: application/json" -d \'{"token": "123", "status": "success", "message": {"text": "Hello World"}}\' ' + HOST_URL + '/webhook/' + TOKEN)
