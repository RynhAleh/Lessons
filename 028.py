# Пользователь вводит последовательность чисел строкой.
# Нужно вывести список и кортеж с этими числами.

list1 = input("Введите последовательность чисел, разделенных пробелами: ").strip().split()
try:
    list1 = [int(elem) for elem in list1]
except ValueError:
    print("Все значения должны быть числами!")
else:
    print(f'{list1}\n{tuple(list1)}')
