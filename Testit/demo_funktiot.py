#Demo funktiot
#Määritellään funktiot
def mysum(a, b):
    #Lasketaan lukujen summa
    summa = a + b
    return summa

def mydivision(a, b):
    retval = a / b
    return retval
#Pääohjelma main
#Kysytään käyttäjältä kaksi lukua
num1 = float(input("Anna ensimmäinen luku: "))
num2 = float(input("Anna toinen luku: "))
summa = mysum(num1, num2)
print("Lukujen summa on:", summa)
#lasketaan lukujen osamäärä
print("Lukujen osamäärä on", mydivision(num1, num2))
