# Создайте класс на тему животных. В классе должен присутствовать конструктор не менее трёх методов.

class Animals:
    def __init__(self, name, areal, food, termlife, iscarnivore):   # атрибуты класса
        self.name: str = name                   # наименование
        self.areal: str = areal                 # ареал обитания
        self.food: set = food                   # чем питается (множество)
        self.termlife: int = termlife           # средняя продолж.жизни
        self.iscarnivore: bool = iscarnivore    # хищник или нет

    def return_dict(self) -> dict:                                  # метод класса (возврат словаря)
        return {
                "name": self.name,
                "areal": self.areal,
                "food": self.food,
                "termlife": self.termlife,
                "iscarnivore": self.iscarnivore
                }

    def print_txt(self):                                            # метод класса (вывод на экран)
        print(f' - Это существо называется "{self.name}".\n'
              f' - Ареал обитания: {self.areal}.\n'
              f' - Чем питается: {self.food}.\n'
              f' - Средн.продолж.жизни, лет: {self.termlife}.\n'
              f' - Хищник: {self.iscarnivore}.'
              )

    def change_areal(self):                                         # метод класса (изменение атрибута)
        self.areal = input(f'{self.name}: введите новый ареал обитания (был "{self.areal}"): ')


obj_1 = Animals("Медведь", "Лес", ("Орехи", "Ягоды", "Коренья", "Мясо", "Рыба",), 25, True)
obj_2 = Animals("Голубой кит", "Океан", ("Моллюски",), 55, False)
obj_3 = Animals("Cуслик", "Степь", ("Трава", "Просо", "Горох",), 2, False)

my_dict = obj_1.return_dict()                                       # вызов метода класса (возврат словаря) и присвоение переменной
print(type(my_dict), my_dict, '\n')                                 # вывод на экран типа и содержимого этой переменной

obj_2.print_txt()                                                   # вызов метода класса (вывод на экран)

print()
print(obj_3.return_dict())                                          # вызов метода класса (возврат словаря) и вывод на экран
obj_3.change_areal()                                                # вызов метода класса (изменение атрибута)
print(obj_3.return_dict())                                          # вызов метода класса (возврат словаря) и вывод на экран

# Output:
"""
<class 'dict'> {'name': 'Медведь', 'areal': 'Лес', 'food': ('Орехи', 'Ягоды', 'Коренья', 'Мясо', 'Рыба'), 'termlife': 25, 'iscarnivore': True} 

 - Это существо называется "Голубой кит".
 - Ареал обитания: Океан.
 - Чем питается: ('Моллюски',).
 - Средн.продолж.жизни, лет: 55.
 - Хищник: False.

{'name': 'Cуслик', 'areal': 'Степь', 'food': ('Трава', 'Просо', 'Горох'), 'termlife': 2, 'iscarnivore': False}
Cуслик: введите новый ареал обитания (был "Степь"): Поле
{'name': 'Cуслик', 'areal': 'Поле', 'food': ('Трава', 'Просо', 'Горох'), 'termlife': 2, 'iscarnivore': False}
"""
