# Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа.

old_list = list(input("Введите текст: "))
new_list = []
for elem in old_list:
    if not(elem in new_list):
        new_list.append(elem)
new_tuple = tuple(new_list)
print(new_tuple)
