import logging
from main import analyzer
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

API_TOKEN = open('token.txt').read()


bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# States
class Form(StatesGroup):
    text_1 = State()  
    text_2 = State()  


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    # Set state
    await message.reply("Hi there! I am a bot that can check how similar two text are, just send them to me ;) \n to start send me /check command")

@dp.message_handler(commands='check')
async def cmd_start(message: types.Message):
    # Set state
    await Form.text_1.set()

    await message.reply("Send me first text:")


@dp.message_handler(state=Form.text_1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text_1'] = message.text

    await Form.text_2.set()
    await message.reply("Okay, now send me second text: ")


@dp.message_handler(state=Form.text_2)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text_2'] = message.text
        output = analyzer(data['text_2'].lower(), data['text_1'].lower())
        s_out = f"📟Similarity = {round(output[0], 2)}\n\n"
        s_out += '🔝Important words:\n'
        for word in output[1]:
            s_out += "      " +  word + " - " + str(abs(round(output[1][word], 2))) + '\n'
        
        await message.reply(s_out)
    await state.finish()
    



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)