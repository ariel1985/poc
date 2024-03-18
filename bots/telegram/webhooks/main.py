import os
import logging
import socketserver
import json
from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_API_KEY')
HTTP_PORT = os.getenv('HTTP_SERVER_PORT')
HTTP_CERT = os.getenv('HTTP_SERVER_CERT')
HTTP_KEY = os.getenv('HTTP_SERVER_KEY')
HTTP_WEBHOOK_URL = os.getenv('HTTP_SERVER_WEBHOOK_URL')


##### Create a simple HTTP server to serve the ASGI application
from asgiref.wsgi import WsgiToAsgi

def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'application/json')]
    start_response(status, headers)
    return [json.dumps({'message': 'Hello world! It is I'}).encode()]

asgi_application = WsgiToAsgi(simple_app)
##### End of simple HTTP server


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    
    # application.run_polling(allowed_updates=Update.ALL_TYPES) # listens to all 
    
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks
    application.run_webhook(
        listen='0.0.0.0',
        port=HTTP_PORT,
        secret_token=TOKEN,
        key=HTTP_KEY,
        cert=HTTP_CERT,
        webhook_url=HTTP_WEBHOOK_URL
    )

if __name__ == "__main__":

    main()