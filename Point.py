import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (x, y)

    def distanceFrom(self, point):
        dist = math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        return dist

    def distanceFromOrigin(self):
        dist = math.sqrt((self.x - 0) ** 2 + (self.y - 0) ** 2)
        return dist

    def equals(self, point):
        if self.x == point.x and self.y == point.y:
            return True
        return False

    def getXvalue(self):
        return self.x

    def getYvalue(self):
        return self.y

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.position = (x, y)

    def toString(self):
        return f"{self.position}"
