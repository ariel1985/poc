import os
from cls_telegram_bot import TelegramBot
# import dotenv for environment variables
from dotenv import load_dotenv
load_dotenv()


# ---- Main ----
TOKEN = os.getenv("TELEGRAM_BOT_API_KEY")
HOST_URL = os.getenv("TELEGRAM_WEBHOOK_URL")
print("\n\tHOST_URL: ", HOST_URL, "\n\n")

async def main():
    webhook_url = f"{HOST_URL}/webhook/{TOKEN}"
    # from os env vars or .env
    
    tlgrm = TelegramBot(TOKEN, HOST_URL)
    
    print("Checking if HOST_URL exsits... " )
    is_exsits_webhook = await tlgrm.isset_telegram_webhook_url(webhook_url)
    
    if is_exsits_webhook:
        print("\nTelegram webhook is already set to ", HOST_URL, end="\n\n")
    else:
        # setting the telegram webhook url
        status = await tlgrm.set_telegram_webhook_url()
        print("\nTelegram webhook is now set to ", HOST_URL, end="\n\n")
        print("Status: ", status, end="\n\n")

    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
        
    # print('\ncurl -X POST -H "Content-Type: application/json" -d \'{"token": "123", "status": "success", "message": {"text": "Hello World"}}\' ' + HOST_URL + '/webhook/' + TOKEN)
