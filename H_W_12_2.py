# Задача 2
# Дано три множества
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
# Одним действием (одной строкой) виполнить intersection єтих множеств

res_set = set1 & set2 & set3
print('Пересечение множеств: ', res_set)
print(set1.intersection(set2, set3))
