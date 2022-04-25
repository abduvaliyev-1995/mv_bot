from aiogram.dispatcher.filters.state import StatesGroup, State


class choose_lang(StatesGroup):
    get_lang = State()


class state_gr(StatesGroup):
    get_lang = State()
    fullname = State()
    phone = State()
    address = State()
    appeal = State()

class lang_up(StatesGroup):
    up_lang = State()
