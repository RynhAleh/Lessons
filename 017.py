# Вычислить факториал введённого числа.


try:
    a = int(input("Введите натуральное число: "))
except ValueError:
    print("Ввёденное значение не является натуральным числом!")
else:
    if a <= 0:
        print("Ввёденное значение меньше нуля!")
    else:
        fact = 1
        for i in range(1, a + 1):
            fact *= i
        print(f'Факториал числа {a} равен {fact}.')
