import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, center: Point):
        self.center = center

    def circumference(self):
       pass

    def area(self):
        pass

class Circle(Shape):
    def __int__(self,center,radius):
        super().__int__(center)
        self.r = radius

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2*math.pi*self.radius

class Square(Shape):
    def __int__(self, center, side_lenth):
        super().__int__(center)
        self.side_lenth = side_lenth

    def area(self):
        return self.side_lenth**2

    def perimeter(self):
        return 4*self.side_lenth