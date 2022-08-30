# Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа.

my_tuple = tuple(input("Введите текст: "))
my_list = []
for elem in my_tuple:
    if not(elem in my_list):
        my_list.append(elem)
print(tuple(my_list))
