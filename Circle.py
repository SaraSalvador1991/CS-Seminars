import numpy
import matplotlib.pyplot as plt

class Circle:
    def __init__(self,radius1,radius2, center1_x, center1_y, center2_x, center2_y,theta):  ## theta in rad
        self.r1 = float(radius1)
        self.r2 = float(radius2)
        self.c1x = float(center1_x)
        self.c1y = float(center1_y)
        self.c2x = float(center2_x)
        self.c2y = float(center2_y)
        self.t = float(theta)

    def Circumference(self):            #funtion that calculate the circumference of a circle of radius r
        return round(2*numpy.pi*self.r1,3)

    def Area(self):            # function that calculate the area of a circle of radius r
        return round(numpy.pi*self.r1,3)

    def Circumference_Sector(self):
        return self.r1 * self.t
    def Area_Sector(self):
        return round(self.r1**2/2*self.t,3)

    def Intersect(self):
        dist = ((self.c1x-self.c2x)**2+(self.c1y-self.c2y)**2)**0.5
        if dist <= self.r1 - self.r2:
            return("Circle 2 is inside circle 1")
        elif dist <= self.r2 - self.r1:
            return ("Circle 1 is inside circle 2")
        elif dist < self.r1 + self.r2:
            return ("The two cricles intersect")
        elif dist == self.r1 + self.r2:
            return ("The two circles intersect in one point")
        else:
            return ("The two circles do not interect")

    def Graphic_prove(self):

        from matplotlib.patches import Circle

        plt.axis([-10, 10, -10, 10])
        plt.axis("equal")
        c1 = (self.c1x,self.c1y)
        c2 = (self.c2x,self.c2y)
        circle1 = Circle(c1, self.r1, fill=False)
        circle2 = Circle(c2, self.r2, fill=False)

        plt.gca().add_artist(circle1)
        plt.gca().add_artist(circle2)
        plt.show()

# ----------------------------------------

c=Circle(1.8,4,0,0,5,3,1.5708)
print(c.Circumference())
print(c.Area())
print(c.Circumference_Sector())
print(c.Area_Sector())
print(c.Intersect())
c.Graphic_prove()










