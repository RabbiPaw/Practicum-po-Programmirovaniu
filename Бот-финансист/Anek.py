import telebot
from telebot import types
import requests
import random
from datetime import datetime
from bs4 import BeautifulSoup
bot = telebot.TeleBot("6236793579:AAFf_J9zh8xXyS4r519tug1jmjGK5H0nHjM")
def Anekdot(message):
    user_id = 12345
    response = requests.get("https://anekdotbar.ru/pro-dengi/")
    soup = BeautifulSoup(response.text, 'lxml')
    valuts = soup.find_all('div',class_='tecst')
    for valut in valuts:
        valut="<br>".join(valut.text.split())
        valut =[i for i in valut if i!='']   
    bot.send_message(message.chat.id,random.choice(valuts))

