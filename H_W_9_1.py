# 1.Создайте словарь с количеством элементов не менее 5-ти.
A = {'BMW': 'X5M', 'Audi': 'RSQ8', 'Toyota': 'Rav4',
     'Honda': 'CR-V', 'Mazda': 'CX5', 'Opel': 'Astra'}
task_0 = id(A)
print(A, id(A))

#  1.1. Поменяйте местами первый и последний элемент объекта.
i_f = list(A.items())[0]
i_l = list(A.items())[-1]
A[i_f[0]] = i_l[1]
A[i_l[0]] = i_f[1]
print(A, id(A))
task_1_1 = id(A)

#  1.2. Удалите второй элемент.
A.pop('Audi', 'RSQ8')
print(A, id(A))
task_1_2 = id(A)

#  1.3. Добавьте в конец ключ «new_key» со значением «new_value».
A.setdefault('new_key', 'new_value')
task_1_3 = id(A)
print(A, id(A))

#  1.4. Выведите на печать итоговый словарь.
#       Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
print('ID task 0 (Create) = ', task_0)
print('ID task 1.1 (Change)= ', task_1_1)
print('ID task 1.2 (Delete) = ', task_1_2)
print('ID task 1.3 (Add) = ', task_1_3)
