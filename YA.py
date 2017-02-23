import time

class myNumbers:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addMethod(self):
        return self.a + self.b + self.c


    def multiply(self):
        return self.a * self.b * self.c

    def middleNumber(self):
        if self.a > self.b and self.a < self.c:
            return self.a

        if self.b > self.a and self.b < self.c:
            return self.b

        if self.c > self.a and self.c < self.b:
            return self.c

    def Largest(self):

        if self.a > self.b and self.a > self.c:
            return self.a

        if self.b > self.a and self.b > self.c:
            return self.b

        if self.c > self.b and self.c > self.a:
            return self.c

        if self.a == self.b or self.a == self.c:
            return False

        if self.b == self.c:
            return False

    def Smallest(self):

        if self.a < self.b and self.c:
            return self.a

        if self.b < self.a and self.c:
            return self.b

        if self.c < self.b and self.a:
            return self.c

    def Average(self):
        return self.a * self.b * self.c / 3

    def Triangle(self):
        count = 0
        if self.a == self.b:
            count += 1
        if self.a == self.c:
            count += 1
        if count == 2:
            return "Equilateral Triangle"
        if count == 1:
            return "Isoceles Triangle"
        if count == 0:
            return "Scalene Triangle"

    def __str__(self):
        return "myNumbers contains the following numbers: %s, %s, %s" % (self.a, ",", self.b, ",", self.c)

    def __add__(self, other):
        return [self.a + other.a, self.b + other.b, self.c + other.c]

    def __sub__(self, other):
        return [self.a - other.a, self.b - other.b, self.c - other.c]

    def isMinute(self):
        if (time.strftime("%M:")) == self.c:
            return True

Numberz = myNumbers(8,8,9)
Numberz2 = myNumbers(15, 25, 33)

print Numberz.Triangle()
print Numberz + Numberz2
print Numberz - Numberz2
print (time.strftime("%M"))
print Numberz.isMinute()
