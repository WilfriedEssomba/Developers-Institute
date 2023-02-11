class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


f1 = Cat('minou', 14)
f2 = Cat('pussy', 6)
f3 = Cat('ruru', 2)


def oldest():
    if f1.age > f2.age and f1.age > f3.age:
        print(f"the oldest is {f1.name} and is {f1.age} years ")
    elif f2.age > f3.age:
        print(f"the oldest cat is {f2.name} and is {f2.age} years")
    else:
        print(f"the oldest cat  is {f3.name} and is {f3.age} years")


oldest()


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x}cm")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def smas(self):
        for i in self.lyrics:
            print(i)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.smas()
list1 = ["kugf", "tkuf"]
list1.pop(0)
print(list1)