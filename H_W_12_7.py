# Задача 7
# Возвращает новый набор со всеми элементами из обоих наборов, удаляя дубликаты.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

res_set = set1.symmetric_difference(set2)
print(res_set)
print(set1 ^ set2)
