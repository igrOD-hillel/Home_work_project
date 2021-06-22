# 5.Дан список стран и городов каждой страны.
#   Затем дан cсмписок названия городов.
#   Для каждого города укажите, в какой стране он находится.
country = ['Ukraine', 'Germany', 'Italy', 'France']
city = [('Kiyv', 'Odessa'), ('Berlin', 'Humburg'), 'Rome', 'Paris']
A = dict(zip(country, city))
print(A)
