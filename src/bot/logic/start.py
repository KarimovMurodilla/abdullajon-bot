"""This file represents a start logic."""

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile

from src.configuration import conf
from src.db.database import Database
from src.language.translator import LocalizedTranslator

from src.bot.utils.stt import Stt
from src.bot.utils.tts import Tts
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
    file_tts_result_path = conf.VOICE_DIR / f'{message.from_user.id}.ogg'

    await message.bot.download_file(file.file_path, file_path)

    stt = Stt()
    tts = Tts()

    text = stt.recognize_speech_from_file(str(conf.VOICE_DIR), file.file_id)
    gpt = ChatGPT()

    if text:
        answer = gpt.add_message(text)
        audio_result_path = tts.text_to_speech(text=answer, file_path=file_tts_result_path)

        await message.answer(answer)
        voice = FSInputFile(audio_result_path)
        await message.answer_voice(voice=voice)
    else:
        await message.answer("Uzur sizni tushunmadim")
