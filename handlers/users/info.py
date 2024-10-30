from loader import dp,bot
from aiogram import types
from aiogram.utils.markdown import hbold,hitalic
from pathlib import Path
import requests



download_path=Path().joinpath("downloads","categories")
download_path.mkdir(parents=True,exist_ok=True)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def send_video(message: types.Message):
    await message.video.download(destination=download_path)
    await message.reply("botga video yuborish mumkin emas?")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo(message: types.Message):
    await message.photo[-1].download(destination=download_path)
    await message.reply("botga rasm yuborish mumkin emas?")

