carlist = []

while True:
    car = input("Anna rekisterinumero esim. ABC-123: ")
    if car: carlist.append(car)
    else: break

carlist.sort()
print(f"Rekisterinumerot aakkosjärjestyksessä: {carlist}")


