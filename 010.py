# Известны год, номер месяца и день рождения каждого из двух человек. Определить, кто из них старше.
import datetime

try:
    dbirth1 = (
        int(input("Введите год рождения 1-го человека: ")),
        int(input("Введите месяц рождения 1-го человека: ")),
        int(input("Введите число месяца рождения 1-го человека: "))
    )
    dbirth2 = (
        int(input("Введите год рождения 2-го человека: ")),
        int(input("Введите месяц рождения 2-го человека: ")),
        int(input("Введите число месяца рождения 2-го человека: "))
    )

except ValueError:
    print("Ввёденное значение не являются числом!")
else:
    try:
        dbr1 = datetime.date(dbirth1[0], dbirth1[1], dbirth1[2])
        dbr2 = datetime.date(dbirth2[0], dbirth2[1], dbirth2[2])
    except Exception as ex:
        print(ex)
    else:
        if dbr1 < dbr2:
            print(f'Первый человек старше второго на {dbr2 - dbr1}')
        else:
            print(f'Второй человек старше первого на {dbr1 - dbr2}')
