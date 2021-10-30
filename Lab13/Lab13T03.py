cars = []

while True: # Autojen lisääminen listaan käyttäjän syöttämillä tiedoilla
    if len(cars) >= 3: break #Lopettaa 10 jälkeen

    rekkari = input("Anna rekisterinumero: ")
    if not rekkari: break
    malli = input("Enter brand: ")

    cars.append([rekkari, malli])

sorted

print(sorted(cars))

