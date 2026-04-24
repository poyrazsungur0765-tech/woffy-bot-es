import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8648121612:AAGZ6AvDvL7UbRRK7weTcIPU04kIXHkNgyY"

WELCOME_TEXT = (
    "👋 ¡Bienvenido al Bot Oficial de Información de Woff-Y!\n\n"
    "🐾 Este bot ha sido creado para brindar acceso a los canales oficiales de redes sociales de Woff-Y.\n\n"
    "📌 Por favor, presiona el botón START para acceder a nuestros canales oficiales. 👇"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📢 Canal de Telegram", url="https://t.me/woffysol"),
            InlineKeyboardButton("📜 Whitepaper", url="https://woffysol.com/whitepaper"),
        ],
        [
            InlineKeyboardButton("🐦 X (Twitter)", url="https://x.com/woffyofficial"),
        ],
        [
            InlineKeyboardButton("🌐 Sitio Web", url="https://woffysol.com/"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Woffy ES Bot is running...")
    app.run_polling()
