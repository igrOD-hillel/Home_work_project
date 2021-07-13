# Функциональное программирование:
# Дано 3 списка
# Используя методи функционального програмирования:
# 1. Из первого и третьего списков оставить все четные числа;


def find_even_n(*args):
    return list(filter(lambda x: not x % 2, *args))


# 2. Со второго оставить все нечетные;


def find_odd_n(*args):
    return list(filter(lambda x: x % 2, *args))


# 3. Объединить списки в один список кортежей пар (значение первого списка,
# значение второго списка, значение третьего списка);


def comb_list(*args):
    return tuple(zip(*args))


# 4. По каждому кортежу определить сумму его значений, получите список сумм кортежей;


def sum_comb(*args):
    return list(map(sum, *args))


# 5. После получения списка п.4 оставить в нем только нечетные значения.
# Код оформить в виде функций.
# Код должен быть максимально автоматизирован

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# 1.
res_l_1 = find_even_n(list_1)
print(res_l_1)
res_l_3 = find_even_n(list_3)
print(res_l_3)
# 2.
res_l_2 = find_odd_n(list_2)
print(res_l_2)
# 3.
res_comb = comb_list(res_l_1, res_l_2, res_l_3)
print(res_comb)
# 4.
res_sum = sum_comb(res_comb)
print(res_sum)
# 5.
final_res = find_odd_n(res_sum)
print(final_res)
