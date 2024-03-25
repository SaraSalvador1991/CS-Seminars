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
    def set_weight(self, weight):
        self.weight = weight

    #def # gravity center

# callback pattern, design pattern most powerful
#user form class SensorObs, with a function getData(), Sensor class (with function set_observe(SensorObs). Sensor S, s.setObserver(self), getData()
# make a temperature sensor, giving back the data when it changes temperature of 5 degrees (random values)

class Circle(Shape):
    def __init__(self,center:Point,radius):
        super().__init__(center)
        self.r = radius

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2*math.pi*self.r

class Square(Shape):
    def __init__(self, center:Point, side_lenth):
        super().__init__(center)
        self.side_lenth = side_lenth

    def area(self):
        return self.side_lenth**2

    def perimeter(self):
        return 4*self.side_lenth

class Triangle(Shape):
    def __init__(self, center:Point, side, height):
        super().__init__(center)
        self.side = side
        self.height = height

    def area(self):
        return self.side * self.height/2

    def circumference(self):
        return 3*self.side

if __name__ == '__main__':

    center_point = Point(0, 0)
    circle = Circle(center_point, 5)
    square = Square(center_point, 4)

    print("Circle area:", circle.area())
    print("Circle perimeter:", circle.perimeter())

    print("Square area:", square.area())
    print("Square perimeter:", square.perimeter())