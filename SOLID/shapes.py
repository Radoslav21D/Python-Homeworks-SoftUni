from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle:
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def calc_area(self):
        return self.side * self.height / 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return pi * self.radius * self.radius


# RectanglesAreaCalculator не го променяме!!!
class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()
        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Triangle(6, 2), Circle(4)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
