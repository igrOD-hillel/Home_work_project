# Задача 2
# Дано словарь
a_dictionary = {"a": 1, "b": 2, "c": 3}
res = [('a', 1), ('b', 2), ('c', 3)]
# Преобразовать его в список кортежей
my_res = list(a_dictionary.items())
print(my_res == res)
print(my_res)
