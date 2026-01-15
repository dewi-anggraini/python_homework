# Task 5: Extending a Class
import math
# Point = "where" position (a location in 2D, like a dot)
# class Point: represents a Point in 2D spaces with x and y coordinates
# includes method for equality, string represenation, and distance
class Point():
    def __init__ (self, x, y):
        # initialize the Point with x and y value
        self.x = x
        self.y = y
    # to check if two Point objects are equal (only Point objects)
    # to check if 'other' is also a Point ( or subclass like Vector), then compare coordinates for equality
    def __eq__ (self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    # return string representation of the Point
    def __str__ (self):
        return f"Point {(self.x), (self.y)}"
    # to calculate euclidean distance between 'this Point and other Point'
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# class vector: Vector = how far and in what direction (direction & movement like an arrow, don't get confused) 
# a subclass of Point that represents a vector in 2D   
class Vector(Point):
    # string representation
    def __str__ (self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__ (self, other):
        # overrides the + operator to perform vector addition
        # return new vector with summed x + y value
        return Vector(self.x + other.x, self.y + other.y)
    
# Test the code
if __name__ == "__main__":
    p1 = Point(2, 4)
    p2 = Point(3, 6)
    p3 = Point(1, 2)
    print(p1==p2)
    print(str(p1))
    print(p1.distance_to(p2))

    v1 = Vector(2, 3)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    print(v1)
    print(v2)
    print(v3)