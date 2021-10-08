from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from telegram_bot.settings import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        "\n".join([
            f'Добро пожаловать в бот расписаний, <b>{message.from_user.full_name}</b>!',
            '<b>Бот знает такие команды:</b>\n'
            'Пройти тест: /test\n'
        ]),)
