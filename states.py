from aiogram import Dispatcher, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext



class slots_class(StatesGroup):
    slots_menu = State()
    making_slots = State()
    waiting_for_link = State()
    