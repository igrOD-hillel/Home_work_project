# Цикл While
# Задан некоторый список A содержащий целые числа.
# Разработать программу, которая вычисляет сумму элементов списка.
A = list(map(int, input('Введите целые числа через пробел ').split()))
i = 0
sum_A = 0
while i < len(A):
    sum_A = sum_A + A[i]
    i += 1
print(f"Сумма элементов списка A = {A} будет равна: ", sum_A)
