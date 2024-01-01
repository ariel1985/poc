from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# import env variables for Token and Bot Username
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN: Final = os.getenv('TELEGRAM_BOT_API_KEY')
BOT_USERNAME: Final = os.getenv('TELEGRAM_BOT_USERNAME')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, lets talk :)')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Here to help')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom command at your service')
    
# Responses

def handle_response(text: str) -> str: 
    
    processed: str = text.lower()
    
    if 'ro' in processed:
        return 'I am a handled response'

    return 'I do not understand.'



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User({update.message.chat.id}) in {message_type}: "{text}')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('Bot: ', response)
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    app.add_error_handler(error)
    
    # Polls the bot - aka waiting for someone to write to it
    print('Polling...')
    app.run_polling(poll_interval=3)
    