# Написать функцию, которая просит ввести имя и выводит на экран "Привет и введённое имя".
# Далее написать к функции декоратор, который изменяет функцию и переводит имя в заглавные буквы.

def decorator(fun):
    def wrapper(arg):
        arg = "ОЛЕГ"
        return fun(arg)
    return wrapper


@decorator
def say_hello(your_name):
    return "Привет, " + your_name


print(say_hello("Олег"))