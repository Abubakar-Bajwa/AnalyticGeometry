import math
from Point import *


class Line:
    p1 = Point(0, 0)
    p2 = Point(0, 0)

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.length = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
     #   self.slope = (self.p2.y - self.p1.y)/(self.p2.x-self.p1.x)

    def setLength(self):
        self.length = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def getLength(self):
        return self.length
    
    def getMidpoint(self):
        middle = ((self.p1.x+self.p2.x)/2,(self.p1.y+self.p2.y)/2)
        return middle


    def getSlope(self):
        return (self.p2.y - self.p1.y)/(self.p2.x-self.p1.x)
    
    def setSlope(self):
        self.slope = (self.p2.y - self.p1.y)/(self.p2.x-self.p1.x)

    def isParallel(self,line):
        
        if self.getSlope() == line.getSlope():
            return True

        else:
            return False

    def toString(self):
        
        return f"{(self.p1.x, self.p1.y)} to {(self.p2.x, self.p2.y)}"
               
    