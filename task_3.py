"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) и возвращающую курс
этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
 http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
 посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция
 должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами
  использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали
   код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
    регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
 в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
  использовать в ответе функции?
"""

import requests
import requests.utils as utils

payload = {'key1': 'CharCode', 'key2': 'Value'}
response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
print(response.text)
print(response.text.find('<Valute'))
print(response.text.find('</Valute'))
print(response.text[response.text.find('<Valute')+7:response.text.find('</Valute')-8])

encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(content)