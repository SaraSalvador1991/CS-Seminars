import numpy

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Shape:
    def __init__(self, center: Point):
        self.center = center
        self.x = self.center.x
        self.y = self.center.y

    def circumference(self):
        return round(2 * numpy.pi * self.r, 3)  # write empy circumference
#write test for this

class Circle(Shape):
    def __init__(self, radius, x, y):
        c = Point(x, y)
        super().__init__(c)
        self.r = float(radius)
    def circumference(self):

        return round(2 * numpy.pi * self.r, 3)

class Square(Shape):
    def __init__(self):

# circle and square. in common: a center
#uml
# class circle and class square
# common class could be shape