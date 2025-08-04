#Multiple Inheritance

class prey:

    def __init__(self,name ,type):
        self.name = name
        self.type = type

    def flee(self):
        print("You have to flee")
    def sleep(self):
        print("Animal is sleeping")

    def eat(self):
        print("Animal is eating")

class preditor:
    def hunt(self):
        print("You have to hunt")

    def sleep(self):
        print("Animal is sleeping")
class Rabbit(prey):
    pass

class Hawk(preditor):
    pass

class Fish(prey, preditor):
    pass

rabbit = Rabbit("Whitey","dove")

print(rabbit.name)
print(rabbit.type)
hawk = Hawk()
fish = Fish("nemo","goldenfish")
print(fish.name)
print(fish.type)

rabbit.flee()
rabbit.eat()
rabbit.sleep()
hawk.hunt()
fish.flee()
fish.hunt()
