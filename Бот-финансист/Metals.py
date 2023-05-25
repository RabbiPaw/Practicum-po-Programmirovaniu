import telebot
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
bot = telebot.TeleBot(open("ключ бота.txt").readline())


def update_data_and_print_metal(message):
    datenow = datetime.now()
    date = datenow - timedelta(days=30)
    datenow = datenow.strftime('%d.%m.%Y')
    date = date.strftime('%d.%m.%Y')
    response = requests.get("https://cbr.ru/hd_base/metall/metall_base_new/?UniDbQuery.Posted=True&UniDbQuery.From=" +
                            date + "&UniDbQuery.To=" + datenow + "&UniDbQuery.Gold=true&UniDbQuery.Silver=true"
                            "&UniDbQuery.Platinum=true&UniDbQuery.Palladium=true&UniDbQuery.so=1")
    soup = BeautifulSoup(response.text, 'lxml')
    currencies = soup.find_all('table', class_='data')
    for currency in currencies:
        currency = currency.text.split('\n')
        currency = [i for i in currency if i != '']
    for z in range(0, len(currency), 5):
        bot.send_message(message.chat.id, currency[z]+' || '+currency[z+1]+' || '+currency[z+2]+' || '+currency[z+3] +
                         ' || ' + currency[z+4]+' || ')
