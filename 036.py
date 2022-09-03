# Написать функцию, которая генерирует словарь, где ключ - это буква сторки,
# а значение - это число, сколько раз повторяется данная буква этой строке.
# Строку пользователь вводит программно.

def gen_dict(txt: str) -> dict:
    set1 = set(txt)
    list1 = list(txt)
    dict1 = {}
    for i in set1:
        dict1[i] = len(list(filter(lambda x: x == i, list1)))
    return dict1


print(gen_dict(input("Введите строку: ")))
