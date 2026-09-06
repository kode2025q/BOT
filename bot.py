import os
import threading

from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.environ["BOT_TOKEN"]

# HTTP-сервер для Render
web = Flask(__name__)


@web.route("/")
def home():
    return "Bot is running!"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет!")


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))


print("Бот запущено!")

# Запускаємо HTTP-сервер окремо
threading.Thread(target=run_web, daemon=True).start()

# Запускаємо Telegram polling
app.run_polling()
