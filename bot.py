import telebot

TOKEN = "8840037436:AAHZKHvr-Z0RKsd75GQEDzxnY1xZEFu7494"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "بات روی سرور فعال شد 😎")

@bot.message_handler(func=lambda m: True)
def chat(message):
    text = message.text.lower()

    if "سلام" in text:
        bot.reply_to(message, "سلام 😏")
    elif "خوبی" in text:
        bot.reply_to(message, "اوکی‌ام 🤖")
    elif "خفن" in text:
        bot.reply_to(message, "خفن بودن تایید شد 💣")
    else:
        bot.reply_to(message, message.text)

bot.infinity_polling()
