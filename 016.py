# Вывести на экран столько элементов ряда Фибоначчи, сколько указал пользователь.
# Например, если на ввод поступило число 6, то вывод должен содержать шесть первых чисел ряда Фибоначчи: 1 2 3 5 8 13.


try:
    a = int(input("До какого элемента вывести ряд Фибоначчи: "))
except ValueError:
    print("Ввёденное значение не является натуральным числом!")
else:
    if a <= 0:
        print("Ввёденное значение меньше нуля!")
    else:
        tmp = ""
        fibo = [1, 1, 2]
        while a > 0:
            a -= 1
            fibo = [fibo[1], fibo[2], fibo[1]+fibo[2]]
            tmp = f'{tmp} {fibo[0]}'
        print(tmp)
