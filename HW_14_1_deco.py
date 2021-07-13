# Декораторы:
# Создать функцию для генерации списка словарей вида:
# [{0:0,}, {0:0, 1:1}, {0:0, 1:1, 2:4}, {0:0, 1:1, 2:4, 3:9}, {0:0, 1:1, 2:4, 3:9, ... n: n**2}, ]
# где n – именованный аргумент функции.
# Функция будет использовать цикл for, внутри которой при помощи Dict Comprahansion
# будут генерироваться вложенные словари.
# Запись в результирующий список производиться при помощи метода append.
# Создать декоратор для вычисления времени выполнения функци. Для создания декоратора использовать модуль datetime.
# Результатом вызова функции должен быть вывод самого списка и продолжительности выполнения генерирования списка.

from _datetime import datetime


def deco_func(function):
    def wrapper(n: int):
        cw_start = datetime.now()
        fin = function(n)
        print(datetime.now() - cw_start)
    return wrapper


@deco_func
def my_res_func(n):
    gen_list = []
    for n in range(n+1):
        gen_dict = {n: n**2 for n in range(n+1)}
        gen_list.append(gen_dict)
    return print(gen_list)


my_res_func(500)
