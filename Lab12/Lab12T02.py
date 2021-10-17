class Cat:
    def __init__(self, name= "", color=""): #Luodaan muodostaja
        self.name = name
        self.color = color

    def __str__(self): #Määrittelee luokan tiedot tekstiksi
        return self.name + ", " + "Color: " + self.color
    
    def miau(self): #Metodi, eli luokan oma funktio
        return f"{self.name} says: Meoooooow!"

    name = ""
    color = ""

kissa = Cat("Kit", "black")
kissa2 = Cat("Kat", "white")

print(kissa.__str__())
print(kissa2.__str__())
print(kissa.miau())
print(kissa2.miau())