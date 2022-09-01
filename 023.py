# Найти максимальный элемент диагонали матрицы.
import random

spis = []
razm = elem = mx_elem = 0

# Запрос размерности матрицы с обработкой исключений
try:
    razm = int(input("Размерность матрицы (2-20): "))
except ValueError:
    print("Ввёденное значение не являются целым числом!")
    exit(0)
if not (0 < razm < 21):
    print("Ввёденное значение должно быть в диапазоне (2-20)!")
    exit(0)

# Заполнение матрицы razm х razm случайными значениями (от 0 до 200)
print(f'Cгенерирована матрица {razm} х {razm} со значениями элементов от 0 до 200:\n')
for i in range(0, razm):
    sub_spis = []
    for j in range(0, razm):
        elem = random.randint(0, 200)
        sub_spis.append(elem)
        print(str(elem).rjust(4), end='')
    print()
    spis.append(sub_spis)

# Перебор элементов матрицы по диагонали
for i in range(0, razm):
    if spis[i][i] > mx_elem:
        mx_elem = spis[i][i]
print(f'\nМаксимальный элемент диагонали матрицы: {mx_elem}.')
