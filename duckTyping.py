#Duck Typing

class Animals:
    alive = True

class Dog(Animals):
    def speak(self):
        print("Woof!")

class Cat(Animals):
    def speak(self):
        print("Meow!")

class Car:
    alive = False
    def speak(self):
        print("PeeP!")

Animals = [Dog(),Cat(),Car()]

for animal in Animals:
    animal.speak()
    print(animal.alive)

# car = Car()
#
# print(car.horn())