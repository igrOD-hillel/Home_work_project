# Задача 5
# Дано список
lst = ["bar", "baz", "qux", "etc"]

# Создать кортеж
lst.insert(0, "foo")
my_res = tuple(lst)
print(my_res)

res = ("foo", "bar", "baz", "qux", "etc")
print(my_res == res)
