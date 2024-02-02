import math
from Point import *


class Circle:
    point = Point(0, 0)
    
    def __init__(self, radius=0, point=(0, 0)):
        self.radius = radius
        self.point = point
        self.area = math.pi * self.radius ** 2
        self.circumference = 2 * math.pi * self.radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getCircumference(self):
        return 2 * math.pi * self.radius

    def getRadius(self):
        return self.radius

    def isPointInside(self, point):
        if self.point.distanceFrom(point) >= self.radius:
            return False
        else:
            return True

    def setArea(self):
        self.area = math.pi * self.radius ** 2

    def setCircumference(self):
        self.circumference = 2 * math.pi * self.radius

    def setLocation(self, point):
        self.point = point

    def setRadius(self, r):
        self.radius = r

    def toString(self):
        return (f"Circle Radius: {self.radius}"
                f" the centre is: {(self.point.x, self.point.y)}")







