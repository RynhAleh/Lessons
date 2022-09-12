"""
class Figure(object):
    def __init__(self, color, nodes):
        self.color: str = color
        self.nodes: int = nodes

    def f_type(self) -> str:
        if self.nodes < 3:
            return "such a figure cannot exist"
        else:
            return str(self.nodes) + "-square"

    def f_nodes(self) -> int:
        return self.nodes


class Triangle(Figure):
    def __init__(self, color, side_1: float, side_2: float, side_3: float, nodes: int = 3):
        super().__init__(color, nodes)
        self.side_1: float = side_1
        self.side_2: float = side_2
        self.side_3: float = side_3

    def squar(self) -> float:
        pp = (self.side_1 + self.side_2 + self.side_3) / 2                          # вычисляем полупериметр, далее
        return abs(pp * (pp-self.side_1) * (pp-self.side_2) * (pp-self.side_3)) ** 0.5  # площадь треугольника вычисляется по трем сторонам по формуле Герона


class Javatpoint:
    volume = 25

    def __init__(self, age=0):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, a):
        self._age = a


John = Javatpoint()
John.set_age(19)
John.age = 18
John.volume = 312

# using the getter function
print(John.get_age())
print(John.age)
print(John.volume)


if __name__ == "__main__":
    fg_1 = Figure("blue", 2)
    print(f'Nodes: {fg_1.f_nodes()}.')
    print(f'Type: {fg_1.f_type()}')

    tr_1 = Triangle("red", 1.5, 6.3, 4.5)
    tr_1.nodes = 5
    fg_1.nodes = 9
    print(f'Nodes (fg): {fg_1.nodes}.')
    print(f'Nodes (tr): {tr_1.nodes}.')
    print(f'Type: {tr_1.f_type()}')
    print(f'Color: {tr_1.color}')
    print(f'Side A: {tr_1.side_1}')
    print(f'Side B: {tr_1.side_2}')
    print(f'Side C: {tr_1.side_3}')
    print(f'Square: {tr_1.squar()}.')
"""

"""
# исследуем обычные методы
class Car:
    var_1 = 1                       # var_1 статический атрибут

    def __init__(self, var_2):      # var_2 динамический атрибут
        self.var_2 = var_2

    def sm1(self, var_3):           # var_3 аргумент метода sm1
        return var_3 + self.var_2

    def sm2(self):
        return self.var_1 + self.var_2


f = Car(9)
print(f.sm1(6))
print(f.sm2())
"""

"""
class Car:
    var_1 = 1                       # var_1 статический атрибут

    def __init__(self, var_2):      # var_2 динамический атрибут
        self.var_2 = var_2

    @staticmethod
    def sm1(var_3):                 # var_3 аргумент метода sm1
        return var_3 ** 2           # если @staticmethod, нельзя обратиться ни к var_1, ни к var_2

    def sm2(self):
        return self.var_1 + self.var_2


f = Car(9)
print(f.sm1(6))
print(f.sm2())
"""


class Animal:
    def about1(self) -> str:                  # к __about1() имеют доступ как объекты родителя Animal, так и объекты потомка Dog
        return "Это - " + self.__info()       # __info() используется только внутри класса

    @staticmethod
    def __info() -> str:                      # __info() не может вызываться извне
        return "живое существо"


class Dog(Animal):
    def about2(self) -> str:                  # к __about2() имеют доступ объекты потомка Dog
        return "Собака " + self.__whatdoes()  # __whatdoes() используется только внутри класса

    @staticmethod
    def __whatdoes() -> str:
        return "лает"


st1 = Animal()
st2 = Dog()
print(f'Animal: {st1.about1()}')              # вызов через экземпляр Animal обычного метода класса Animal
print()
print(f'Dog: {st2.about1()}')                 # вызов через экземпляр Dog обычного метода класса-предка Animal
print(f'Dog: {st2.about2()}')                 # вызов через экземпляр Dog обычного метода класса Dog
print(f'Animal: {st1.__info()}')              # попытка вызова через экземпляр Animal приватного метода класса Animal
"""AttributeError: 'Animal' object has no attribute '__info'"""
