from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from api.core.google_sheets import service, SPREADSHEET_ID
from telegram_bot.settings import dp
from aiogram import types
from telegram_bot.states.test import Test

info = service.get(
        spreadsheetId=SPREADSHEET_ID,
        range='B2:B100',
        majorDimension='COLUMNS'
    ).execute()


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer(info['values'][0][0])
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer=answer)
    await message.answer(info['values'][0][1])
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer")
    answer2 = message.text

    await message.answer("Спасибо за ваши ответы.")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

    await state.finish()
