from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import keyboard
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=keyboard.menu)


# @router.message(Command("my_slots"))
# async def slots_command(msg: types.Message):
#     await msg.answer('123')

@router.callback_query(F.data == "my_slots")
async def slots_command(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text.slots_test)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=keyboard.menu)