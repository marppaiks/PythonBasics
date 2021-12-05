#Toteuta ohjelma, johon voi tallentaa kymmenen eri auton tiedot.
#Kustakin autosta tiedetään rekisterinumero (esim ABC-123) ja autonmerkki (esim Skoda).

#Keksi itse erilaisia rekisterinumeroita ja automerkkejä. Tallenna tiedot valitsemaasi kokoelmaan.
#Tulosta sen jälkeen autojen tiedot ensin aakkosjärjestyksssä automerkin mukaan, ja sen jälkeen aakkosjärjestyksessä rekisterinumeron mukaan.

cars = []

while True: # Autojen lisääminen listaan käyttäjän syöttämillä tiedoilla
    if len(cars) >= 10: break #Lopettaa 10 jälkeen

    rekkari = input("Anna rekisterinumero: ")
    if not rekkari: break
    malli = input("Anna malli: ")

    cars.append([rekkari, malli])

cars.sort(key=lambda x: x[0])
print(cars)

cars.sort(key=lambda x: x[1])
print(cars)
