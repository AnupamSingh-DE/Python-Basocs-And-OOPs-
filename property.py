# @property decorator

class Rectangle:
    def __init__(self,length,breadth):
        self._length = length            # _ makes the attributes private
        self._breadth = breadth          # _ makes the attributes private

    @property
    def breadth(self):
        return f"{self._breadth:.1f}cm"

    @property
    def length(self):
        return f"{self._length:.1f}cm"

    @breadth.setter
    def breadth(self,new_breadth):
        if new_breadth > 0:
            self._breadth = new_breadth
        else:
            print("New Breadth should be greater than ZERO")

    @length.setter
    def length(self,new_length):
        if new_length > 0 :
            self._length = new_length
        else:
            print("Height should be greater than ZERO")


rectangle = Rectangle(6,5)


rectangle.breadth = 9
print(rectangle.length)
print(rectangle.breadth)