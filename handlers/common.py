from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import kb1, kb3 #импортируем клавиатуру
from utils.random_fox import fox

router = Router()

# Хэндлер на команду /start
#@dp.message(Command('start'))
#async def cmd_start(message: types.Message):
#    name = message.chat.first_name
#    await message.answer(f'Привет, {name}', reply_markup=kb1) #При нажатии /start появляется клавитаура

# Хэндлер на команду /fox
#@dp.message(Command('fox')) #КОМАНДА /декоратор (ввод в строке "/fox"
#@dp.message(Command('лиса')) #ФИЛЬТР ТЕКСТА /вариативность вводимых команд
#@dp.message(F.text.lower() == 'покажи лису')
#async def cmd_fox(message: types.Message):
#    name = message.chat.first_name
#    img_fox = fox()
#    await message.answer(f'Держи лису, {name}')
#    await message.answer_photo(photo=img_fox)
#    #await bot.send_photo(message.from_user.id, photo=img_fox)

#Хендлер на сообщения
#@dp.message(F.text)
#async def msg_echo(message: types.Message): #Эхо
#    msg_user = message.text.lower() #Присвоили переменну вводимому тексту
#    name = message.chat.first_name #Переменной ИМЯ присаиваем имя пользователя(подтягивается автоматически)
#    if 'привет' in msg_user: #Оператор вхождения: если слово содержится в водимом пользователем сообщении то..
#        await message.answer(f'Привет-привет, {name}') #Ответ
#    elif 'пока' == msg_user: #Оператор вхождения: строго только слово(==)
#        await message.answer(f'Пока-пока, {name}')
#    elif 'лиса' in msg_user:
#        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2) #на сообщение "лиса" появляется клавиатура
#    else: #Иначе
#        await message.answer(f'Я не знаю такого слова')


# Хэндлер на команду /start
@router.message(Command('start'))
@router.message(F.text.lower() == 'старт')
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Здравствуйте, {name}', reply_markup=kb1) #При нажатии /start появляется клавитаура

# Хэндлер на команду /law
@router.message(Command('law'))
@router.message(F.text.lower() == 'закон')
async def cmd_law(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'{name}, это нормативная база', reply_markup=kb3)
    await message.answer(f'Конституция РФ https://www.consultant.ru/document/cons_doc_LAW_28399/ ')
    await message.answer(f'Земельный кодекс РФ https://www.consultant.ru/document/cons_doc_LAW_33773/')


# Хэндлер на команду /info
@router.message(Command('info'))
async def cmd_info(message: types.Message):
    await message.answer(f' Fyfcnfcbz_bot - это Бот, который создан для оказания помощи в вопросах недвижимости.', reply_markup=kb3)

# Хэндлер на команду /stop
@router.message(Command('stop'))
@router.message(F.text.lower() == 'стоп')
@router.message(F.text.lower() == 'пока')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'До встречи, {name}')

# Хэндлер на команду /exit
@router.message(F.text.lower() == 'закрыть')
async def cmd_exit(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'{name}', reply_markup=kb1)


#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message): #Эхо
    msg_user = message.text.lower() #Присвоили переменну вводимому тексту
    name = message.chat.first_name #Переменной ИМЯ присаиваем имя пользователя(подтягивается автоматически)
    if 'привет' in msg_user: #Оператор вхождения: если слово содержится в водимом пользователем сообщении то..
        await message.answer(f'Здравтсуйте, {name}', reply_markup=kb1) #Ответ
    else: #Иначе
        await message.answer(f'Чтобы запустить бота нажми "/start"')


