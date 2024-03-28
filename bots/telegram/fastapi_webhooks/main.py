
# main.py

# web framework for building APIs with Python
from fastapi import FastAPI, Request

# import TelegramBot class from cls_telegram_bot
from cls_telegram_bot import TelegramBot

# Data validation and settings management using python type annotations
from pydantic import BaseModel

# environment variable dotenv
from dotenv import load_dotenv
import os

load_dotenv()

# ---- DataModels ----
class Chat(BaseModel):
    id: int

class Message(BaseModel):
    chat: Chat
    text: str

class BotMessage(BaseModel):
    token: str
    status: str
    message: Message

# ---- API ----

# web framework for building APIs with Python
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/webhook/{token}")
async def webhook(token: str, request: Request):
    data = await request.json()
    message = Message(**data.get('message', {}))
    print("Message text: ", message.text)
    print("Chat ID: ", message.chat.id)
    print("data: ", data)
    return data


# ---- Telegram ----

TOKEN = os.getenv("TELEGRAM_BOT_API_KEY")
HOST_URL = os.getenv("TELEGRAM_WEBHOOK_URL")
print("\n\tHOST_URL: ", HOST_URL, "\n\n")

async def main():
    webhook_url = f"{HOST_URL}/webhook/{TOKEN}"
    print("webhook_url to check: ", webhook_url)
    
    tlgrm = TelegramBot(TOKEN, HOST_URL)
    
    is_exsits_webhook = await tlgrm.isset_telegram_webhook_url(webhook_url)
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
