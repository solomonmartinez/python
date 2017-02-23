from sys import arvg

script, filename = arvg

for i in range(1,1000):
    if i % 2 == 0:
        filename.write(i)
    if i % 3 == 0:
        filname.write(i)

#target = open(filename, "w")
#target.close
#target.write(i)
