# Есть пятизначное натуральное число. Найдите его наибольшую цифру.
# Например: введено число 76458, наибольшая цифра в нём 8.
try:
    a = int(input("Введите пятизначное натуральное число: "))
except ValueError:
    print("Ввёденное значение не являются натуральным числом!")
else:
    if a <= 0:
        print("Ввёденное значение не являются натуральным числом!")
    elif not (9999 < a < 100000):
        print("Ввёденное число не являются пятизначным!")
    else:
        print(f'Максимальная цифра в числе {a} - {max(str(a))}.')
