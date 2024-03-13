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

def Area (c:Circle):
    return round(numpy.pi * c.r ** 2, 3)

def Circumference(c:Circle):
    return round(2*numpy.pi*c.r,3)