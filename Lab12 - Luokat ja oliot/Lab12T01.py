#Tee luokka Human. Luokalla on kaksi ominaisuutta name ja age. Kirjoita Human-luokka seuraavasti:
# Konstruktori alustaa Human-olion nimen ja iän parametrien kautta.
# Luokan str metodi toimii kuten on alla esitetty
#Luo kaksi Human-luokan oliota seuraavilla tiedoilla:
#Nimi: Adam, Ikä: 18
#Nimi: Eva, Ikä: 18

class Human:
    def __init__(self, name= "", age= 0):
        self.name = name
        self.age = age

    def __str__(self):
        return "Nimi: " + self.name + ", " + "Ikä: " + str(self.age)

    name = ""
    age = 0

person = Human("Adam", 18)
person2 = Human("Eva", 18)

print(person.__str__())
print(person2.__str__())
