
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

places_keyboard = [
    [InlineKeyboardButton(text="Дром", callback_data="drom"),
     InlineKeyboardButton(text="Авто.ру", callback_data="autoru")],
    [InlineKeyboardButton(text="Авито", callback_data="avito")],
    [InlineKeyboardButton(text="📍 Главное меню", callback_data="menu")]
]

places_kb = InlineKeyboardMarkup(inline_keyboard=places_keyboard)