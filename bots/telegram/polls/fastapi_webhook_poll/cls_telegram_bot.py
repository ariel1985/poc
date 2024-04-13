
# cls_telegram_bot.py

import httpx

class TelegramBot:
    
    def __init__(self, token, host_url,):
        self.TOKEN = token
        self.HOST_URL = host_url
        self.TELEGRAM_API_URL = f"https://api.telegram.org/bot{self.TOKEN}"
        self.TELEGRAM_SET_WEBHOOK_URL = f"{self.TELEGRAM_API_URL}/setWebhook"
        self.TELEGRAM_GET_WEBHOOK_INFO_URL = f"{self.TELEGRAM_API_URL}/getWebhookInfo"

    async def request_post(self, url, payload):
        """An async function that sends a POST request to a URL with a payload."""
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
        return response


    # SEND POLL MESSAGE
    async def send_poll(self, chat_id, question, options):
        """Send a poll to a specific chat."""
        url = f"{self.TELEGRAM_API_URL}/sendPoll"
        payload = {
            "chat_id": chat_id,
            "question": question,
            "options": options
        }
        response = await self.request_post(url, payload)
        return response
    
    # SET UP WEBHOOK

    async def get_telegram_webhook_info(self,):
        """Get the current webhook information."""
        res = await self.request_post(self.TELEGRAM_GET_WEBHOOK_INFO_URL, {})
        # print("\nresponse: ", res.json())
        return res.json()

    async def isset_telegram_webhook_url(self, webhook_url) -> bool:
        """Check if the webhook is already set."""
        # check if the webhook is already set
        webhook_info = await self.get_telegram_webhook_info()
        # print("\n\n webhook_info: ", webhook_info, "\n\n")
        return webhook_info['ok'] and webhook_info['result']['url'] == webhook_url

    async def set_telegram_webhook_url(self,) -> bool:
        """Register the webhook URL."""
        payload = {"url": f"{self.HOST_URL}/webhook/{self.TOKEN}"}
        print("\n\npayload: ", payload, end="\n\n")
        res = await self.request_post(self.TELEGRAM_SET_WEBHOOK_URL, payload)
        print("\n\n req: ", res, end="\n\n")
        return res.status_code == 200
