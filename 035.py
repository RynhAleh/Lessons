# Написать функцию, которая заполняет массив случайными числами в диапазоне, указанном пользователем.
# Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать.
# Вывод значений элементов массива должен происходить в основной ветке программы.
import random


def fill_array(_fr: int, _to: int):
    global list1
    for i in range(0, 10):  # поскольку длина массива не предписана, будет 10
        list1.append(random.randint(_fr, _to))


try:
    range_fr = int(input("Диапазон с:  "))
    range_to = int(input("Диапазон по: "))
except ValueError:
    print("Ввёденное значение не являются целым числом!")
else:
    if range_fr >= range_to:
        print('"Диапазон по" должен быть больше "Диапазона с"!')
    else:
        list1 = []
        fill_array(range_fr, range_to)
        print(list1)
