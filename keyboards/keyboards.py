#Клавиатура

from aiogram import types

#Кнопки
button2 = types.KeyboardButton(text='/law')
button3 = types.KeyboardButton(text='/info')
button4 = types.KeyboardButton(text='/сделка')
button5 = types.KeyboardButton(text='Закрыть')
button7 = types.KeyboardButton(text='/stop')

#Клавиатура(список)
keyboard1 = [
    [button2, button3],
    [button4, button7],
]

keyboard3 = [
    [button5],
]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True) #resize_keyboard=True - уменьшает размер клавиатуры
kb3 = types.ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)