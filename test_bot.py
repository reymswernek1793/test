import telebot
import requests
from telebot import types

token = ''
API = 'https://currency-converter-pro1.p.rapidapi.com/convert'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])

def hello():
    pass

def start(message):
    markup=types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('GBP', callback_data='GBP'),
               types.InlineKeyboardButton('USD', callback_data='USD'),
               types.InlineKeyboardButton('RUB', callback_data='RUB'))

 bot.send_message(message.chat.id,"Choose a currency: ", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    querystring = {'from': call.data, 'to':'UZS','amount': '1'}

    headers={
        "X-RapidAPI-Key": "bd262d54c7mshf47276b2ceb8ad0p10d8f7jsn038b77b71d63",
        "X-RapidAPI-Host": "currency-converter-pro1.p.rapidapi.com"
    }

    response=requests.get(API, headers=headers, params=querystring)

    if response.status_code==200:
        data=response.json()
        conversion_result=data['result']
        bot.send_message(call.message.chat.id, f'Conversion result: {conversion_result}')
    else:
        bot.send_message(call.message.chat.id, 'Failed to perform conversion. Please try again later')

print("The bot is running....")
bot.polling()

