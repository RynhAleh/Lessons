# Написать функцию, которая просит ввести имя и выводит на экран "Привет и введённое имя".
# Далее написать к функции декоратор, который изменяет функцию и переводит имя в заглавные буквы.

def decorator(fun):
    def wrapper(arg: str):
        fun(arg.upper())
    return wrapper


@decorator
def say_hello(your_name: str):
    print("Привет, " + your_name)


say_hello(input("Введите имя: "))
