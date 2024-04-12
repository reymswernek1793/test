import telebot
import requests
from telebot import types

token = '7095274403:AAFQkCa5tVLhPX0PfIg9UrmHRWCjqpM1TT4'
API = 'https://currency-converter-pro1.p.rapidapi.com/convert'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup=types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('GBP', callback_data='GBP'),
               types.InlineKeyboardButton('USD', callback_data='USD'),
               types.InlineKeyboardButton('RUB', callback_data='RUB'))


