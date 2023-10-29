import telebot
from telebot import types
from search import Search


with open('token.txt', 'r') as TOKEN:
    bot = telebot.TeleBot(token=TOKEN.read())
srch = Search()
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    remove_keyboard = telebot.types.ReplyKeyboardRemove()
    srch.way_search = message.chat.id
    srch.tag = 'инженер'
    bot.send_message(message.chat.id, "Привет, я бот, который поможет тебе найти нужный документ.\n Чтобы начать введите команду /find",reply_markup=remove_keyboard)

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

# def create_inline_keyboard(options):
#     options = ['Информационные технологии. ', 'Ведение электронной документации']
#     keyboard = telebot.types.InlineKeyboardMarkup()
#     for option in options:
#         callback_data = f"option_{option}"
#         button = telebot.types.InlineKeyboardButton(text=option, callback_data=callback_data)
#         keyboard.add(button)
#     return keyboard

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    srch.search(message.text, srch.tag)
    buttons = srch.answer.split('\n\n')
    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    if srch.answer:
        for but in buttons:
            keyboard.add(but)
        bot.send_message(message.chat.id, f'{srch.answer}', reply_markup=keyboard) #!!!!!! на данном этапе во время демонстрации работы бота, он ничего не
                                                                                   #выведил, потому что у пользователя-инженера не было доступа к запрашиваемому
                                                                                   #документу, и тг бот ругался, потому что не мог вывести пустую строку. 
                                                                                   #Но я добавил проверку условием и теперь все в порядке ↓↓↓
    else:
        bot.send_message(message.chat.id, 'Подходящего вашему запросу документа не найдено, или у вас нет доступа.\nВведите /find чтоб еще раз произвести поиск')


def send_file(name):
    with open(fr"D:\Ярлыки\IT\Project\hackaton\files\{name}.pdf","rb") as f:
        ret = f.read()
    return ret

"""
Данная функция к сожалению работает некорректно (не работает)
"""
@bot.message_handler(func=lambda message: message.text in srch.answer.split('\n\n'))
def handle_button_click(message):
    remove_keyboard = telebot.types.ReplyKeyboardRemove()
    print(send_file(message.text))
    # bot.send_document(message.chat.id, send_file(message.text), reply_markup=remove_keyboard)
    bot.send_message(message.chat.id, f"Введите запрос на основе выбранной категории: ", reply_markup=remove_keyboard)
    

bot.polling()

