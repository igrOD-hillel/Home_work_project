# задача7
# Определить четверть координатной плоскости, которой принадлежит точка.
# Координаты точки ввести с клавиатуры.
x, y = map(int, input("Введите координаты (x, y), через пробел: ").split())
if x > 0 and y > 0:
    print(f"Точка с координатами ({x}, {y}), лежит в I четверти.")
elif x < 0 and y > 0:
    print(f"Точка с координатами ({x}, {y}), лежит во II четверти.")
elif x < 0 and y < 0:
    print(f"Точка с координатами ({x}, {y}), лежит в III четверти.")
elif x > 0 and y < 0:
    print(f"Точка с координатами ({x}, {y}), лежит в IV четверти.")
