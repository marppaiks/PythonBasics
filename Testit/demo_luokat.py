#Luokka (class)
class Dog:
    #ominaisuudet (properties)
    age = 0
    name = "unknown"
    breed = "canis familiaris"
    #metodi
    def bark(self, sound):
        return f"{self.name} says {sound}"


#Pääohjelma käyttää luokkaa, eli luodaan olioita
dog = Dog()
dog.name = "Reiska"
dog.breed = "Jodlaava matikkakoira"
dog.age = 10

#näytetään koiran tiedot
print("Koirani nimi on:", dog.name)
print("Koirani on rodultaan:", dog.breed)
print("Koirani on", dog.age)
print(dog.bark("Räyh"))
#print(f"Koirani {dog.name} sanoo: {dog.bark('Vuh vuh')}")

#toinen koira
dog2 = Dog()
dog2.name = "Tintti"
dog2.breed = "Villakoira"
dog2.age = 5

print(dog2.name, dog2.breed, dog2.age, dog2.bark("hau"))

#koirat listaan
dogs = [dog, dog2]
#Käydään koiralauma läpi
print("Koiramme ovat")
for x in dogs:
    print(x.name)