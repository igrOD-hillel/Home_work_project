#
# 2. Создать python модуль для реализации ввода через клавиатуру дробних (с поавающей запятой) значений.
#     Добавить функционал конвертации во int и str.
#     Вивести результат. на печать.
#
my_float = float(input('Введите значение с плавающей запятой: '))
print(my_float, type(my_float))
my_float_i = int(my_float)
print(my_float_i, type(my_float_i))
my_float_s = str(my_float)
print(my_float_s, type(my_float_s))
