from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 እንኳን ወደ Tiwilid AI Bot በደህና መጡ!\n\n📖 የመጽሐፍ ቅዱስ ጥያቄዎችን ይጠይቁ።"
    )

app = Application.builder().token("TOKEN_HERE").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
