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

"""
<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="21.02.2021" name="Foreign Currency Market"><Valute ID="R01010"><NumCode>036</NumCode><CharCode>AUD</CharCode><Nominal>1</Nominal><Name>Австралийский доллар</Name><Value>58,2249</Value></Valute><Valute ID="R01020A"><NumCode>944</NumCode><CharCode>AZN</CharCode><Nominal>1</Nominal><Name>Азербайджанский манат</Name><Value>43,5196</Value></Valute>
"""



import requests
import requests.utils as utils

valute_course = {}

def find_tag(st, tag1, tag2):
	t1 = st.find(tag1)
	t2 = st.find(tag2)
	print(t1)
	print(t2)
	if t1 == -1 or t2 == -1:
		return None
	tag_text = st[t1+len(tag1):t2]
	if tag_text:
		return tag_text
	else:
		return None


response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
print(type(response.content))
s = response.text
print(s.find('<Valute'))
print(s.find('</Valute'))
print(s[s.find('<Valute')+7:s.find('</Valute')])
print(s)
valute = find_tag(s, '<Valute',  '</Valute>')
while valute:

	print(valute)
	valute_course[find_tag(valute, '<CharCode>', '</CharCode>')] = find_tag(valute, '<Value>', '</Value>')
	s = s[len(valute)+9:]
	print(s)
	valute = find_tag(s, '<Valute',  '</Valute>')
	print(valute)
	
print(valute_course)

# encodings = utils.get_encoding_from_headers(response.headers)
# content = response.content.decode(encoding=encodings)
# print(content)