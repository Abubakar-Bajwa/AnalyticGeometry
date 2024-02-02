from Circle import *
from Point import *
from Line import *


#defining functions for each testing scenario
def scenarioOne():
    """
    This function was created to mimic the example out for scenario 1 of test
    cases.
        Parameters:
              None
        Returns:
              None
    """
    #declaration, creating instances of objects
    pointOne = Point(2.0, 2.0)
    pointTwo = Point(3.0, 3.0)

    newLine = Line(pointOne, pointTwo)
    newCircle = Circle(2, Point(1.0, 1.0))

    #printing all the statements with embedded object calls
    print("*")
    print("Scenario 1*")
    print("*")
    print("Point 1 is " + pointOne.toString())
    print("Point 2 is " + pointTwo.toString())
    print("Distance of point 1 from origin is: {0:.2f}".format(
        pointOne.distanceFromOrigin()))
    print("Distance of point 2 from origin is: {0:.2f}".format(
        pointTwo.distanceFromOrigin()))
    print("Line " + newLine.toString() +
          " Length: {0:.4f} Slope: {1:.4f}".format(newLine.getLength(),
                                                   newLine.getSlope()))
    print("The mid-point of this line segment p1-p2 is: " +
          str(newLine.getMidpoint()))
    if pointOne.equals(pointTwo):
        print("The 2 Points are the same.")
    else:
        print("The 2 Points are different.")
    print(newCircle.toString())
    print("Area of the circle is {0:.2f}".format(newCircle.getArea()))
    print("Circumference of the circle is {0:.2f}".format(
        newCircle.getCircumference()))
    if newCircle.isPointInside(pointOne):
        print("Point 1 is inside the circle.")
    else:
        print("Point 1 is not inside the circle.")
    if newCircle.isPointInside(pointTwo):
        print("Point 2 is inside the circle.")
    else:
        print("Point 2 is not inside the circle.")
    print(end='\n')


def scenarioTwo():
    """
    This function was created to mimic the example out for scenario 2 of test
    cases.
        Parameters:
              None
        Returns:
              None
    """
    #declaration, creating instances of objects
    pointOne = Point(1.0, 1.0)
    pointTwo = Point(1.0, 1.0)
    newLine = Line(pointOne, pointTwo)
    newCircle = Circle(4, Point(4.0, 0.0))

    #printing all the statements with embedded object calls
    print("*")
    print("Scenario 2*")
    print("*")
    print("Point 1 is " + pointOne.toString())
    print("Point 2 is " + pointTwo.toString())
    if pointOne.equals(pointTwo):
        print("The 2 Points are the same.")
    else:
        print("The 2 Points are different.")
    print("Distance of line segment p1-p2 is: {0:.2f}".format(
        newLine.getLength()))
    print(newCircle.toString())
    print("Area of the circle is {0:.2f}".format(newCircle.getArea()))
    print("Circumference of the circle is {0:.2f}".format(
        newCircle.getCircumference()))
    if newCircle.isPointInside(pointOne):
        print("Point 1 is inside the circle.")
    else:
        print("Point 1 is not inside the circle.")
    print(end='\n')


def scenarioThree():
    """
    This function was created to mimic the example out for scenario 3 of test
    cases.
        Parameters:
              None
        Returns:
              None
    """
    #declaration, creating instances of Line objects
    lineOne = Line(Point(2.0, 2.0), Point(3.0, 3.0))
    lineTwo = Line(Point(1.0, 1.0), Point(6.0, 6.0))

    #printing all the statements with embedded object calls
    print("*")
    print("Scenario 3*")
    print("*")
    print("Line " + lineOne.toString() +
          " Length: {0:.4f} Slope: {1:.4f}".format(lineOne.getLength(),
                                                   lineOne.getSlope()))
    print("Line " + lineTwo.toString() +
          " Length: {0:.4f} Slope: {1:.4f}".format(lineTwo.getLength(),
                                                   lineTwo.getSlope()))
    if lineOne.isParallel(lineTwo):
        print("Parallel.")
    else:
        print("Not parallel.")
    print(end='\n')


#calling all the test case functions
scenarioOne()
scenarioTwo()
scenarioThree()

