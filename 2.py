import telebot
a = telebot.TeleBot("7750348601:AAGi1ZKxfeQ2-uiqsIXXdFUPDsPqUgLYNuA")
@a.message_handler(commands=['start'])
def startWork(message):
  tid = message.chat.id
  a.send_message(tid, "Привет. Я понимаю только голосовые сообщения")

@a.message_handler(content_types=['text'])
def sendYourMessage(message):
  mid = message.chat.id
  if message.text == "П":
    a.send_message(mid, "Привет:)")
  else:
    a.send_message(mid, "Отправьте голосовое сообщение")

@a.message_handler(content_types=['voice'])
def handle_voice(message):
    a.send_message(message.chat.id, "Это голосовое сообщение")

a.polling()
