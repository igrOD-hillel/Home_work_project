# задача1
# Из двух случайных чисел, одно из которых четное, а другое нечетное, определить и вывести на экран нечетное число.
import random
x = random.randrange(0, 101)
y = random.randrange(0, 101)
if x % 2 and y % 2 or x % 2 == 0 and y % 2 == 0:
    x += 1
print(x, y)
if x % 2:
    print("x=", x, "Нечетное число")
else:
    print("y=", y, "Нечетное число")
