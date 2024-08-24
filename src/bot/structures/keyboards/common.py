from aiogram import types


def show_keyboard():
    kb = [
        [types.KeyboardButton(text="Button 1")],
        [types.KeyboardButton(text="Button 2")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard
