
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

#кнопки главного меню
menu = [
    [InlineKeyboardButton(text="🚗  Мои слоты", callback_data="my_slots"),
    InlineKeyboardButton(text="🏢 Площадки", callback_data="places")],
    [InlineKeyboardButton(text="☎️ Уведомления", callback_data="notifications")],
    [InlineKeyboardButton(text="💡 Инфо", callback_data="info"),
    InlineKeyboardButton(text="🛟 Техподдержка", callback_data="supports")],
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
