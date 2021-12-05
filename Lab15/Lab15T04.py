#Tee ohjelma joka kysyy käyttäjältä lukuja (joko kokonaisluku tai liukuluku) ja tallenna kokonaisluvut eri tiedostoon kuin liukuluvut.
#Sovellus tulee lopettaa jos käyttäjä ei syötä kokonais- tai liukulukua.
#Tarkista tiedostojen sisältö tekstieditorilla.

import os
filename = os.path.expanduser('~/') + 'liukuluvut.txt'
filename2 = os.path.expanduser('~/') + 'kokonaisluvut.txt'

liukuluku = []
kokonaisluku = []

try:
    while True:
        numero = input("Anna kokonais- tai liukuluku: ")
        if numero.isdigit() == True:                    #isdigit katsoo onko stringi numero.
            kokonaisluku.append(numero)                 #Jos True -> Lisää listaan
        if numero.replace(',', '').isdigit() == True or numero.replace('.', '').isdigit() == True: #Poistaa , tai . ja jos numero ilman pilkkua tai pistettä =numero -> True
            if ',' in numero or '.' in numero:          #Jos aikaisemmin True ja inputissa on , tai . niin lisää listaan
                liukuluku.append(numero)
        else: break                                     #Lopettaa jos syöttää mitä tahansa muuta (string tai enter)

except:
    print("Jotain meni vikaan.")

finally:
    file = open(filename, "w")
    liukuluku.sort()
    file.writelines(str(liukuluku))
    file.close

    file = open(filename2, "w")
    kokonaisluku.sort
    file.writelines(str(kokonaisluku))
    file.close

print("Tiedostoon lisätyt liukuluvut:", liukuluku)
print("Tiedostoon lisätyt kokonaisluvut:", kokonaisluku)

