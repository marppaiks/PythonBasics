lista = [1,2,3,4]

try:
    lista[4] = "Testi"

except IndexError:
    print("Listassa ei ole elementtiä, jota yrität muuttaa.")
