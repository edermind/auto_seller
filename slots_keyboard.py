
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

#кнопки раздела слоты 
slots_keyboard = [
    [InlineKeyboardButton(text= "Слот № 1 - 🏎 BMW e46", callback_data="slot_num_1"),
     InlineKeyboardButton(text= "➕ Добавить слот", callback_data= "new_slot")],
     [InlineKeyboardButton(text= "📍 Главное Меню", callback_data= "menu")]
]

sl = InlineKeyboardMarkup(inline_keyboard=slots_keyboard)
