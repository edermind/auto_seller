
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from button_refreser import create_name_button
#кнопки раздела слоты

async def create_name_button(link):
    abx = link.split('/')
    name = abx[-3] + ' ' + abx[-2]
    return name 


try:
    async def set_button_name():
        AAA = create_name_button()
        return AAA  
except:
    AAA = 'пустая кнопка'

try:
    slots_keyboard = [
        [InlineKeyboardButton(text= f"{AAA}", callback_data="slot_num_1"),
        InlineKeyboardButton(text= "➕ Добавить слот", callback_data= "new_slot")],
        [InlineKeyboardButton(text= "📍 Главное Меню", callback_data= "menu")]
    ]


except:
    slots_keyboard = [
        [InlineKeyboardButton(text= "___", callback_data="slot_num_1"),
        InlineKeyboardButton(text= "➕ Добавить слот", callback_data= "new_slot")],
        [InlineKeyboardButton(text= "📍 Главное Меню", callback_data= "menu")]
    ]

sl = InlineKeyboardMarkup(inline_keyboard=slots_keyboard)
