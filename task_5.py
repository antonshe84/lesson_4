"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
 в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего
  лишнего не происходит.
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

from datetime import date
import sys
from course import *


if __name__ == '__main__':
    args = sys.argv

    while True:
        if len(args) > 1:
            v = args[1]
        else:
            v = input("Введите валюту (например USD), для выхода наберите 'exit': ")
        if v == "exit": break
        d = currency_rates(v)
        if d is None:
            print("Валюта указана не верно, повторите ввод")
        else:
            print(f'{d[0]:0.2f}, {d[1].strftime("%Y-%m-%d")}')
        if len(args) > 1: break