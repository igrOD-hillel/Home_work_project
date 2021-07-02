# Задача 13
# Удалите элементы из set1, которые не являются общими для set1 и set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)
