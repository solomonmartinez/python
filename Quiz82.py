from sys import argv

script, filename = argv

list2 = ""

for i in range(1,1000):
    if i % 2 == 0:
        list2+=str(i)
    if i % 3 == 0:
        list2+=str(i)

#print list2

text22 = open(filename, "w")
text22.close
text22.write(list2)
print text22.txt
