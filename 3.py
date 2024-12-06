import telebot
a = telebot.TeleBot("7776098211:AAFz-Rx005HbBk5L4Kk8rnWIyKW-k6JocSU")

user_data = {}

@a.message_handler(commands=['start'])
def startWork(message):
   user_data[message.chat.id] = {}
   a.send_message(message.chat.id, "Привет. Давай начнем!\nКак тебя зовут?")

@a.message_handler(content_types=['text'])
def sendYourMessage(message):
  if 'name' not in user_data[message.chat.id]:
    user_data[message.chat.id]['name'] = message.text
    a.send_message(message.chat.id, "Тебя зовут {0}\nCколько тебе лет?".format(message.text))
  elif 'age' not in user_data[message.chat.id]:
      user_data[message.chat.id]['age'] = message.text
      a.send_message(message.chat.id, "Тебе уже {0} лет\nКакой у тебя рост в см?".format(message.text))
  elif 'rost' not in user_data[message.chat.id]:
      user_data[message.chat.id]['rost'] = message.text
      a.send_message(message.chat.id, "Вау, твой рост {0} см\nКогда у тебя день рождения?".format(message.text))
  elif 'day' not in user_data[message.chat.id]:
      user_data[message.chat.id]['day'] = message.text
      a.send_message(message.chat.id, "Классно, у тебя {0} день рождения".format(message.text))
a.polling()
