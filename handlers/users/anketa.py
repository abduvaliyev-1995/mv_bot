# import asyncio
# import random
# import logging
# import sqlite3
# from aiogram.dispatcher.filters.builtin import CommandStart, Command
# from aiogram import types
#
# from states.state_steps import state_gr, lang_up, choose_lang
# from keyboards.inline.keyLang import langKey, menu_lang
# from keyboards.default.key_contact import keyContact, keyboard, keyStart, keyCancel, keyAnketa
# from keyboards.inline.keyLang import level_keyboard
#
# from loader import dp, db, bot
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command, Text
# from aiogram.dispatcher import filters
# from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
# from data.config import ADMINS
# from datetime import datetime
# from .start import tm
#
# lang = db.select_user(date_id=tm)
# print(lang)
# @dp.message_handler(text='anketa')
# async def enter_name(message: types.Message, state: FSMContext):
#     await state_gr.fullname.set()
#     fullname = message.text #bu f-yani ichidagi o'zgaruvchi, saqlamasak yo'q bo'lib ketadi
#     await state.update_data(
#         {"fullname": fullname}
#     )
#     if message.text.isalpha():
#         # ----------MB ga fullNameni qo'shamiz:
#         # if message.text not in ['/start', '/help']:
#         try:
#             db.update_user_fullName(date_id=tm, fullName=fullname)
#             await state_gr.next()
#         except sqlite3.IntegrityError as err:
#             await bot.send_message(chat_id=ADMINS[0], text=err, reply_markup=ReplyKeyboardRemove())
#         try:
#             if lang == 'uz':
#                 await message.answer("Telefon raqamingizni ulashish uchun quyidagi tugmani bosing", reply_markup=keyContact)
#             elif lang == 'ru':
#                 await message.answer("Нажмите кнопку ниже, чтобы поделиться своим номером телефона", reply_markup=keyContact)
#         except sqlite3.IntegrityError as err:
#             await bot.send_message(chat_id=ADMINS[0], text=err, reply_markup=ReplyKeyboardRemove())
#         print(message)
#         await state_gr.phone.set() #keyingi holatga o'tkazish uchun
#         # else:
#         #     await message.answer("Ism kiriting")
#     else:
#         if lang == 'uz':
#             # await message.answer("Sonlar kiritmang")
#             await message.answer("Ismingizni kiriting")
#         elif lang == 'ru':
#             # await message.answer("нелзя число ")
#             await message.answer("Введите Ваше имя и фамилию! А не число")
#         # await message.answer("Sonlar kiritnmang")
#
#
# @dp.message_handler(state=state_gr.phone, content_types='contact', is_sender_contact=True)
# async def enter_phone(message: types.Message, state: FSMContext):
#     print(message)
#     phone_num = message.contact.phone_number
#     if message.text not in ['/start', '/help']:
#
#         # DB ga telefonni qo'shish
#         if phone_num:
#             try:
#                 db.update_user_phone_num(date_id=tm, phone_num=phone_num)
#             except sqlite3.IntegrityError as err:
#                 await bot.send_message(chat_id=ADMINS[0],text=err)
#         else:
#             await message.answer("Qaytadan kiriting")
#         if message.contact.phone_number:
#             if lang == 'uz':
#                 await message.answer("Telefon raqamingiz qabul qilindi", reply_markup=ReplyKeyboardRemove())
#             elif lang == 'ru':
#                 await message.answer("Ваш номер телефона был принят", reply_markup=ReplyKeyboardRemove())
#         else:
#             if lang == 'uz':
#                 await message.answer("Siz telefon raqamlarini kiritmadingiz")
#             elif lang == 'ru':
#                 await message.answer("Вы не ввели номер телефона")
#
#         await state.update_data(
#             {"phone_num": phone_num}
#         )
#         if lang == 'uz':
#             await message.answer("Manzilingizni kiritng:")
#         elif lang == 'ru':
#             await message.answer("Введите свой адрес:")
#         await state_gr.next() #keyingi holatga o'tkazish uchun
#     else:
#         await message.answer("Kontaktingizni ulashish uchun quyidagi tugmani bosing")
#
# # @dp.message_handler(Text(contains='/', ignore_case=True), state=state_gr.address)
# @dp.message_handler(state=state_gr.address, content_types='text')
# async def enter_address(message: types.Message, state: FSMContext):
#     address = message.text
#     print(f"messaga for address- {address}")
#     await state.update_data(
#         {"address": address}
#     )
#     if message.text not in ['/start', '/help']:
#         # ----------MB ga addressni qo'shamiz:
#         try:
#             db.update_user_address(date_id=tm, address=address)
#             # await state_gr.next()
#         except sqlite3.IntegrityError as err:
#             await bot.send_message(chat_id=ADMINS[0], text=err, reply_markup=ReplyKeyboardRemove())
#         if lang == 'uz':
#             await message.answer("Murojaatingizni yuboring:")
#         elif lang == 'ru':
#             await message.answer("Отправьте свое обращение:")
#         await state_gr.next() #keyingi holatga o'tkazish uchun
#     else:
#         if lang == 'uz':
#             await message.answer("Manzil kiriting")
#         elif lang == 'ru':
#             await message.answer("Отправьте свое адрес")
#
# # @dp.message_handler(Text(startswith='/', ignore_case=False), state=state_gr.appeal)
# @dp.message_handler(state=state_gr.appeal)
# async def enter_appeal(message: types.Message, state: FSMContext):
#     appeal = message.text
#     await state.update_data(
#         {"appeal": appeal}
#     )
#     # ----------MB ga addressni qo'shamiz:
#     try:
#         db.update_user_appeal(date_id=tm, appeal=appeal)
#     except sqlite3.IntegrityError as err:
#         await bot.send_message(chat_id=ADMINS[0], text=err, reply_markup=ReplyKeyboardRemove())
#     data = await state.get_data()
#
#     fullname = data.get("fullname")
#     phone = data.get("phone_num")
#     address = data.get("address")
#     appeal = data.get("appeal")
#     user_name = db.select_user(date_id=tm)[5]
#
#     if user_name:
#         msg_to_admins = f"""\n<b>Telegram IDsi: </b>{message.from_user.id} \nNomi: {message.from_user.full_name} \nUshbu foydalanuvchidan quyidagilar qabul qilindi:  \
#                   \n\n<b>Ismi</b>: {fullname.title()}  \
#                   \n<b>Foydalanuvchi nomi:</b> @{user_name}\n \
#                   \n\n<b>Telefoni:</b> {phone} \
#                   \n\n<b>Manzili:</b> {address.capitalize()} \
#                   \n\n<b>Murojaat matni:</b> \n{appeal}\n"""
#     else:
#         msg_to_admins = f"""\n<b>Telegram IDsi: </b>{message.from_user.id} \nNomi: {message.from_user.full_name} \nUshbu foydalanuvchidan quyidagilar qabul qilindi:  \
#                   \n\n<b>Ismi</b>: {fullname.title()}  \
#                   \n\n<b>Telefoni:</b> {phone} \
#                   \n\n<b>Manzili:</b> {address.capitalize()} \
#                   \n\n<b>Murojaat matni:</b> \n{appeal}\n"""
#
#     if lang == 'uz':
#         await message.answer(f"""✅ <b>Sizning murojaatingiz ma'muriyatga jo'natildi.</b>\n
#             ✅ Ma'lumotlaringiz to'g'riligiga ishonch hosil qiling. Agar xatolik bo'lsa qaytadan yuboring.\n
#             ♻️ Tez orada ko'rib chiqib ijobiy javob beriladi.
#         """)
#     elif lang == 'ru':
#         await message.answer(f"""✅ <b>Ваш запрос передан администрации.</b>\n
#             ✅ Убедитесь, что ваша информация верна. Если есть ошибка, пожалуйста, отправьте повторно.\n
#             ♻️ В ближайшее время ваша заявка будет рассмотрена и на нее будет дан ответ.
#         """)
#
#     for admin in ADMINS:
#         try:
#             await dp.bot.send_message(admin, msg_to_admins)
#             await dp.bot.forward_message(chat_id=admin, from_chat_id=message.from_user.id, message_id=message.message_id)
#         except Exception as err:
#             logging.exception(err)
#     await state.finish()
#     # await state.reset_state(with_data=False) # Ma'lumotlar o'chib ketmaydi
#
#
#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
#
#
# from keyboards.inline.support import support_keyboard, support_callback
# from loader import dp, bot
#
# # from aiogram.utils.callback_data import CallbackData, CallbackQuery
#
# @dp.message_handler(Command("support"))
# async def ask_support(message: types.Message):
#     text = "Murojaat qilishni xohlaysizmi?\n Quyidagi tugmani bosing!"
#     keyboard = await support_keyboard(messages="one")
#     await message.answer(text, reply_markup=keyboard)
#
# @dp.callback_query_handler(support_callback.filter(messages="one"))
# async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
#     await call.answer()
#     user_id = int(callback_data.get("user_id"))
#
#     await call.message.answer("Xabaringizni yozib qoldirishingiz mumkin.")
#     await state.set_state("wait_for_support_message")
#     await state.update_data(second_id=user_id)
#
# @dp.message_handler(state="wait_for_support_message", content_types=types.ContentTypes.ANY)
# async def get_support_message(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     second_id = data.get("second_id")
#
#     await bot.send_message(second_id,
#                            f"Sizga xabar! Quyidagi tugmani bosib javob berishingiz mumkin!")
#     keyboard = await support_keyboard(messages="one",user_id=message.from_user.id)
#     await message.copy_to(second_id, reply_markup=keyboard)
#
#     # await message.answer("Siz shu xabarni yubordingiz")
#     await state.reset_state()
