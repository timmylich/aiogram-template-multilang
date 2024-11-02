from config import TOKEN
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


from aiogram_translation import Translator

from locales import *


translator = Translator(default_language_key="en")

translator.include([
    English(),
    Russian()
])
translator.set_default(key='en')