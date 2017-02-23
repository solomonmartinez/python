import math

class Circle(object):

    pi = math.pi

    def __init__(self, radius, name):
        self.radius = radius
        self.name = name

    def Circumference(self):
        return 2 * math.pi * self.radius

    def Area(self):
        return math.pi * self.radius * self.radius

    def __str__(self):
        return "Circle with Radius %s" % (self.radius)

    def __add__(self, other):
        return self.radius + other.radius

    def __len__(self):
        return len(self.name)


C1 = Circle(10, "Kitten")
C2 = Circle(15, "Mitten")

print len(C2)
print C1 + C2 
