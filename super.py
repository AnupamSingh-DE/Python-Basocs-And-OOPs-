#Testing Super Class

class shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
class Circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius
class Rectangle(shape):
    def __init__(self, color, is_filled, width, length):
        super().__init__(color, is_filled)
        self.width = width
        self.length = length
class Triangle(shape):
    def __init__(self, color, is_filled, width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

circle  = Circle("Yellow",True,"20cm")

print(circle.color)
circle.describe()
