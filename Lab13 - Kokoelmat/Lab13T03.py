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
