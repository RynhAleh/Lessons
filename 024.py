# Вычислить количество отрицательных элементов под главной диагональю матрицы.
import random

spis = []
sub_spis = []
razm = elem = sm_elem = 0

# Запрос размерности матрицы с обработкой исключений
try:
    razm = int(input("Размерность матрицы (2-20): "))
except ValueError:
    print("Ввёденное значение не являются целым числом!")
    exit(0)
if not (1 < razm < 21):
    print("Ввёденное значение должно быть в диапазоне (2-20)!")
    exit(0)

# Заполнение матрицы razm х razm случайными значениями (от -200 до 200)
print(f'Cгенерирована матрица {razm} х {razm} со значениями элементов от -200 до 200:\n')
for i in range(0, razm):
    for j in range(0, razm):
        elem = random.randint(-200, 200)
        sub_spis.append(elem)
        print(str(elem).rjust(5), end='')
    print()
    spis.append(sub_spis)
    sub_spis = []

# Перебор элементов матрицы под диагональю
for i in range(1, razm):
    for j in range(0, i):
        if spis[i][j] < 0:
            sm_elem += spis[i][j]
print(f'\nСумма отрицательных элементов под диагональю матрицы: {sm_elem}.')
