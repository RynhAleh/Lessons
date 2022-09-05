# Написать функцию, которая просит ввести имя и выводит на экран "Привет и введённое имя".
# Далее написать к функции декоратор, который изменяет функцию и переводит имя в заглавные буквы.

def decorator(fun):
    # Ниже вместо аргументов wrapper используется _, так как планируется заменить аргументы своими.
    # Установление явных (your_name) или неявных (*args) вызвало бы предупреждение IDE Parameter '...' value is not used
    def wrapper(_):
        return fun("ОЛЕГ")
    return wrapper


@decorator
def say_hello(your_name):
    return "Привет, " + your_name


print(say_hello("Олег"))
