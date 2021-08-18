#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 18.08.2021 1:22:28

import re,sys,os
import  requests
import  json
from  config import  keys

class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExeption ( f'Нельзя переводить {quote} в {base}' )

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption ( f'Не удалось обработать валюту {quote} её нет в списке /values' )
        try:
            quote_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption ( f'Не удалось обработать валюту {base} её нет в списке /values' )
        try:
            amount = float ( amount )
        except KeyError:
            raise ConvertionExeption ( f'Не удалось обработать количество {amount}' )
        r = requests.get ( f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}' )
        total_base = json.loads(r.content)[keys[base]]
        return  total_base
