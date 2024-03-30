import asyncio
import os
from cls_telegram_bot import TelegramBot

# dotenv
from dotenv import load_dotenv
load_dotenv()

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