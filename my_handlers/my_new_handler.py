from aiogram import types, F, Router
from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.filters import Command,StateFilter
from aiogram.fsm.context import FSMContext

from drom_parser import parse_drom


import slots_keyboard
import menu_keyboard
import places_keyboard
import text
import states

from .router import my_router

@my_router.message(Command("temp"))
async def temp_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=menu_keyboard.menu)
