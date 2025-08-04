#Polymorphism

from abc import ABC, abstractmethod




class Shape:
    def area(self):
        pass


class Circle(Shape): #its a circle and a shape
    def __init__(self,radius):
        self.radius  = radius

    def area(self):
        return 3.14 * pow(self.radius,2)

class Rectangle(Shape): #its a rectangle and a shape
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class Triangle(Shape): #its a triangle and a shape
    def __init__(self,height,breadth):
        self.height = height
        self.breadth = breadth

    def area(self):
        return 0.5 * self.height * self.breadth

class Pizza(Circle):         # pizza has three forms its a pizza and circle and a shape
    def __init__(self,toppings,radius):
        super().__init__(radius)
        self.toppings = toppings



Shape = [Circle(4),Rectangle(9,4),Triangle(9,5),Pizza("mushroom",9)]

for shape in Shape:
    print(shape.area())
pizza = Pizza()
print(pizza.toppings)
