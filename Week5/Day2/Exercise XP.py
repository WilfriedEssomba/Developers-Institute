class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    pass


b1 = Bengal('lulu', 3)
c1 = Chartreux('bobo', 7)
s1 = Siamese('toto', 12)
all_cats = [b1, c1, s1]
sara_pets = Pets(all_cats)
sara_pets.walk()


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        x = self.weight / self.age * 10
        print(f"the running speed of {self.name} is {x}m/s")

    def fight(self, other_dog):
        if ((self.weight / self.age * 10) * self.weight) > ((other_dog.weight / other_dog.age * 10) * other_dog.weight):
            print(f"the winner is {self.name}")
        else:
            print(f"the winner is {other_dog.name}")


my_dog = Dog('sara', 1, 100)
your_dog = Dog('bob', 3, 20)
zaza_dog = Dog('zeze', 2, 46)
your_dog.fight(my_dog)
