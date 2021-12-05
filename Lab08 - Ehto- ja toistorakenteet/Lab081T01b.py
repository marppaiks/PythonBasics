#Tee ohjelma jossa kysytään käyttäjältä tämän ikä.
#jos ikä on alle 13 vuotta, tulosta "child"
#jos ikä on 13-19 vuotta, tulosta "teen"
#jos se on 20-65 vuotta, tulosta "adult"
#muussa tapauksessa tulosta "senior".

def kerro3(ika):
    if ika < 13:
        return "child"
    elif ika >= 13 and ika <= 19:
        return "teen"
    elif ika >= 20 and ika <= 65:
        return "adult"
    else:
        return "senior"

ika = int(input("Give your age: "))
print(kerro3(ika))
