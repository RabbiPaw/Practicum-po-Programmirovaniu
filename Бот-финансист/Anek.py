import telebot
import requests
import random
from bs4 import BeautifulSoup
bot = telebot.TeleBot(open("ключ бота.txt").readline())


def anekdot(message):
    response = requests.get("https://anekdotbar.ru/pro-dengi/")
    soup = BeautifulSoup(response.text, 'lxml')
    currencies = soup.find_all('div', class_='tecst')
    bot.send_message(message.chat.id, random.choice(currencies))
