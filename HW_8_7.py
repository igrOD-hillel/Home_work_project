# 7.Поменять местами самый большой и самый маленький элементы списка;

A = [24, 467, 0, 32, 12, 23, 6, 252, 67, 21, -52, 87, 125, 457]
print('A: ', A)
min_el = min(A)
max_el = max(A)
i_min = A.index(min_el)
i_max = A.index(max_el)
A[i_min] = max_el
A[i_max] = min_el
print('A: ', A)
