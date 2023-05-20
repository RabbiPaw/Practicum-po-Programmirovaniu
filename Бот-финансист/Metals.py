import telebot
from telebot import types
import requests
from datetime import *
from bs4 import BeautifulSoup
bot = telebot.TeleBot("6236793579:AAFf_J9zh8xXyS4r519tug1jmjGK5H0nHjM")
def Update_Data_And_Print_Metal(message):
    x=0
    user_id = 12345
    datenow = datetime.now()
    user_id = 12345
    date = datenow - timedelta(days=30)
    datenow=datenow.strftime('%d.%m.%Y')
    date=date.strftime('%d.%m.%Y')
    response = requests.get("https://cbr.ru/hd_base/metall/metall_base_new/?UniDbQuery.Posted=True&UniDbQuery.From="+date+"&UniDbQuery.To="+datenow+"&UniDbQuery.Gold=true&UniDbQuery.Silver=true&UniDbQuery.Platinum=true&UniDbQuery.Palladium=true&UniDbQuery.so=1")
    soup = BeautifulSoup(response.text, 'lxml')
    valuts = soup.find_all('table',class_='data')
    for valut in valuts:
        valut=valut.text.split('\n')
        valut =[i for i in valut if i!='']
    for z in range(0,len(valut),5):
            bot.send_message(message.chat.id,valut[z]+' || '+valut[z+1]+' || '+valut[z+2]+' || '+valut[z+3] +' || '+valut[z+4]+' || ')

