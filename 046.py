# В классе из предыдущего урока приведите пример инкапсуляции.

class Animal:
    def about1(self) -> str:                  # к __about1() имеют доступ как объекты родителя Animal, так и объекты потомка Dog
        return "Это - " + self.__info()       # __info() используется только внутри класса (ИНКАПСУЛЯЦИЯ)

    @staticmethod
    def __info() -> str:                      # __info() не может вызываться извне (ИНКАПСУЛЯЦИЯ)
        return "живое существо"


class Dog(Animal):
    def about2(self) -> str:                  # к __about2() имеют доступ объекты потомка Dog
        return "Собака " + self.__whatdoes()  # __whatdoes() используется только внутри класса (ИНКАПСУЛЯЦИЯ)

    @staticmethod
    def __whatdoes() -> str:                  # __whatdoes() не может вызываться извне (ИНКАПСУЛЯЦИЯ)
        return "лает"


st1 = Animal()
st2 = Dog()
print(f'Animal: {st1.about1()}')              # вызов через экземпляр Animal обычного метода класса Animal
print()
print(f'Dog: {st2.about1()}')                 # вызов через экземпляр Dog обычного метода класса-предка Animal
print(f'Dog: {st2.about2()}')                 # вызов через экземпляр Dog обычного метода класса Dog
print(f'Animal: {st1.__info()}')              # попытка вызова через экземпляр Animal приватного метода класса Animal
"""
AttributeError: 'Animal' object has no attribute '__info'
Область видимости методов __info() и __whatdoes() - только внутри соответствующих классов. 
"""
