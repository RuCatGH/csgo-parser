# Импортировать Text
import logging
from settings import Token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink, hbold
import json
import time
from main import get_data
API_TOKEN = Token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    start_buttons = ['Ножи', 'Перчатки', 'Снайперки']
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keybord.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup=keybord)

@dp.message_handler(Text(equals=['Ножи']))
async def knife(message: types.Message):
    get_data(2)

    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for index, i in enumerate(data):
        card = f'{hlink(i.get("name"),i.get("link"))}\n' \
                f'{hbold("Цена:")} {i.get("price")}\n' \
                f'{hbold("Скидка")} {i.get("overprice")}\n' 
       
        if index%20 ==0:
            time.sleep(4)
        await message.answer(card)

@dp.message_handler(Text(equals=['Перчатки']))
async def gloves(message: types.Message):
    get_data(13)

    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for index, i in enumerate(data):
        card = f'{hlink(i.get("name"),i.get("link"))}\n' \
                f'{hbold("Цена:")} {i.get("price")}\n' \
                f'{hbold("Скидка")} {i.get("overprice")}\n' 
       
        if index%20 ==0:
            time.sleep(4)
        await message.answer(card)

    
@dp.message_handler(Text(equals=['Снайперки']))
async def rifle(message: types.Message):
    get_data(4)

    with open('result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for index, i in enumerate(data):
        card = f'{hlink(i.get("name"),i.get("link"))}\n' \
                f'{hbold("Цена:")} {i.get("price")}\n' \
                f'{hbold("Скидка")} {i.get("overprice")}\n' 
       
        if index%20 ==0:
            time.sleep(4)
        await message.answer(card)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)