"""Реализуем 2 скрипта итератора с использованием функции count() b cycle() """

from itertools import count

var_sop = int(input('Введите начальное значение - '))
var_eop = int(input('Введите конечное значение - '))
for el in count(var_sop):
    if el > var_eop:
        break
    else:
        print(el)

from itertools import cycle

progr_lang = ["python", "java", "perl", "javascript"]

i = 0
var_eop = int(input('Введите конечное значение счетчика - '))
for el in cycle(progr_lang):
    if i > var_eop:
        break
    print(el)
    i +=1
