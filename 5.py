import telebot
a = telebot.TeleBot("Token")

user_data = {}

@a.message_handler(commands=['start'])
def startWork(message):
    user_data[message.chat.id] = {}
    keyboard_test = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_close = telebot.types.KeyboardButton("Закрыть")
    keyboard_test.add(keyboard_close)
    a.send_message(message.chat.id, "Привет. Чтобы закрыть клавиатуру, тебе нужно закрыть кнопку", reply_markup=keyboard_test)

@a.message_handler(content_types=['text'])
def sendYourMessage(message):
  if message.text == "Закрыть":
        a.send_message(message.chat.id, "Клавиатура закрыта.", reply_markup=telebot.types.ReplyKeyboardRemove())

a.polling()

