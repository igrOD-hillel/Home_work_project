# задача5
# Вводятся три целых числа. Определить какое из них наибольшее.
#
a = int(input("Введите число A. A= "))
b = int(input("Введите число B. B= "))
c = int(input("Введите число C. C= "))
if a > b and a > c:
    print(f"A = {a} is maximum")
elif b > a and b > c:
    print(f"B = {b} is maximum")
else:
    print(f"C = {c} is maximum")
