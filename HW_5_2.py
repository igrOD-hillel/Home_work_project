# задача2
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input("Введите число A. A= "))
b = int(input("Введите число B. B= "))
c = int(input("Введите число C. C= "))
print(a, b, c)
if a > b > c or c > b > a:
    print("Среднее значение, B=", b)
elif b > a > c or c > a > b:
    print("Среднее значение, A=", a)
elif a > c > b or b > c > a:
    print("Среднее значение, C=", c)
else:
    print("STOP")
