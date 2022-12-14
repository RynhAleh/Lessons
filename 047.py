class Animal:
    def __init__(self, group):
        self.group = group

    # метод родителя с тремя значениями по умолчанию (параметры Хищника)
    def what_does(self, whateat="Мясо", howget="Охота", whereget="Лес"):
        print(f'Это животное - {self.group}. '
              f'Как правило, разновидности этого типа едят {whateat}. '
              f'Путь добычи: {howget}. '
              f'Место добычи: {whereget}'
              )


class Cat(Animal):
    def __init__(self, group="Хищник", name="Кот"):
        super().__init__(group)
        self.name = name

    # переопределенный метод с тремя значениями по умолчанию (параметры Кота) - ПОЛИМОРФИЗМ
    def what_does(self, whateat="Мясные блюда", howget="Из миски", whereget="Дома"):
        print(f'Это - {self.name}. '
              f'Разновидность чего - {self.group}. '
              f'Поэтому он ест {whateat}. '
              f'Путь добычи: {howget}. '
              f'Место добычи: {whereget}'
              )


an1 = Animal("Хищник")                                         # создание экземпляра родительского класса
ct1 = Cat()                                                    # создание экземпляра наследуемого класса со значениями по умолчанию
an1.what_does()                                                # вызов метода родительского класса со значениями по умолчанию
ct1.what_does()                                                # вызов переопределенного метода наследуемого класса со значениями по умолчанию (ПОЛИМОРФИЗМ)
ct2 = Cat("Хищник", "Дикий кот")                               # создание экземпляра наследуемого класса с заданными значениями
ct2.what_does("Мясо", "Охота (т.к.дикий)", "Лес (т.к.дикий)")  # вызов переопределенного метода наследуемого класса с заданными значениями (ПОЛИМОРФИЗМ)

"""
Это животное - Хищник. Как правило, разновидности этого типа едят Мясо. Путь добычи: Охота. Место добычи: Лес
Это - Кот. Разновидность чего - Хищник. Поэтому он ест Мясные блюда. Путь добычи: Из миски. Место добычи: Дома
Это - Дикий кот. Разновидность чего - Хищник. Поэтому он ест Мясо. Путь добычи: Охота (т.к.дикий). Место добычи: Лес (т.к.дикий)
"""
