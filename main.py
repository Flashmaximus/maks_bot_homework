from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1_2 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_1_2')
    markup.add(button_call_1_2)
    question = 'Речка спятила с ума - по домам пошла она?'
    answer = ['Рыба','Водопровод','Тишина']
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=50,
        explanation='Легкая загадка',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda func: func.data=='button_call_1_2')
async def quize2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2_3 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_2_3')
    markup.add(button_call_2_3)
    question ='На расскрашенных страницах много праздников хранится?'
    answer = ['Газета', 'Журнал', 'Календарь']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=50,
        explanation='Висит на стене',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'button_call_2_3')
async def quiz3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3_4 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_3_4')
    markup.add(button_call_3_4)
    question = 'Ах не трогайте меня обожгу и без огня'
    answer = ['Солнце', 'Крапива', 'Кипяток',]
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Растение',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'button_call_3_4')
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4_5 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_4_5')
    markup.add(button_call_4_5)
    question = 'Продолжи фразу "Расскажи снегурочка где  ........" '
    answer = ['Спала', 'Была', 'Кушала', 'Ночевала']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Из ну погоди',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'button_call_4_5')
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5_6 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_5_6')
    markup.add(button_call_5_6)
    question = 'На воде увидел ты нежно белые цветы, эти жители реки на ночь прячут лепестки" '
    answer = ['Ромашка', 'Роза', 'Одуванчик', 'Лилии']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Растет в прудах и реках',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'button_call_5_6')
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_6_7 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_6_7')
    markup.add(button_call_6_7)
    question = 'Вот иголки и булавки выползают из под лавки, на меня они глядят, молока они хотят" '
    answer = ['Магнит', 'Еж', 'Кактус']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Колючий колобок',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'button_call_6_7')
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_7_8 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_7_8')
    markup.add(button_call_7_8)
    question = 'Маленькие домики по улице бегут,мальчиков и девочек домики везут." '
    answer = ['Машины', 'Улитки', 'Кенгуру']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Кушают бензин',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'button_call_7_8')
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_8_9 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_8_9')
    markup.add(button_call_8_9)
    question = 'Пустые отдыхаем, полные шагаем?" '
    answer = ['Часы', 'Карманы', 'Сапоги']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Их носит солдат',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'button_call_8_9')
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_9_10 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_9_10')
    markup.add(button_call_9_10)
    question = 'Над нами кверху ногами?" '
    answer = ['Тучи', 'Луна', 'Таракан']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Из одноименной сказки',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'button_call_9_10')
async def quiz4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_10_11 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_10_11')
    markup.add(button_call_10_11)
    question = 'Деревянный брусок а на нем растет лесок?" '
    answer = ['Картина', 'Щетка']
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Обувь чистит',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

#@dp.message_handler(commands=['start'])
#async def hello(message: types.Message):
#    await bot.send_message(message.chat.id, f'Приветствую  {message.from_user.full_name}')

#@dp.message_handler()
#async def echo_message(message:types.Message):
    #await message.answer(message.text.lower())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
