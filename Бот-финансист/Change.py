import telebot
import requests
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.getenv('TOKEN'))


def course_change(message):
    x = 0
    datenow = datetime.now()
    for k in range(0, 8):
        date = datenow - timedelta(days=k)
        date = date.strftime('%d.%m.%Y')
        response = requests.get("https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To="+date)
        soup = BeautifulSoup(response.text, 'lxml')
        currencies = soup.find_all('table', class_='data')
        for currency in currencies:
            currency = currency.text.split('\n')
            currency = [i for i in currency if i != '']
        for z in range(0, len(currency), 5):
            if message.text == currency[z+1]:
                bot.send_message(message.chat.id, date+'\n'+currency[z]+' || '+currency[z+1]+' || '+currency[z+2]+' || '
                                 + currency[z+3]+' || '+currency[z+4])
                x = 1
                break
    if x == 0:
        bot.send_message(message.chat.id, "Не обладаем курсом такой валюты, посмотрите список доступной валюты")
