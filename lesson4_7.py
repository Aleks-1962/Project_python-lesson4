"""Реализуем генератор с помощью функции yield(), вычисляем факториал  """

from math import factorial

n = int(input('Введите число, для вычисления факториала - '))


def generator():
    for el in range(1, n+1):
        print('Элемент ' + str(el))
        yield factorial(el)


my_gen = generator()
i = 0
for i in my_gen:
    print(i)
