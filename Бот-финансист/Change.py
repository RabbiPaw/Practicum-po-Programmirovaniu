import telebot
from telebot import types
import requests
from datetime import *
from bs4 import BeautifulSoup
bot = telebot.TeleBot("6236793579:AAFf_J9zh8xXyS4r519tug1jmjGK5H0nHjM")
def Course_change(message):
    x=0
    datenow = datetime.now()
    for k in range(0,8):
        user_id = 12345
        date = datenow - timedelta(days=k)
        date=date.strftime('%d.%m.%Y')
        response = requests.get("https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To="+date)
        soup = BeautifulSoup(response.text, 'lxml')
        valuts = soup.find_all('table',class_='data')
        for valut in valuts:
            valut=valut.text.split('\n')
            valut =[i for i in valut if i!='']
        for z in range(0,len(valut),5):
            if message.text==valut[z+1]:
                bot.send_message(message.chat.id,date+'\n'+valut[z]+' || '+valut[z+1]+' || '+valut[z+2]+' || '+valut[z+3]+' || '+valut[z+4])
                x=1
                break
    if x==0:
        bot.send_message(message.chat.id,"Не обладаем курсом такой валюты, посмотрите список доступной валюты")
