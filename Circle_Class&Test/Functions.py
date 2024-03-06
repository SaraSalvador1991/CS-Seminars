from Circle_Class import Circle
import math
import numpy
def compute_intersection(c1:Circle, c2:Circle):
    dist = ((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2) ** 0.5
    if dist <= c1.r - c2.r:
        return f"Circle 2 is inside circle 1"
    elif dist <= c2.r - c1.r:
        return f"Circle 1 is inside circle 2"
    elif dist < c1.r + c2.r:
        return f"The two circles intersect in two points"
    elif dist == c1.r + c2.r:
        return "The two circles intersect in one point"
    else:
        return "The two circles do not intersect"


def get_intersection(c1:Circle, c2:Circle):
    dist = ((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2) ** 0.5

    if dist <= c1.r - c2.r:
        return f"There is not intersection point(s)"
    elif dist <= c1.r - c2.r:
        return f"There is not intersection point(s)"
    elif dist < c1.r + c2.r:

        a = (c1.r ** 2 - c2.r ** 2 + dist ** 2) / (2 * dist)
        h = math.sqrt(c1.r ** 2 - a ** 2)
        x2 = c1.x + a * (c2.x - c1.x) / dist
        y2 = c1.y + a * (c2.y - c1.y) / dist
        x3 = x2 + h * (c2.y - c1.y) / dist
        y3 = y2 - h * (c2.x - c1.x) / dist

        x4 = x2 - h * (c2.y - c1.y) / dist
        y4 = y2 + h * (c2.x - c1.x) / dist

        I1 = (x3, y3)
        I2 = (x4, y4)

        return f"The intersection points are {I1} and {I2}"

    elif dist == c1.r + c2.r:
        a = (c1.r ** 2 - c2.r ** 2 + dist ** 2) / (2 * dist)
        h = math.sqrt(c1.r ** 2 - a ** 2)
        x2 = c1.x + a * (c2.x - c1.x) / dist
        y2 = c1.y + a * (c2.y - c1.y) / dist
        x3 = x2 + h * (c2.y - c1.y) / dist
        y3 = y2 - h * (c2.x - c1.x) / dist

        I = (x3, y3)

        return f"The intersection point is {I}"

    else:
        return f"There is not intersection point(s)"


def Area (c:Circle):
    return round(numpy.pi * c.r ** 2, 3)


def Circumference(c:Circle):
    return round(2*numpy.pi*c.r,3)