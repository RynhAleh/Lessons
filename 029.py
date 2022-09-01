dict1 = {
    "dog": "собака",
    "cat": "кошка",
    "table": "стол",
    "house": "дом",
    "sun": "солнце",
    "sky": "небо",
}

str1 = input("Введите слово: ")
for key, val in dict1.items():
    if str1 == key:
        print(val)
        break
    elif str1 == val:
        print(key)
        break
else:
    print("В нашем словаре такого слова нет!")
