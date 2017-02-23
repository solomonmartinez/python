from sys import argv
script, filename = argv

txt = open(filename)
LISTQ = []
for i in txt:
    if i[0] == "q":
        LISTQ.append(i.rstrip())
        #LISTQ.append(i)

print LISTQ  #[i].lsstrip()

x = int(raw_input("Input a number"))

QWE = []

for i in LISTQ:
    if len(i) == x :
        QWE.append(i)

print QWE
