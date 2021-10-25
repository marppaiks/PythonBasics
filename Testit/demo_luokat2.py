class Cat:
    breed = "Felix Catus"
    name = ""
    #ylikirjoitetaan merkkijonomuunnos
    def __str__(self):
        return self.name + " " + self.breed
    #Määritellään luokalle konstruktori
    def __init__(self, name):
        self.name = name


#luodaan kissa-olio
cat = Cat("Repe")
#cat.name = "Mesi"

a = cat.breed
b = cat.name
#print(a, b)
print(cat)