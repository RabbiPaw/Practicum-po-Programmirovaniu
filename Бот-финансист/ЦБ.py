import telebot
import requests
from datetime import datetime
from bs4 import BeautifulSoup
bot = telebot.TeleBot(open("ключ бота.txt").readline())


def update_data_and_print_money(message):
    datenow = datetime.now()
    datenow = datenow.strftime('%d.%m.%Y')
    response = requests.get("https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To="+datenow)
    soup = BeautifulSoup(response.text, 'lxml')
    valuts = soup.find_all('table', class_='data')
    for currency in valuts:
        currency = currency.text.split('\n')
        currency = [i for i in currency if i != '']
    for z in range(0, len(currency), 5):
        bot.send_message(message.chat.id, currency[z]+' || '+currency[z+1]+' || '+currency[z+2]+' || '+currency[z+3] +
                         ' || '+currency[z+4]+' || ')
