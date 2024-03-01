import math

import numpy
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, radius, theta):  ## theta in rad
        self.r = float(radius)
        self.t = float(theta)

    def Circumference(self):            # funtion that calculate the circumference of a circle of radius r
        return round(2*numpy.pi*self.r,3)

    def Area(self):            # function that calculate the area of a circle of radius r
        return round(numpy.pi*self.r**2,3)

    def Circumference_Sector(self):
        return self.r * self.t
    def Area_Sector(self):
        return round(self.r**2/2*self.t,3)


class TwoCircles:

    def __init__(self, radius1, radius2, center1_x, center1_y, center2_x, center2_y):  ## theta in rad
        self.r1 = float(radius1)
        self.r2 = float(radius2)
        self.c1x = float(center1_x)
        self.c1y = float(center1_y)
        self.c2x = float(center2_x)
        self.c2y = float(center2_y)

    def Intersect(self):
        dist = ((self.c1x-self.c2x)**2+(self.c1y-self.c2y)**2)**0.5
        if dist <= self.r1 - self.r2:
            print("Circle 2 is inside circle 1 and the area of the intersection is", round(numpy.pi * self.r2 ** 2,3))
        elif dist <= self.r2 - self.r1:
            print("Circle 1 is inside circle 2 and the area of the intersection is", round(numpy.pi * self.r1 ** 2,3))
        elif dist < self.r1 + self.r2:
            d1 = (self.r1**2-self.r2**2+dist**2)/(2*dist)
            d2 = dist -d1
            A_int = self.r1**2*math.acos(d1/self.r1)-d1*(self.r1**2-d1**2)**0.5+self.r2**2*math.acos(d2/self.r2)-d2*(self.r2**2-d2**2)**0.5
            print("The two cricles intersect and the area of the intersection is ", round(A_int,3))
        elif dist == self.r1 + self.r2:
            print("The two circles intersect in one point")
        else:
            print("The two circles do not interect")

    def Graphic_prove(self):

        dist = ((self.c1x - self.c2x) ** 2 + (self.c1y - self.c2y) ** 2) ** 0.5
        if dist <= self.r1 - self.r2:

            import shapely.geometry as sg
            import descartes

            circ1 = sg.Point(self.c1x, self.c1y).buffer(self.r1)
            circ2 = sg.Point(self.c2x, self.c2y).buffer(self.r2)

            # use descartes to create the matplotlib patches
            ax = plt.gca()
            ax.add_patch(descartes.PolygonPatch(circ1, fc='w', ec='k', alpha=0.2))
            ax.add_patch(descartes.PolygonPatch(circ2, fc='b', ec='k', alpha=0.2))

            # control display
            ax.set_xlim(-10, 10);
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal')
            plt.show()

        elif dist <= self.r2 - self.r1:

            import shapely.geometry as sg
            import descartes

            circ1 = sg.Point(self.c1x, self.c1y).buffer(self.r1)
            circ2 = sg.Point(self.c2x, self.c2y).buffer(self.r2)

            # use descartes to create the matplotlib patches
            ax = plt.gca()
            ax.add_patch(descartes.PolygonPatch(circ1, fc='b', ec='k', alpha=0.2))
            ax.add_patch(descartes.PolygonPatch(circ2, fc='w', ec='k', alpha=0.2))

            # control display
            ax.set_xlim(-10, 10);
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal')
            plt.show()
        elif dist < self.r1 + self.r2:

            import shapely.geometry as sg
            import descartes

            circ1 = sg.Point(self.c1x, self.c1y).buffer(self.r1)
            circ2 = sg.Point(self.c2x, self.c2y).buffer(self.r2)

            left = circ1.difference(circ2)
            right = circ2.difference(circ1)
            middle = circ1.intersection(circ2)

            # use descartes to create the matplotlib patches
            ax = plt.gca()
            ax.add_patch(descartes.PolygonPatch(left, fc='w', ec='k', alpha=0.2))
            ax.add_patch(descartes.PolygonPatch(right, fc='w', ec='k', alpha=0.2))
            ax.add_patch(descartes.PolygonPatch(middle, fc='b', ec='k', alpha=0.2))

            # control display
            ax.set_xlim(-10, 10);
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal')
            plt.show()

        elif dist == self.r1 + self.r2:

            import shapely.geometry as sg
            import descartes

            circ1 = sg.Point(self.c1x, self.c1y).buffer(self.r1)
            circ2 = sg.Point(self.c2x, self.c2y).buffer(self.r2)

            # use descartes to create the matplotlib patches
            ax = plt.gca()
            ax.add_patch(descartes.PolygonPatch(circ1, fc='w', ec='k', alpha=0.2))
            ax.add_patch(descartes.PolygonPatch(circ2, fc='w', ec='k', alpha=0.2))

            # control display
            ax.set_xlim(-10, 10);
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal')
            plt.show()

        else:

            import shapely.geometry as sg
            import descartes

            circ1 = sg.Point(self.c1x, self.c1y).buffer(self.r1)
            circ2 = sg.Point(self.c2x, self.c2y).buffer(self.r2)

            # use descartes to create the matplotlib patches
            ax = plt.gca()
            ax.add_patch(descartes.PolygonPatch(circ1, fc='w', ec='k', alpha=0.2))
            ax.add_patch(descartes.PolygonPatch(circ2, fc='w', ec='k', alpha=0.2))

            # control display
            ax.set_xlim(-10, 10);
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal')
            plt.show()

# -------------------------

radius1 = 3
radius2 = 2
center1 = (0,0)
center2= (0,0)

c1 = Circle(radius1, 0.57)
c2 = Circle(radius2, 0.57)

print(c1.Circumference())
print(c1.Area())
print(c1.Circumference_Sector())
print(c1.Area_Sector())

print(c2.Circumference())
print(c2.Area())
print(c2.Circumference_Sector())
print(c2.Area_Sector())

# ----------------------------

Tc= TwoCircles(radius1,radius2,center1[0],center1[1],center2[0], center2[1])

print(Tc.Intersect())
Tc.Graphic_prove()
