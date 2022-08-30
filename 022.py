# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.
import random

# Заполнение списка случайной размерностью (от 10 до 20) случайными значениями (от 0 до 200)
spis = []
for i in range(random.randint(10, 20)):
    spis.append(random.randint(0, 200))
print(f'Сгеренирован случайный список {spis}')

# Запрос параметров
try:
    mn = int(input("Интервал с:  "))
    mx = int(input("Интарвал по: "))
except ValueError:
    print("Ввёденное значение не являются целым числом!")
else:
    if mx < mn:
        print('"Интервал с" должен быть больше "Интервала по"!')
    else:
        # перебор списка, удаление неугодных элементов, вставка вместо них нулей в конец
        for i in spis:
            if i in range(mn, mx+1):
                spis.remove(i)
                spis.append(0)
        print(f'Список после обработки        {spis}')