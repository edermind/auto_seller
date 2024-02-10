
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

places_keyboard = [
        [InlineKeyboardButton(text= "drom",callback_data= "drom"),
        InlineKeyboardButton(text= "auto.ru", callback_data= "autoru")],
        [InlineKeyboardButton(text= "avito", callback_data= "avito")],
        [InlineKeyboardButton(text= "📍 Главное меню", callback_data= "menu")]
    ]

places_kb = InlineKeyboardMarkup(inline_keyboard=places_keyboard)