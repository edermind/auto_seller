from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import menu_keyboard
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=menu_keyboard.menu)

# Все что ниже это обработчики кнопок в главном меню(1)
@router.callback_query(F.data == "my_slots")
async def slots_command(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text.slots_test)

@router.callback_query(F.data == "places")
async def slots_command(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text.slots_test)

@router.callback_query(F.data == "info")
async def slots_command(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text.info)

@router.callback_query(F.data == "supports")
async def slots_command(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text.support)
#вот до сюда(1)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=menu_keyboard.menu)