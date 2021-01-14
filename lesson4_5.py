"""Определяем список четных чисел, с использованием генератора и функции reduce()"""
from functools import reduce

def my_func(pr_el, el):
    return pr_el*el


my_list = [el for el in range(99, 1001) if el % 2 == 0]
print('Список четных чисел - ' + str(my_list))
print('Произведение всех чисел списка - ' + str(reduce(my_func, my_list)))
