import math

try:
    a = float(input("Введите число, из которого извлечь квадратный корень: "))
except (TypeError, ValueError):
    print("Введенное значение не является числом!")
else:
    try:
        res = math.sqrt(a)
    except ValueError:
        print("Из такого числа квадратный корень не может быть извлечён!")
    else:
        print(f'Квадратный корень из {a} равен {res}.')
