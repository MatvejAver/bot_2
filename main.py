from config import token
from logic import password_gen,len_password,get_duck_image_url
import telebot
from os import listdir
from random import choice

mode = 0
bot = telebot.TeleBot(token)    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    bot.reply_to(message, get_duck_image_url())

@bot.message_handler(commands=['mem'])
def info(message):
    with open(f'images/{choice(listdir('images'))}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['password'])
def password(message):
    global mode
    mode = 1
    bot.send_message(message.chat.id, 'Введите длинну пароля:')

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, """\
список команд: /start, /info
""")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Здравствуйте! Введите /info, чтобы узнать команды.')
    
@bot.message_handler(content_types=['photo'])
def send_welcome(message):
    bot.reply_to(message, 'Какое красивое фото!')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global mode
    if message.text.lower() == 'привет':
        bot.reply_to(message, '👋')
        bot.send_message(message.chat.id, 'Здравствуйте! Как ваши дела?')

    elif message.text.lower() == 'пока':
        bot.reply_to(message, '😁')
        bot.send_message(message.chat.id, 'До новых встреч!')

    elif mode == 1:
        mode = 0
        if len_password(message.text) == True:  
            bot.send_message(message.chat.id, f'Вот ваш пароль из {message.text} символов: {password_gen(int(message.text))}')

        else:
            bot.reply_to(message, 'Введенны неверные данные!')

    else:
        bot.reply_to(message, message.text)


bot.infinity_polling()