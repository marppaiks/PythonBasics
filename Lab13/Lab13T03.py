cars = []

while True: # Autojen lisääminen listaan käyttäjän syöttämillä tiedoilla
    if len(cars) >= 3: break #Lopettaa 10 jälkeen

    rekkari = input("Anna rekisterinumero: ")
    if not rekkari: break
    malli = input("Enter brand: ")

    cars.append([rekkari, malli])

cars.sort(key=lambda x: x[0])
print(cars)

cars.sort(key=lambda x: x[1])
print(cars)
