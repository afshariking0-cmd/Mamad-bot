import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# 🔑 کلیدها
TOKEN = "8745349919:AAEJ9qWkz7roGlIYo8yzFeJCLN0VEuF_RX8"
API_KEY = "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"

# ===== AI Function =====
def ask_ai(text):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "تو یک ربات فارسی خیلی باحال و کمک‌کننده هستی 🤖🔥"},
            {"role": "user", "content": text}
        ],
        "max_tokens": 300
    }

    try:
        r = requests.post(url, headers=headers, json=data, timeout=20)
        res = r.json()

        if "choices" in res:
            return res["choices"][0]["message"]["content"]

        return f"⚠️ API Error: {res}"

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# ===== Message Handler =====
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip()

    # فقط پیام + دار جواب بده
    if not msg.endswith("+"):
        return

    msg = msg[:-1].strip()

    if not msg:
        await update.message.reply_text("یه چیزی بنویس 😎")
        return

    reply = ask_ai(msg)
    await update.message.reply_text(reply)


# ===== Bot Run =====
app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("🤖 Bot is running...")
app.run_polling()
