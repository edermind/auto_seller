from aiogram import types, F, Router
from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.filters import Command,StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Dispatcher, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


import slots_keyboard
import menu_keyboard
import places_keyboard
import text
import states

router = Router()

@router.callback_query(F.data == "new_slot")
async def new_slot_handler(callback_query: types.CallbackQuery, state:FSMContext):
    await callback_query.answer()
    await callback_query.message.answer('Вставьте ссылку: ')
    await state.set_state(states.slots_class.waiting_for_link)

@router.message()
async def memoriz_link(message: types.Message, ):
    link = message.text
    await message.answer.text(f"Ссылка \"{link}\" сохранена")








