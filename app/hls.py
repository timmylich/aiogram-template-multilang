from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from locales import *
from app.states import BaseStates

router = Router()

@router.message()
async def echoTest(message: Message, language: BaseTranslation, state: FSMContext):
    await message.answer(text=language.test_string)
    await state.set_state(BaseStates.test)