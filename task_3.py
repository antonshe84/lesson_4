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
from decimal import Decimal

"""
<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="21.02.2021" name="Foreign Currency Market">
<Valute ID="R01010"><NumCode>036</NumCode><CharCode>AUD</CharCode><Nominal>1</Nominal><Name>Австралийский доллар</Name><Value>58,2249</Value></Valute>
<Valute ID="R01020A"><NumCode>944</NumCode><CharCode>AZN</CharCode><Nominal>1</Nominal><Name>Азербайджанский манат</Name><Value>43,5196</Value></Valute>
"""

import requests
from datetime import datetime, date

serv = 'http://www.cbr.ru/scripts/XML_daily.asp'

def find_tag(st, tag1, tag2):
    t1 = st.find(tag1)
    t2 = st.find(tag2, t1 + len(tag1))
    if t1 == -1 or t2 == -1:
        return None
    tag_text = st[t1 + len(tag1):t2]
    if tag_text:
        return tag_text
    else:
        return None

def currency_rates(val):
	# Получаем текст запроса
	response = requests.get(serv)
	s = response.text
	date_val = find_tag(s, '<ValCurs Date="', '"')   	# 21.02.2021
	date_return = date(int(date_val[6:10]), int(date_val[3:5]), int(date_val[0:2]))
	s = s[s.find('<Valute'):]
	valute = find_tag(s, '<Valute', '</Valute>')
	valute_course = {}
	while valute:
		valute_course[find_tag(valute, '<CharCode>', '</CharCode>').lower()] = \
			float(find_tag(valute, '<Value>', '</Value>').replace(",", "."))
		s = s[len(valute) + 16:]
		valute = find_tag(s, '<Valute', '</Valute>')
	course_ret = valute_course.get(val.lower())
	if course_ret is None:
		return None
	else:
		return [course_ret, date_return]


if __name__ == '__main__':
	while True:
		v = input("Введите валюту (например USD), для выхода наберите 'exit': ")
		if v == "exit": break
		d = currency_rates(v)
		if d is None:
			print("Валюта указана не верно, повторите ввод")
		else:
			print(f'{d[0]:0.2f}, {d[1].strftime("%Y-%m-%d")}')




