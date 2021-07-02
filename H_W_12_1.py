# Задача 1
# Проработать встроенние функции множеств. Встроенние функции можно взять на сайте
# (https://www.programiz.com/python-programming/set).
# Но на єтом сайте приведени примери для списков, Задача переделать примери для множеств.
#==================================================================================================================

#Function                                Description
#   all()               Returns True if all elements of the set are true( or if the set is empty).
my_set = {800, 100, 200, 300, 400, 500, 600}
my_set_f = {False}
print(all(my_set))
print(all(my_set_f))

#   any()               Returns True if any element of the set is true. If the set is empty, returns False.
my_set = {800, 100, 200, 300, 400, 500, 600}
my_set_f = {}
print(any(my_set))
print(any(my_set_f))

#   enumerate()         Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
my_set = {800, 100, 200, 300, 400, 500, 600}
for i in enumerate(my_set):
    print(i)

#   len()               Returns the length (the number of items) in the set.
my_set = {800, 100, 200, 300, 400, 500, 600}
print('Длинна множества:', len(my_set))

#   max()               Returns the largest item in the set.
my_set = {800, 100, 200, 300, 400, 500, 600}
print('Максимальный элемент:', max(my_set))

#   min()               Returns the smallest item in the set.
my_set = {800, 100, 200, 300, 400, 500, 600}
print('Минимальный элемент:', min(my_set))

#   sorted()            Returns a new sorted list from elements in the set (does not sort the set itself).
my_set = {800, 100, 200, 300, 400, 500, 600}
print('Сортировка:',sorted(my_set))

#   sum()               Returns the sum of all elements in the set.
print('Сумма множества:', sum(my_set))
