from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.prof_keyboards import make_row_keyboard #импортируем клавиатуру


router = Router()

availabel_prof_names = ["Квартира", "Дом", "Земельный участок"]
availabel_prof_grades = ["Покупка", "Продажа"]


class ChoiceProfNames(StatesGroup):
    choice_prof_names = State()
    choice_prof_grades = State()


@router.message(Command('сделка'))
async def cmd_prof(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f'Здравствуйте, {name}, выберите вид объекта недвижимости', reply_markup=make_row_keyboard(availabel_prof_names))

    await state.set_state(ChoiceProfNames.choice_prof_names)

@router.message(ChoiceProfNames.choice_prof_names, F.text.in_(availabel_prof_names))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_prof=message.text.lower())
    await message.answer(f'Спасибо, теперь выберите вид сделки который вы хотите осуществить', reply_markup=make_row_keyboard(availabel_prof_grades))

    await state.set_state(ChoiceProfNames.choice_prof_grades)

@router.message(ChoiceProfNames.choice_prof_names)
async def prof_chosen_incorrectly(message: types.Message):
    await message.answer(f'Упс.. Похоже, ввод был некорректен. Попробуйте снова.', reply_markup=make_row_keyboard(availabel_prof_names))



@router.message(ChoiceProfNames.choice_prof_grades, F.text.in_(availabel_prof_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'Ваш вид недвижимости {user_data.get("chosen_prof")}. Вид желаемой сделки {message.text.lower()}.', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'! Приносим извинения. Дальнейший функционал находится в разработке !')

    await state.clear()

@router.message(ChoiceProfNames.choice_prof_grades)
async def grade_chosen_incorrectly(message: types.Message):
    await message.answer(f'Упс.. Похоже, ввод был некорректен. Попробуйте снова.', reply_markup=make_row_keyboard(availabel_prof_grades))

