import re
import requests
from django.conf import settings
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)


async def main_command(update: Update):
    keyboard = [
        [
            InlineKeyboardButton(
                "Register new alert",
                callback_data="(#command#)1",
            ),
        ],
        [
            InlineKeyboardButton(
                "List my alerts",
                callback_data="(#command#)2",
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Choose a option",
        reply_markup=reply_markup,
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome!",
    )
    # user_id = update.message.from_user.id
    response = requests.get("http://localhost:8000/api/user-count/")
    if response.status_code == 200:
        await update.message.reply_text(
            f"Total users right now: {response.content.decode()}",
        )
    # await main_command(update)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    if re.match(r"^[A-Z0-9]{8}$", text):
        await update.message.reply_text(
            "Aguarde...",
        )
        response = requests.get(
            "http://localhost:8000/account/verify-code/",
            params={
                "code": text,
                "user_id": update.message.from_user.id,
            },
        )
        if response.status_code == 200:
            update_session(update.message.from_user.id)
            await update.message.reply_text("Código validado com sucesso ✅")
            await main_command(update)
        else:
            await update.message.reply_text("Código inválido, tente novamente.")


async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query.data == "🔎 Buscar pessoa":
        keyboard = [
            [
                InlineKeyboardButton(
                    "Foto de rosto",
                    callback_data="Foto de rosto",
                ),
            ],
            [
                InlineKeyboardButton(
                    "Qualificação",
                    callback_data="Qualificação",
                )
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.answer()
        await query.edit_message_text(text=f"{query.data}", reply_markup=reply_markup)

    elif query.data == "📝 Cadastrar pessoa":
        pass
    else:
        await query.edit_message_text(text="Opção inválida.")
        await main_command(update)


async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error: {context.error}")


def start_bot():
    print("[Telegram bot] Starting...")
    app = Application.builder().token(settings.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(handle_error)
    app.run_polling(poll_interval=3)
