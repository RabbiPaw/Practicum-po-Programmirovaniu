import telebot
from telebot import types
import requests
from datetime import *
from bs4 import BeautifulSoup

def Money_Convert(message):
    print(str(datetime.now())+" || " +str(message.from_user.id)+" || "+str(message.from_user.username)+" || " + message.text)
    bot = telebot.TeleBot("6236793579:AAFf_J9zh8xXyS4r519tug1jmjGK5H0nHjM")
    user_id = 12345
    datenow = datetime.now()
    datenow=datenow.strftime('%d.%m.%Y')
    response = requests.get("https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To="+datenow)
    soup = BeautifulSoup(response.text, 'lxml')
    valuts = soup.find_all('table',class_='data')
    for valut in valuts:
        valut=valut.text.split('\n')
        valut =[i for i in valut if i!='']
    for w in range(0,len(valut),5):
        valut[w+4]=valut[w+4].replace(",",".",1)
    Convert = message.text.split()
    try:        
        if Convert[0]=="RUB":
            k=0
            for z in range(0,len(valut),5):
                if (Convert[2]==valut[z+1]):
                    try:
                        bot.send_message(message.chat.id, str((float(Convert[1])/float(valut[z+4]))*float(valut[z+2])))
                    except ValueError:
                        bot.send_message(message.chat.id,"Некорректный ввод")
                    k=1
            if k==0:
                bot.send_message(message.chat.id,"Не обладаем курсом такой валюты, посмотрите список доступной валюты")
        elif Convert[2]=="RUB":
            k=0
            for z in range(0,len(valut),5):
                if (Convert[0]==valut[z+1]):
                    try:
                        bot.send_message(message.chat.id, str((float(Convert[1])/float(valut[z+2]))*float(valut[z+4])))
                    except ValueError:
                        bot.send_message(message.chat.id,"Некорректный ввод")
                    k=1
            if k==0:
                bot.send_message(message.chat.id,"Не обладаем курсом такой валюты, посмотрите список доступной валюты")
        else:
            k=0
            for z in range(0,len(valut),5):
                if (Convert[0]==valut[z+1]):
                    for x in range(0,len(valut),5):
                        if(Convert[2]==valut[x+1]):
                            try:
                                bot.send_message(message.chat.id, str((((float(Convert[1])/float(valut[z+2]))*float(valut[z+4]))/float(valut[x+4]))*float(valut[x+2])))
                            except ValueError:
                                bot.send_message(message.chat.id,"Некорректный ввод")
                            k=1
            if k==0:
                bot.send_message(message.chat.id,"Не обладаем курсом такой валюты, посмотрите список доступной валюты")
    except  IndexError:
        bot.send_message(message.chat.id,"Некорректный ввод")
