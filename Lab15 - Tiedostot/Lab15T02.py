#Luo jollakin editorilla (esim Notepadilla) tekstitiedosto 'nimet.txt', johon lisäät vähintään kymmenen naisten ja kymmenen miesten etunimeä.
#Tee ohjelma, joka lukee em. tekstitiedostosta nimet ja kertoo montako nimeä löytyy ja montako kertaa kukin nimi esiintyy.
#Huomioi myös muut mahdolliset poikkeukset joita tiedoston käsittely voi aiheuttaa.

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





