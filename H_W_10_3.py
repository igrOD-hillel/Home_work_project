# Задача 3
# Дано два списка
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

# Создать из них список кортежей
list_c = [(1, 5), (2, 6), (3, 7), (4, 8)]

list_d = list(zip(list_a, list_b))
print(list_d, list_d == list_c)
