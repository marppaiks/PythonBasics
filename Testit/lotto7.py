#Demo Lotto, arvotaan 7 numero 40:sta
#Listassa 40 alkiota, joiden arvo on aluksi False
import random
numerot = []
for x in range(40):
    numerot.append(False)

#arvotaan 7 toisistaan poikkeavaa numeroa
i = 0 #laskuri
while i < 7:
    a = random.randrange(1,40)
    #tarkista, onko jo listassa arvottu
    if not numerot[a]:
        numerot[a] == True      #Muutetaan arvoon True
        i += 1

#tulostetaan
txt = "Tässä sinulle arvotut 7 numeroa: "
print(txt)
i = 0
for x in numerot:
    i += 1
    if x:
        txt += str(i) + " "
        #print(i)
#tulostus samalle riville
print(txt)
