# 4.Найдите сумму и произведение элементов списка.
#   Результаты вывести на экран;

list_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
sum_list = 0
mult_list = 1
for i in list_2:
   sum_list += i
   mult_list *= i
print(f'Сумма элементов list_2 = ', sum_list)
print(f'Произведение элементов list_2 = ', mult_list)
