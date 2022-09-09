# В класс из предыдущего урока добавьте три класса-наследника на ваше усмотрение.
from Anim.anim import Animals


class Dog(Animals):
    def __init__(self, breed, diff, name="Собака", areal="Где человек", food="Мясо, злаки, овощи", termlife=15, iscarnivore=True):
        super().__init__(name, areal, food, termlife, iscarnivore)
        self.breed: str = breed
        self.diff: tuple = diff


class Bird(Animals):
    def __init__(self, subname, isflying, areal, food, termlife, iscarnivore, name="Bird"):
        super().__init__(name, areal, food, termlife, iscarnivore)
        self.subname: str = subname
        self.isflying: bool = isflying


class Fish(Animals):
    def __init__(self, subname, in_salt_water, areal, food, termlife, iscarnivore, name="Рыба"):
        super().__init__(name, areal, food, termlife, iscarnivore)
        self.subname: str = subname
        self.in_salt_water: bool = in_salt_water
        self.termlife: str = termlife


obj_1 = Dog("Той-терьер", "Маленькая и лиловая")
print(f'Средняя продолжительность жизни собаки породы {obj_1.breed}: {obj_1.termlife}. '
      f'Ее отличия: {obj_1.diff}')
print(f'Данные класса-родителя определены в классе-наследнике: '
      f'Наименование - {obj_1.name}, '
      f'ареал обитания - {obj_1.areal}, '
      f'пища - {obj_1.food}.\n')

obj_2 = Bird("Пингвин", False, "Южный полюс", "Рыба", 20, True)
print(f'Средняя продолжительность жизни пингвина: {obj_2.termlife}. '
      f'Может ли летать: {obj_2.isflying}')
print(f'Данные класса-родителя определены в классе-наследнике: '
      f'Наименование - {obj_2.name}, '
      f'ареал обитания - {obj_2.areal}, '
      f'пища - {obj_2.food}.\n')

obj_3 = Fish("Касатка", True, "Океан", "Другая рыба", 50, True)
print(f'Средняя продолжительность жизни касатки: {obj_3.termlife}. '
      f'В соленой ли воде: {obj_3.in_salt_water}')
print(f'Данные класса-родителя определены в классе-наследнике: '
      f'Наименование - {obj_3.name}, '
      f'ареал обитания - {obj_3.areal}, '
      f'пища - {obj_3.food}.')
