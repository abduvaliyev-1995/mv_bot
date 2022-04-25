import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


# Turli tugmalar uchun CallbackData-obyektlarni yaratib olamiz
langKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="O'zbek tili", callback_data='uz'),
        InlineKeyboardButton(text="Русский язык", callback_data='ru'),
         ],
    ],

)

async def level_keyboard():
    # Eng yuqori 0-qavat ekanini ko'rsatamiz
    CURRENT_LEVEL = 1
    # Keyboard yaratamiz
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text="Orqaga", callback_data='back'))

    # Keyboardni qaytaramiz
    return markup

menu_lang = CallbackData("O'zbek tili", "Русский язык")



