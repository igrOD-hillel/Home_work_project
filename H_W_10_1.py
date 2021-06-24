# Задача 1
# Дано список словорей
# [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
A = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
# Создать список кортежей [('red', 'high'), ('yellow', 'low')]
my_res = []
for i in range(len(A)):
    my_res.append(tuple(A[i].values()))
print(my_res)
res = [('red', 'high'), ('yellow', 'low')]
print(res == my_res)
