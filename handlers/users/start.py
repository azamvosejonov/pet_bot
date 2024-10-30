from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import requests
from loader import dp


@dp.message_handler(CommandStart())
async def pet(message: types.Message):
    restar = requests.get('https://random.dog/woof.json')
    await message.answer_photo(restar.json()['url'])
