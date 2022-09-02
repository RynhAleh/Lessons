# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество символов и слов в ней.

ls = []
cnt = words = symbs = 0
with open("file_001.txt", "r", encoding="utf-8") as file:
    for line in file:
        tx = line.replace("\n", "").replace(" – ", " ").replace(" - ", " ")
        ls = tx.split(" ")
        symbs = len(tx)
        words = len(ls)
        cnt += 1
        print(f'(символов:{str(symbs).rjust(4)}, слов:{str(words).rjust(3)}) {line}', end='')
    print(f'Всего строк: {cnt}')
