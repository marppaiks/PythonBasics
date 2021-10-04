#demo while looppi
#Kysytään käyttäjältä nimiä kunnes käyttäjä antaa tyhjän merkkijonon

#VE1
name = "x"
names = "" #tähän lisätään annetut nimet pilkulla erottettuna

#Looppi VE1
#while name != "":
#   name = input("Anna kaverisi nimi: ")
#    if name != "":
#        names += (name + ",")

#looppi VE2
while True:
    name = input("Anna kaverisi nimi: ")
    if name != "":
        names += name + ","
    else: 
        break

#Näytetään annetut nimet
print(names)