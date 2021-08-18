#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 18.08.2021 1:22:28

import re,sys,os
import telebot
from  config import keys, TOKEN
from  extensions import  ConvertionExeption, CryptoConverter


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def help(message:telebot.types.Message):
    text = 'Что бы начать работу введите комманду боту в следующем формате:\n<имя валюты>, \
<в какую валюту перевести>, \
<количество переводимой валюты >\nУвидить список всех доступных валют: /values '
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for i, key in enumerate(keys.keys()):
        text = '\n'.join((text, f'{i+1}. {key}'))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split ( ',' )
        values = list(map(str.lower, values))
        if len ( values ) != 3:
            raise ConvertionExeption ( 'Перебор с параметрами' )
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to ( (message, f'Не удалось обработать команду\n {e}') )
    else:
        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()