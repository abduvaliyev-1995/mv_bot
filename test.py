# import asyncio
# import random
# import logging
# import sqlite3
# from aiogram.dispatcher.filters.builtin import CommandStart, Command
# from aiogram import types
#
# from states.state_steps import state_gr, lang_up, choose_lang
# from keyboards.inline.keyLang import langKey, menu_lang
# from keyboards.default.key_contact import keyContact, keyboard, keyStart, keyCancel
# from keyboards.inline.keyLang import level_keyboard
#
# from loader import dp, db, bot
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command, Text
# from aiogram.dispatcher import filters
# from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
# from data.config import ADMINS
# from datetime import datetime
#
# # global time_id, tm
# time_id = int(datetime.now().strftime('%y%m%H%M%S%f'))
# tm = int(message.date.now().strftime('%y%m%H%M%S%f'))
# print(f"1-{time_id}")
# print(f"2-{tm}")
#
# @dp.message_handler(CommandStart(), state=None)
# async def bot_start(message: types.Message):
#    await message.answer(f"Assalomu alaykum!, {message.from_user.full_name} \n Boshlash uchun Start tugmasini bosing\n", reply_markup=keyStart)
#
# @dp.message_handler(text='Start')
# async def sel_lang(message: types.Message):
#     # global time_id, tm
#     # time_id = int(datetime.now().strftime('%y%m%H%M%S%f'))
#     # tm = int(message.date.now().strftime('%y%m%H%M%S%f'))
#     # print(f"1-{time_id}")
#     # print(f"2-{tm}")
#
#     if message.from_user.username:
#         try:
#             db.update_user_username(date_id=tm, username=message.from_user.username)
#         except sqlite3.IntegrityError as err:
#             await bot.send_message(chat_id=ADMINS[0], text=err)
#     else:
#         try:
#             db.update_user_username(date_id=tm, username=None)
#         except sqlite3.IntegrityError as err:
#             await bot.send_message(chat_id=ADMINS[0], text=err)
#     await message.answer(f"\nTilni tanlang | Выберите язык \n", reply_markup=langKey)
#     print(message)
#     await state_gr.get_lang.set()
#
# @dp.callback_query_handler(state=state_gr.get_lang)
# async def get(call: CallbackQuery):
#
#     print(call)
#     global lang
#     lang = call.data
#     if call.data == 'uz':
#         await call.message.answer(f"""
#                                 \nSavol, taklif, murojaatlaringiz bo‘lsa, marhamat bizga yuboring, sizga tez orada javob beriladi.
#                              \n\n❗ Iltimos murojaatingizni quyidagi tartibda yuboring:\n
#                                 \n1. ✅ To'liq ismingiz
#                                 \n2. ☎️ Kontakt ma'lumotlaringiz
#                                 \n3. 📍 Manzilingiz
#                                 \n4. ❓ Murojaatning mazmuni
#                                 \n⚠ Sizning murojaatingiz bo'yicha javobni yuborishimiz uchun ma'lumotlarni to'g'ri to'ldirganingizga ishonch hosil qiling.
#                              """, reply_markup=ReplyKeyboardRemove())
#     elif call.data == 'ru':
#         await call.message.answer(f"""
#                                 \nЕсли у вас есть какие-либо вопросы, предложения, пожелания, пожалуйста, присылайте их нам, вы получите ответ в ближайшее время.
#                              \n\n❗ Пожалуйста, присылайте заявки в следующем порядке:\n
#                                 \n1. ✅ Ваше полное имя
#                                 \n2. ☎️ Ваши контактные данные
#                                 \n3. 📍 Ваш адрес
#                                 \n4. ❓ Содержание обращения
#                                 \n⚠ Убедитесь, что вы правильно заполнили информацию, чтобы мы могли ответить на ваш запрос.
#         """, reply_markup=ReplyKeyboardRemove())
#
#     if lang == 'uz':
#         await call.message.answer("To'liq ismingizni kiriting:")
#     elif lang == 'ru':
#         await call.message.answer("Введите Ваше имя и фамилию:")
#     try:
#         db.add_user(date_id=tm, tg_id=call.from_user.id, name=call.from_user.full_name, language=lang)
#         await call.message.delete()
#         await call.answer(cache_time=2)
#     except sqlite3.IntegrityError:
#         await bot.send_message(chat_id=ADMINS[0], text=err, reply_markup=ReplyKeyboardRemove())
#     # -----------------Ism kiritish
#     await state_gr.fullname.set()
# # _____________________________________________________________
#
# @dp.message_handler(state=state_gr.fullname)
# async def enter_name(message: types.Message, state: FSMContext):
#     # tm = db.select_user(id=id, tg_id=message.from_user.id)
#     fullname = message.text #bu f-yani ichidagi o'zgaruvchi, saqlamasak yo'q bo'lib ketadi
#     print(fullname)
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

fullname = 'kdjlskdjlkkldsvSDFSDSSDFSLD;KF;LSDKFLSKD;LSKD;LSKD655151'
character_allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'ҳ','қ','ғ','ў', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
symb2 = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','1','2','3','4','5','6','7','8','9','0',]
for letter in fullname.lower():
    # if not (letter.isalpha() or letter.isdigit() or letter in character_allowed):
    if letter in symb2:
        print(letter)

        break
    #     letter.isdigit()




# def Convert(string):
#     li = list(string.split(" "))
#     return li
#
#     # Driver code
# str1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# list2 = list(str1)
# print(Convert(str1))
# print(list2)
# symb = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
# print(symb)
# symb2 = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','1','2','3','4','5','6','7','8','9','0',]