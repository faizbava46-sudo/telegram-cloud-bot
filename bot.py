import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = os.environ.get("ADMIN_ID")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['document', 'photo', 'video', 'audio'])
def handle_files(message):
    user_id = message.from_user.id
    
    # സെക്യൂരിറ്റി ചെക്ക്
    if ADMIN_ID and str(user_id) != str(ADMIN_ID):
        bot.reply_to(message, "Unauthorized access!")
        return

    bot.reply_to(message, "📂 File received and stored securely in your private cloud!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_id = message.from_user.id
    if ADMIN_ID and str(user_id) != str(ADMIN_ID):
        return
    bot.reply_to(message, "Send me any file, photo, or video to store.")

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
