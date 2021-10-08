from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = "2042268190:AAHd8a9za_tJpZfhagjDunwW40Pm5sjyV70"
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
