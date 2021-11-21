from collections import Counter


file = open('C:\\Users\\Marppa\\names.txt', "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

file = open('C:\\Users\\Marppa\\names.txt', "r")
nimilista = []
for line in file:
    if line != "\n":
        nimilista.append(line)
file.close
c= Counter(nimilista)
print(c)
print(line_count, "Nimeä tiedostossa")





