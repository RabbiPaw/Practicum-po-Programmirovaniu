import telebot
import requests
import random
import os
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup

load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.getenv('TOKEN'))


def anekdot(message):
    response = requests.get("https://anekdotbar.ru/pro-dengi/")
    soup = BeautifulSoup(response.text, 'lxml')
    currencies = soup.find_all('div', class_='tecst')
    bot.send_message(message.chat.id, random.choice(currencies))
