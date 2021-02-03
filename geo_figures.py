from math import sqrt
from math import pi


class GeoFigures:
    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass

    def add_area(self, some_figure):
        try:
            figure_name = some_figure.name
        except AttributeError:
            return 'ошибка, введите фигуру'
        if figure_name not in ["triangle", "rectangle", "square", "circle"]:
            return 'ошибка, введите фигуру, являющуюся объектом классов Triangle, Rectangle, Square, Circle'
        else:
            return round((self.area + some_figure.area), 2)


class Triangle(GeoFigures):
    def __init__(self, a, b, c):
        self.name = "triangle"
        self.angles = 3
        self.a = abs(a)
        self.b = abs(b)
        self.c = abs(c)
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        calc_area = sqrt(
            self.perimeter * (self.perimeter - self.a) * (self.perimeter - self.b) * (self.perimeter - self.c))
        return round(calc_area, 2)


class Rectangle(GeoFigures):
    def __init__(self, a, b):
        self.name = "rectangle"
        self.angles = 4
        self.a = abs(a)
        self.b = abs(b)
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        return round((self.a + self.b) * 2, 2)

    def calculate_area(self):
        return round(self.a * self.b, 2)


class Square(GeoFigures):
    def __init__(self, a):
        self.name = "square"
        self.angles = 4
        self.a = abs(a)
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        return round(self.a * 4, 2)

    def calculate_area(self):
        return round(self.a ** 2, 2)


class Circle(GeoFigures):
    def __init__(self, r):
        self.name = "circle"
        self.angles = 0
        self.r = abs(r)
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        return round(2 * pi * self.r, 2)

    def calculate_area(self):
        return round(pi * self.r ** 2, 2)
