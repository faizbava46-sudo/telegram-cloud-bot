import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your Admin Telegram User ID (Replace with your actual numeric ID if needed, or leave it to accept your messages)
ADMIN_ID = os.environ.get("ADMIN_ID")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Optional: Security check to make sure only you use your bot
    if ADMIN_ID and str(user_id) != str(ADMIN_ID):
        await update.message.reply_text("Unauthorized access!")
        return

    # Forward or save file info
    file = update.message.document or update.message.photo or update.message.video
    if file:
        await update.message.reply_text("📂 File received and stored securely in your private cloud!")

if __name__ == '__main__':
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), handle_file))
    
    print("Bot is running...")
    app.run_polling()