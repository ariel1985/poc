import asyncio
import os
from cls_telegram_bot import TelegramBot

# dotenv
from dotenv import load_dotenv
load_dotenv()

# fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# pydantic
from pydantic import BaseModel

# create a data model for chat poll
class Poll(BaseModel):
    question: str
    options: list[str]
    
    class Config:
        schema_extra = {
            "example": {
                "question": "What's your favorite color?",
                "options": ["Red", "Blue", "Green"]
            }
        }

# --- FastAPI ---

app = FastAPI()

# CORS

# accept all origins
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/send_poll")
async def send_poll(poll: Poll):
    bot = TelegramBot(token, host_url)
    response = await bot.send_poll(chat_id, poll.question, poll.options)
    return {"message": response}

# --- Telegram Bot ---

token = os.getenv("TELEGRAM_BOT_API_KEY")
host_url = os.getenv("TELEGRAM_WEBHOOK_URL")
chat_id = os.getenv("TELEGRAM_BOT_CHAT_ID")

print("Token: ", token)
print("Host URL: ", host_url)
print("Chat ID: ", chat_id)

async def main():
    bot = TelegramBot(token, host_url)
    print("Setting up poll...")
    await bot.send_poll(chat_id, "What's your favorite color?", ["Red", "Blue", "Green"])
    

if __name__ == "__main__":
    asyncio.run(main())