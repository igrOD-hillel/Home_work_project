# задача3
# Вводятся координаты (x;y) точки и радиус круга (r).
# Определить принадлежит ли данная точка кругу, если его центр находится в начале координат.
x = float(input("Введите координату X. X= "))
y = float(input("Введите координату Y. Y= "))
r = float(input("Введите радиус круга R. R= "))
new_r = (x**2 + y**2)**0.5
if r > new_r:
    print(f"Точка с координатами ({x},{y}) принадлежит кругу с радиусом {r}")
else:
    print(f"Точка с координатами ({x},{y}) не принадлежит кругу с радиусом {r}")

