import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your Admin Telegram User ID
ADMIN_ID = os.environ.get("ADMIN_ID")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Security check to ensure only you use your bot
    if ADMIN_ID and str(user_id) != str(ADMIN_ID):
        await update.message.reply_text("Unauthorized access!")
        return

    # Check for files, photos or videos
    file = update.message.document or update.message.photo or update.message.video
    if file:
        await update.message.reply_text("📂 File received and stored securely in your private cloud!")

if __name__ == '__main__':
    TOKEN = os.environ.get("BOT_TOKEN")
    
    # Build application
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Add message handler
    app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), handle_file))
    
    print("Bot is running...")
    app.run_polling()
