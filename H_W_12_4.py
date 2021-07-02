# Задача 4
# Дано три множества
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
# Одним действием (одной строкой) виполнить union єтих множеств

res_set = set1 | set2 | set3

print(res_set)
print(set1.union(set2, set3))
