import telebot
import os
from dotenv import load_dotenv, find_dotenv
import requests
from datetime import datetime
from bs4 import BeautifulSoup

load_dotenv(find_dotenv())


def money_convert(message):
    print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || " +
          message.text)
    bot = telebot.TeleBot(os.getenv('TOKEN'))
    datenow = datetime.now()
    datenow = datenow.strftime('%d.%m.%Y')
    response = requests.get("https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To="+datenow)
    soup = BeautifulSoup(response.text, 'lxml')
    currencies = soup.find_all('table', class_='data')
    for currency in currencies:
        currency = currency.text.split('\n')
        currency = [i for i in currency if i != '']
    for w in range(0, len(currency), 5):
        currency[w+4] = currency[w+4].replace(",", ".", 1)
    convert = message.text.split()
    try:        
        if convert[0] == "RUB":
            k = 0
            for z in range(0, len(currency), 5):
                if convert[2] == currency[z+1]:
                    try:
                        bot.send_message(message.chat.id, str((float(convert[1])/float(currency[z+4])) *
                                                              float(currency[z+2])))
                    except ValueError:
                        bot.send_message(message.chat.id, "Некорректный ввод")
                    k = 1
            if k == 0:
                bot.send_message(message.chat.id, "Не обладаем курсом такой валюты, посмотрите список доступной валюты")
        elif convert[2] == "RUB":
            k = 0
            for z in range(0, len(currency), 5):
                if convert[0] == currency[z+1]:
                    try:
                        bot.send_message(message.chat.id, str((float(convert[1])/float(currency[z+2])) *
                                                              float(currency[z+4])))
                    except ValueError:
                        bot.send_message(message.chat.id, "Некорректный ввод")
                    k = 1
            if k == 0:
                bot.send_message(message.chat.id, "Не обладаем курсом такой валюты, посмотрите список доступной валюты")
        else:
            k = 0
            for z in range(0, len(currency), 5):
                if convert[0] == currency[z+1]:
                    for x in range(0, len(currency), 5):
                        if convert[2] == currency[x+1]:
                            try:
                                bot.send_message(message.chat.id, str((((float(convert[1])/float(currency[z+2])) *
                                                                        float(currency[z+4]))/float(currency[x+4])) *
                                                                      float(currency[x+2])))
                            except ValueError:
                                bot.send_message(message.chat.id, "Некорректный ввод")
                            k = 1
            if k == 0:
                bot.send_message(message.chat.id, "Не обладаем курсом такой валюты, посмотрите список доступной валюты")
    except IndexError:
        bot.send_message(message.chat.id, "Некорректный ввод")
