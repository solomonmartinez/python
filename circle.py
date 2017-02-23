class circle:

    #radius = 15

    def __init__ (self, radius, pieSq):
        self.radius = radius
        self.pieSq = pieSq

    def area(self):
        return self.radius * self.pieSq
    def circumference(self):
        return self.radius * 2 * 3.14

circleJuan = circle(15, 9.85)

print circleJuan.area()
print circleJuan.circumference()
