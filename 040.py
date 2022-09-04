# Найти сумму цифр числа с помощью рекурсии. 112 = 4

def sum_digits(n: int) -> int:
    if n == 0:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


print(sum_digits(112))
