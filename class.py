class movies(object):

    def __init__ (self, title, runTime, genre):
        self.title = title
        self.runTime = runTime
        self.genre = genre

    def time(self):
        print "The total time of the movie was %s minutes." % (self.runTime)


    def printmovie(self):
        return "The total time was %s. The title was %s. The genre was %s." % (self.runTime, self.title, self.genre)


movie1 = movies("Lord of The Rings", 60, "Fantasy")

print movie1.title
print movie1.genre
print movie1.runTime

movie1.time()

print movie1.printmovie()
