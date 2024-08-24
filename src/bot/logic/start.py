"""This file represents a start logic."""

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from src.configuration import conf
from src.db.database import Database
from src.language.translator import LocalizedTranslator

from src.bot.utils.stt import Stt
from src.bot.utils.chatgpt import ChatGPT

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: types.Message, db: Database, translator: LocalizedTranslator, state: FSMContext):
    """Start command handler."""
    await state.clear()

    await message.answer("Assalomu aleykum. Menga audio habar yuboring")


@start_router.message(F.voice)
async def audio_handle(message: types.Message):
    file_id = message.voice.file_id
    file = await message.bot.get_file(file_id)

    file_path = conf.VOICE_DIR / f'{file.file_id}.ogg'
    await message.bot.download_file(file.file_path, file_path)

    stt = Stt()
    text = stt.recognize_speech_from_file(str(conf.VOICE_DIR), file.file_id)
    gpt = ChatGPT()
    if text:
        answer = gpt.add_message(text)
        await message.answer(answer)
    else:
        await message.answer("Uzur sizni tushunmadim")
