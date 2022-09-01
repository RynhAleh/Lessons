# 1. В текстовый файл построчно записаны фамилия и имя каждого учащегося класса и их оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов, и посчитать средний балл по классу.

list1, list2 = [], []

with open("pupils.txt", "r") as f:
    for i in f:
        list1.append(i.split())

sm = ct = 0
for elem in list1:
    sm += int(elem[2])
    ct += 1
    if int(elem[2]) < 3:
        list2.append(f'{elem[0]} {elem[1]}')

print(f'Средний балл: {sm / ct}')
print(f'Ученики с оценками ниже 3 баллов: {list2}')
