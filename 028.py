def _ask_(txt: str) -> str:
    while True:
        right = True
        list1 = txt.split(" ")
        for i in list1:
            if not i.isdigit():
                print("Вы должны вводить только числа!")
                right = False
                break
        if right:
            return f'{list1}\n{tuple(list1)}'


print(_ask_(input("Введите последовательность чисел, разделенных пробелами: ").strip()))
