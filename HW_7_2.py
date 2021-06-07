import random
import string
items = int(input("Введите кол-во элементов списка: "))
f_letters = str(input("Введите искомый символ: "))
A = []
letters = string.ascii_letters
count = 0
while len(A) < items:
    length = random.randint(1, 20)
    rand_string = ''.join(random.choice(letters) for i in range(length))
    A.append(rand_string)
print("Сформирован список А содержащий элементы: ", A)
for x in A:
    count += x.count(f_letters)
    print("В элементе " "%-20s %-3d" "символов " "%-3s" % (x, x.count(f_letters), f_letters))
print(f"В спсиске А найдено {count} символов '{f_letters}'")
