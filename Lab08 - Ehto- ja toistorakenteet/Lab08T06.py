#Tee ohjelma joka näyttää onko annettu vuosi karkausvuosi. Vuosiluku kysytään käyttäjältä.
#Algoritmi:
#4:llä jaolliset on, paitsi täydet vuosisadat. Kuitenkin 400:lla jaolliset vuosisadat ovat karkausvuosia.
#Esim. 1991 -> ei, 1992 -> on, 1900 -> ei, 2000 -> on

def checkleap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Is leap year!"
            else:
                return "Is not leap year!"
        else:
            return "Is leap year!"
    else:
        return "Is not leap year!"

year = int(input("Insert year: "))
print(checkleap(year))
