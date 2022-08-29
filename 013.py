# Вывести на экран ряд натуральных чисел от минимума до максимума с шагом.
# Например, если минимум 10, максимум 35, шаг 5, то вывод должен быть таким: 10 15 20 25 30 35.
# Минимум, максимум и шаг указываются пользователем (считываются с клавиатуры).
try:
    v = [
        int(input("Введите минимум: ")),
        int(input("Введите максимум: ")),
        int(input("Введите шаг: "))
    ]
except ValueError:
    print("Ввёденное значение не являются натуральным числом!")
else:
    if v[0] >= v[1]:
        print("Минимум должен быть меньше максимума!")
    else:
        res = ""
        while v[0] <= v[1]:
            res = res + str(v[0]) + " "
            v[0] += v[2]
        print(res)
