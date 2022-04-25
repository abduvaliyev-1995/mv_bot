from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Start'),
        ],
    ],
    resize_keyboard=True #bu tugmalarni auto o'lchamlarini sozlaydi
)
keyCancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Bekor qilish'),
        ],
    ],
    resize_keyboard=True #bu tugmalarni auto o'lchamlarini sozlaydi
)

keyContact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📞', callback_data="contact", request_contact=True),
        ],
    ],
    resize_keyboard=True #bu tugmalarni auto o'lchamlarini sozlaydi
)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="O'zbek tili", callback_data='uz')
                                   ],
                                   [
                                       KeyboardButton(text="Русский язык", callback_data='ru')
                                   ],
                               ])


