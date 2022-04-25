from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

fullName = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ism kiritish"),
        ],
        [
            KeyboardButton(text='Orqaga'),
        ],
    ],
    resize_keyboard=True #bu tugmalarni auto o'lchamlarini sozlaydi
)
