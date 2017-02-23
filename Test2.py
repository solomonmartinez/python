class Recta(object):

    def __init__(self, length, width ):
        self.length = length
        self.width = width

    def lengthBox(self):
        return self.length

    def widthBox(self):
        return self.width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)

    def diagonal(self):
        y = (self.length * 2) + (self.width * 2)
        return y ** .5

    def Top(self):
        return "*" * self.length

    def S1(self):
        z = 0
        while z < self.width:
            print "*" , "",  "*"
            z += 1
    def Bottom3(self):
        return "*" * self.length

    ######################

class Cube(Recta):
    def __init__(self, length, width, height):
		super(Recta, self).__init__(self, length, width)
	    self.height = height

    def Volume(self):
        return self.height * self.width * self.length

    def LengthAll(self):
        o = self.length * 4
        v = self.height * 4
        q = self.width * 4
        return o + v + q

    def HWside(self):
        t = self.width * self.height
        LIST1.append(t)
        return self.width * self.height

    def HWside2(self):
        t = self.width * self.height
        LIST1.append(t)
        return self.width * self.height

    def HLside(self):
        t = self.length * self.height
        LIST1.append(t)
        return self.length * self.height

    def HLside2(self):
        t = self.length * self.height
        LIST1.append(t)
        return self.length * self.height

    def Top1(self):
        t = self.length * self.width
        LIST1.append(t)
        return self.length * self.width

    def Bottom1(self):
        t = self.length * self.width
        LIST1.append(t)
        return self.length * self.width

        ##############

rec1 = Recta(4, 4,)

cube1 = Cube(3,3,3)

LIST1 = []


print rec1.lengthBox()
print rec1.widthBox()
print rec1.area()
print rec1.perimeter()
print rec1.diagonal()
print rec1.Top()
rec1.S1()
print rec1.Bottom3()

print cube1.HWside()
print cube1.HWside2()
print cube1.HLside()
print cube1.HLside2()
print cube1.Top1()
print cube1.Bottom1()

print cube1.LengthAll()
