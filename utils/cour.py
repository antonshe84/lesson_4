import requests
from datetime import date

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
    date_val = find_tag(s, '<ValCurs Date="', '"')  # 21.02.2021
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
    d = currency_rates('USD')
    print(f'{d[0]:0.2f}, {d[1].strftime("%Y-%m-%d")}')
    d = currency_rates('EUR')
    print(f'{d[0]:0.2f}, {d[1].strftime("%Y-%m-%d")}')
