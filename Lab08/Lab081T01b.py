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