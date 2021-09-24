def kerro3(age):
    if age < 13:
        return "child"
    elif age >=13 and age <=19:
        return "teen"
    elif age >=20 and age <=65:
        return "adult"
    else:
        return "senior"

age = int(input("Give your age: "))
print(kerro3(age))