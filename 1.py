import telebot
a = telebot.TeleBot("7873627575:AAHmPxX7I60rP_bPSX9RUSd3upyrRKeKCTo")

keyboard_test = telebot.types.ReplyKeyboardMarkup(True)
keyboard_test.row("Новостные (СМИ)", "Общие сайты (блоги и форумы)", "Англоязычные ресурсы")

@a.message_handler(commands=['start'])
def startWork(message):

    tid = message.chat.id
    a.send_message(tid, "Бот готов к работе!", reply_markup = keyboard_test)

@a.message_handler(content_types=['text'])
def sendYourMessage(message):
    mid = message.chat.id

    if message.text == "Новостные (СМИ)":
        a.send_message(mid, "1.3DNews(https://3dnews.ru/) – согласно описанию сайта, публикация новостей и аналитики в компьютерных технологиях, результатов тестирования компьютерной техники (видеокарт, мультимедиа, принтеров, сканеров и др)\n2.Tproger(https://tproger.ru/) – интернет-издание о разработке, публикуют актуальные новости, авторские статьи и переводы.\n3.Dou(https://dou.ua/) – украинский новостной сайт с публикациями об IT-индустрии в стране и мире, а также со статистикой зарплат работников и рейтингом компаний.\n4.DevBy(https://devby.io/) – белорусский новостной сайт с публикациями об IT-индустрии в стране и мире. На сайте размещаются новости, интервью, репортажи, аналитика.\n5.IXBT(https://www.ixbt.com/) – новостной сайт с разборами техники, информационных технологий и новых программных продуктов")
    elif message.text =="Общие сайты (блоги и форумы)":
        a.send_message(mid, "1.Securitylab.ru(https://www.securitylab.ru/) – портал, посвященный информационной безопасности.\n2.Unetway(https://unetway.com/blog) – портал для общения между компаниями и IT-специалистами.\n3.Ru.Board(https://forum.ru-board.com/) – форум, где можно обсудить такие IT-проблемы как: компьютерные игры, ремонт компьютеров на дому, фото и видео техника, программирование, графика и многое другое.\n4.Nomobile.ru(http://www.nomobile.ru/) – журнал, посвященный гаджетам.\n5.Computerworld Россия(https://www.computerworld.ru/) — сайт, где публикуются обзоры событий индустрии информационных технологий в России и в мире, а также примеры успешных внедрений информационных систем на российских предприятиях.\n6.Losst(https://losst.pro/) – сайт, целиком посвященный Linux.")
    elif message.text =="Англоязычные ресурсы":
        a.send_message(mid, "1.Network (https://www.networkworld.com/) – печатное еженедельное IT-издание, ориентирующееся на новости и события в мире компьютерных сетей.\n2.Mashable(https://mashable.com/) – мировая техническо-развлекательная медиа-платформа.\n3.Dzone(https://dzone.com/) — сайт, посвящённый вопросам разработки ПО.\n4.CIO(https://www.cio.com/) — англоязычный журнал, связанный с технологиями и ИТ.\n5.Engadget(https://www.engadget.com/) — блог о технологиях, публикующий новости о гаджетах и потребительской электронике.\n6.Sitepoint(https://www.sitepoint.com/) – сообщество со статьями на тему веб-разработки.")

    else:
        a.send_message(mid, "Выберите пожалуйста из предложенных вариантов")

a.polling()
