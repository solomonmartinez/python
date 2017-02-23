class Cube:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

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




LIST1 = []
cube1 = Cube(3,3,3)

#print cube1.HWside()
#print cube1.HWside2()
#print cube1.HLside()
#print cube1.HLside2()
#print cube1.Top1()
#print cube1.Bottom1()
print cube1.S1()
print cube1.Top()
#print LIST1


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
