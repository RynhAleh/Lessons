# 2. Известны год, номер месяца и день рождения человека, а также день, год и номер месяца сегодняшнего дня.
# Определите возраст человека (число полных лет).
import datetime

td = datetime.date.today()
today = (td.year, td.month, td.day)
try:
    dbirth = (
        int(input("Введите год рождения: ")),
        int(input("Введите месяц рождения: ")),
        int(input("Введите число месяца рождения: "))
    )
except ValueError:
    print("Ввёденное значение не являются числом!")
else:
    try:
        dbr = datetime.date(dbirth[0], dbirth[1], dbirth[2])
    except Exception as ex:
        print(ex)
    else:
        res = td - dbr
        if td < dbr:
            print("Вы ввели дату больше текущей!")
        else:
            print(f'Возраст человека: {res}.')
