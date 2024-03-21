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
    def __init__(self,center,radius):
        super().__init__(center)
        self.r = radius

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2*math.pi*self.r

class Square(Shape):
    def __init__(self, center, side_lenth):
        super().__init__(center)
        self.side_lenth = side_lenth

    def area(self):
        return self.side_lenth**2

    def perimeter(self):
        return 4*self.side_lenth

class Isoscele_Triangle(Shape):
    def __init__(self, center, side, height):
        super().__init__(center)
        self.side = side
        self.height = height

    def area(self):
        return self.side * self.height/2

    def circumference(self):
        return 3*self.side

center_point = Point(0, 0)
circle = Circle(center_point, 5)
square = Square(center_point, 4)

print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

print("Square area:", square.area())
print("Square perimeter:", square.perimeter())