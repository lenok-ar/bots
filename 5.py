import telebot
import requests
a = telebot.TeleBot("7806687336:AAGUezfbPHEKzUPqtAS0OYxrrGsVDNmplDE")
 
user_data = {}
 
@a.message_handler(commands=['start'])
def startWork(message):
  user_data[message.chat.id] = {}
  a.send_message(message.chat.id, "Нажми на /cat или напиши в чат, чтобы я отправил тебе фото котика")
 
@a.message_handler(commands=['cat'])
def sendYourMessage(message):
  url = "https://api.thecatapi.com/v1/images/search"
  response = requests.get(url)
  if response.status_code == 200:
  	data = response.json()
  	image_url = data[0]['url']
      a.send_photo(message.chat.id, image_url)
 
a.polling()

