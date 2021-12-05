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