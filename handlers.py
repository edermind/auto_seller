from aiogram import types, F, Router
from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.filters import Command,StateFilter
from aiogram.fsm.context import FSMContext


import slots_keyboard
import menu_keyboard
import places_keyboard
import text
import states

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=menu_keyboard.menu)

@router.callback_query(F.data == "menu")
async def menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("📍 Главное меню", reply_markup= menu_keyboard.menu)

'''
# Все что ниже это обработчики кнопок в главном меню(1)
'''
# обработчик кнопки"Мои слоты" в гл.меню 
@router.callback_query(F.data == "my_slots")
async def my_slots_handler(callback_query: types.CallbackQuery, state:FSMContext):
    await callback_query.answer()
    await callback_query.message.answer("Мои слоты", reply_markup=slots_keyboard.sl)
    await state.set_state(states.slots_class.slots_menu)
    current_state = await state.get_state()
    await callback_query.message.answer(f"Бот находится в состоянии: {current_state}")
    await callback_query.message.answer(reply_markup=ReplyKeyboardRemove())

#обработчик кнопки"Площадки" в гл.меню 
@router.callback_query(F.data == "places")
async def places_handler(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Площадки: ", reply_markup=places_keyboard.places_kb)

#обработчик кнопки"Информаця" в гл.меню 
@router.callback_query(F.data == "info")
async def info_handler(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text.info)

#обработчик кнопки"Техподдержка" в гл.меню 
@router.callback_query(F.data == "supports")
async def supports_handler(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text.support)

#обработчик кнопки"Уведомления" в гл.меню 
@router.callback_query(F.data == "notifications")
async def noti_handler(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text.slots_test)
    
#вот до сюда(1)




@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=menu_keyboard.menu)