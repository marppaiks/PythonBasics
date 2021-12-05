#Tee ohjelma, joka kysyy käyttäjältä viisi lukua. Laske annetuista luvuista yhteen ne luvut, jotka ovat nollaa suurempia.

#Eli jos käyttäjä antaa nollan tai negatiivisen luvun sitä ei lisätä summaan.
#Tulosta summa konsoliin. Kokeile ohjelmaasi esim seuraavilla arvoilla: 1,2,3,4,5 ja -2,0,2,4,6. Mitä sait summaksi?


def checknum(sum):
    if a <= 0:
        return b + c + d + e
    elif b <= 0:
        return a + c + d + e
    elif c <= 0:
        return a + b + d + e
    elif d <= 0:
        return a + b + c + e
    elif e <= 0:
        return a + b + c + d
    else:
        return a + b + c + d + e
    

a = int(input("Input number: "))
b = int(input("Input number: "))
c = int(input("Input number: "))
d = int(input("Input number: "))
e = int(input("Input number: "))


print(f"Sum is {checknum(sum)}")
