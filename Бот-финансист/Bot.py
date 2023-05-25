import telebot
from telebot import types
from datetime import datetime
from ЦБ import update_data_and_print_money
from Metals import update_data_and_print_metal
from Converter import money_convert
from Change import course_change
from Anek import anekdot
from Dict import dictionary
print("ник бота в телеграмме https://t.me/FinBirMonBot")
bot = telebot.TeleBot(open("ключ бота.txt").readline())


@bot.message_handler(commands=['start'])
def start_message(message):
    print(str(datetime.now())+" || " + str(message.from_user.id)+" || "+str(message.from_user.username)+" || " +
          message.text)
    bot.send_message(message.chat.id, 'Привет, я бот, который покажет тебе нынешние курсы валют, '
                                      'поможет с переводом денежных валют')
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton("Начать")
    markup.add(item1)
    bot.send_message(message.chat.id, "Нажмите начать", reply_markup=markup)


@bot.message_handler(content_types='text')
def button_message(message):
    if message.text == "Начать" or message.text == "Назад":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || " +
              message.text)
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Курсы валют к рублю")
        markup1.add(item1)
        item2 = types.KeyboardButton("Курсы акций металлов (изменения за последние 30 дней)")
        markup1.add(item2)
        item3 = types.KeyboardButton("Конвертатор валют")
        markup1.add(item3)
        item4 = types.KeyboardButton("Изменение курса валюты в течении последних 7 дней")
        markup1.add(item4)
        item5 = types.KeyboardButton("Экономический термин")
        markup1.add(item5)
        item6 = types.KeyboardButton("Небольшой анекдот")
        markup1.add(item6)
        item7 = types.KeyboardButton("Информация")
        markup1.add(item7)
        bot.send_message(message.chat.id, 'Выберите что хотите узнать или сделать', reply_markup=markup1)
    elif message.text == "Конвертатор валют":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || "
              + message.text)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Конвертация с рублями")
        markup2.add(button1)
        button2 = types.KeyboardButton("Конвертация иностранных валют")
        markup2.add(button2)
        button3 = types.KeyboardButton("Назад")
        markup2.add(button3)
        bot.send_message(message.chat.id, 'Выберите тип конвертации', reply_markup=markup2)
    elif message.text == "Конвертация с рублями":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || " +
              message.text)
        bot.send_message(message.chat.id, "Введите валюты в формате: Исходная_валюта Значение Конечная_валюта "
                                          "(RUB - рубли)(Все валюты через буквенный код)")
        bot.register_next_step_handler(message, money_convert)
    elif message.text == "Конвертация иностранных валют":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || " +
              message.text)
        bot.send_message(message.chat.id, "Введите валюты в формате: Исходная_валюта Значение Конечная_валюта "
                                          "(Все валюты через буквенный код)")
        bot.register_next_step_handler(message, money_convert)
    elif message.text == "Курсы валют к рублю":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || "
              + message.text)
        update_data_and_print_money(message)
    elif message.text == "Курсы акций металлов (изменения за последние 30 дней)":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || "
              + message.text)
        update_data_and_print_metal(message)
    elif message.text == "Изменение курса валюты в течении последних 7 дней":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || " +
              message.text)
        bot.send_message(message.chat.id, "Введите валюту, изменение курса которой, вы хотите посмотреть "
                                          "(Валюта в виде буквенного кода)")
        bot.register_next_step_handler(message, course_change)
    elif message.text == "Небольшой анекдот":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || "
              + message.text)
        anekdot(message)
    elif message.text == "Экономический термин":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || "
              + message.text)
        dictionary(message)
    elif message.text == "Информация":
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || "
              + message.text)
        bot.send_message(message.chat.id, ("Информация о проекте:"+"\n" +
                                           "Создатели : Салабун С.И. Студент ОмГТУ Группы ФИТ-222 (sivitik44@gmail.com)"
                                           ", Овчинников С.А. Студент ОмГТУ группы ФИТ-222 (ovstal@gmail.com)"+"\n"
                                           + "Информация взята с сайта Центрального банка РФ (https://cbr.ru)"+"\n"
                                           + "Анекдоты взяты сайта Анекдотбар (https://anekdotbar.ru/pro-dengi/)"))
    else:
        print(str(datetime.now())+" || " + str(message.from_user.id)+" || " + str(message.from_user.username)+" || "
              + message.text)
        bot.send_message(message.chat.id, ' Я тебя не понимаю напиши /start')


bot.infinity_polling()
