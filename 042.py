# Создать класс и вызвать пять объектов этого класса.

class Cars:
    def __init__(self, brand, name, power, color, price):           # атрибуты класса
        self.brand: str = brand
        self.name: str = name
        self.power: int = power
        self.color: str = color
        self.price: int = price

    def output_dict(self):                                          # метод класса
        print({"brand": self.brand,
               "name": self.name,
               "power": self.power,
               "color": self.color,
               "price": self.price}
              )

    def output_txt(self):                                           # метод класса
        print(f' - Это автомобиль {self.brand} {self.name}.\n'
              f' - Его мощность {self.power} л.с.\n'
              f' - Цвет - {self.color}.\n'
              f' - Цена: ${self.price}.'
              )


obj_1 = Cars("Рено", "Дастер", 149, "черный", 19500)
obj_2 = Cars("Ниссан", "Кашкай", 163, "серебристый", 22000)
obj_3 = Cars("Хендай", "Акцент", 138, "серый", 16700)
obj_4 = Cars("Киа", "Рио", 138, "красный", 16400)
obj_5 = Cars("Фольксваген", "Поло", 125, "синий", 17100)

obj_1.output_dict()                                                 # вызов метода класса
obj_2.output_txt()                                                  # вызов метода класса
print(f'(!) {obj_3.brand} {obj_3.name}'                             # вызов атрибутов класса
      f'{"не " if obj_3.price <= obj_4.price else ""}'              # вызов атрибутов класса
      f'дороже, чем {obj_4.brand} {obj_4.name}')                    # вызов атрибутов класса
print(f'>>> Я бы взял {obj_5.brand} {obj_5.name} {obj_5.color}.')   # вызов атрибутов класса
