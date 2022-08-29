a = input("Введите возраст (1-99): ")
try:
    a = int(a)
except Exception as ex:
    print("Введенное значение не является числом!")
else:
    if a < 1 or a > 99:
        print("Введенный вами возраст выходит за рамки 1-99!")
    else:
        if 10 < a < 15:
            years = "лет"
        elif str(a)[-1:] in ["2", "3", "4"]:
            years = "года"
        elif str(a)[-1:] == "1":
            years = "год"
        else:
            years = "лет"
        print(f'Мне {a} {years}.')
