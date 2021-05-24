#
# 1. Создать python модуль для реализации ввода через клавиатуру целочисленних значений
#    Добавить функционал конвертации во float и str. Вивести результат на печать.
#
my_int = int(input('Введите целочисленное значение: '))
print(my_int, type(my_int))
my_int_f = float(my_int)
print(my_int_f, type(my_int_f))
my_int_s = str(my_int)
print(my_int_s, type(my_int_s))
