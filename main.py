from telegram.ext import Application
from telegram import Update

from handlers import setup_dispatcher
from settings import TELEGRAM_TOKEN

application = Application.builder().token(TELEGRAM_TOKEN).build()
setup_dispatcher(application)
application.run_polling(allowed_updates=Update.ALL_TYPES)

