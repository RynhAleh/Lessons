# Сгенерировать n множеств (нумерацию начать с 1).
# Вывести элементы, которые входят во все множества с номерами, кратными трём, но не входят в первое множество.
import random

# Запрос размерности матрицы с обработкой исключений
cnt = 0
try:
    cnt = int(input("Сгенерировать количество множеств (3-21): "))
except ValueError:
    print("Ввёденное значение не являются целым числом!")
    exit(0)
if not (3 <= cnt <= 21):
    print("Ввёденное значение должно быть в диапазоне (3-21)!")
    exit(0)

# Генерация заданного количества множеств по 30 генераций элементов в каждом
my_list = []
for i in range(0, cnt):
    my_set = set()
    for j in range(0, 30):
        my_set.add(random.randint(1, 30))
    my_list.append(my_set)
    print("%2i" % (i + 1), my_list[i])

# Непосредственно решение и вывод результата
union_set = my_list[2]
for i in range(2, cnt, 3):
    union_set &= my_list[i]
print(f'Есть в каждом третьем: {union_set if union_set else "Отсутствуют."}')
union_set -= my_list[0]
print(f'Есть в каждом третьем, но нет в первом: {union_set if union_set else "Отсутствуют."}')