class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, value):
        comparisonResult = (self.getX() == value.getX()) and (self.getY() == value.getY())
        return comparisonResult
    
    def __repr__(self):
        expression = 'Coordinate({},{})'.format(self.getX(), self.getY())
        return expression

x1 = Coordinate(0, 0)
test1 = Coordinate(0, 0)
print(x1)
print(str(x1 == test1))

test2 = Coordinate(1, 1)
print(str(x1 == test2))

x2 = eval(repr(x1))
print(x2)
print(str(x1 == x2))
