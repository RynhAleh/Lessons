from abc import abstractmethod


class Animal:
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Кот бегает")

    def eat(self):
        print("Кот ест")

    def sleep(self):
        print("Кот спит")


ct1 = Cat()
ct1.run()
ct1.eat()
ct1.sleep()
