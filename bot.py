import telebot
from telebot import types
from search import Search


with open('token.txt', 'r') as TOKEN:
    bot = telebot.TeleBot(token=TOKEN.read())
srch = Search()
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    srch.way_search = message.chat.id
    # srch.get_user(message.chat.id)
    print(message.chat.id)
    bot.send_message(message.chat.id, "Привет, я бот, который поможет тебе найти нужный документ.\n Чтобы начать введите команду /find")

@bot.message_handler(commands=['find'])
def find(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = telebot.types.KeyboardButton("ключевое слово")
    button2 = telebot.types.KeyboardButton("тип")
    button3 = telebot.types.KeyboardButton("название")
    button4 = telebot.types.KeyboardButton("дата выхода")
    button5 = telebot.types.KeyboardButton("номер")
    button6 = telebot.types.KeyboardButton("дата ввода в действие")
    
   
    keyboard.row(button1, button2)
    keyboard.row(button3, button4)
    keyboard.row(button5, button6)

    bot.send_message(message.chat.id, "Выберите одну из кнопок:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in ["ключевое слово", "тип", "название", "дата выхода", "номер", "дата ввода в действие"])
def handle_button_click(message):
    if message.text == 'ключевое слово':
        srch.way_search = "keyword"
    elif message.text == 'номер':
        srch.way_search = "number"
    elif message.text == 'дата ввода в действие':
        srch.way_search = "date_enter"
    elif message.text == 'дата выхода':
        srch.way_search = "date_exit"  
    elif message.text == 'название':
        srch.way_search = "name"  
    else:
        srch.way_search = "type"  
    remove_keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, f"Введите запрос на основе выбранной категории: ", reply_markup=remove_keyboard)

def create_inline_keyboard(options):
    options = ['Информационные технологии. ', 'Ведение электронной документации']
    keyboard = telebot.types.InlineKeyboardMarkup()
    for option in options:
        callback_data = f"option_{option}"
        button = telebot.types.InlineKeyboardButton(text=option, callback_data=callback_data)
        keyboard.add(button)
    return keyboard

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    srch.search(message.text, srch.tag)
    # if srch.answer:
    #     keyboard = create_inline_keyboard(srch.answer)
    #     bot.send_message(message.chat.id, "Вот документы найденные по вашему запросу.\nДля просмотра дополнительной информации нажмите на кнопку:", reply_markup=keyboard)
    # else:
    #     bot.send_message(message.chat.id, "По вашему запросу ничего не найдено")
    bot.send_message(message.chat.id, f'{srch.answer}')

"""
Данная функция к сожалению не успела доработаться 
"""
@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data.startswith('option_'):
        option = call.data[len('option_'):]
        new_options = ["Новый вариант 1", "Новый вариант 2", "Новый вариант 3"]
        new_keyboard = create_inline_keyboard(new_options)
        
        # Изменяем текст сообщения
        bot.edit_message_text(f"Вы выбрали: {option}", call.message.chat.id, call.message.message_id)
        
        # Изменяем инлайн клавиатуру в сообщении
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=new_keyboard)

"""
Эта функция тоже в разработке
"""
@bot.message_handler(func=lambda message: True)
def send_file(message):
    pass
bot.polling()
