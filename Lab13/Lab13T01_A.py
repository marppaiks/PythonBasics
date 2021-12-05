#Toteuta ohjelma, joka kysyy käyttäjältä autojen rekisterinumeroita (siis esim 'ABC-123' jne) ja tallentaa ne listaan.
#Käyttäjä voi syöttää niin monta rekisterinumeroa kuin haluaa, syöttäminen lopetetaan tyhjällä syötteellä.
#Näytä syötetyt rekisterinumero aakkosjärjestyksessä.

carlist = []

while True:
    car = input("Anna rekisterinumero esim. ABC-123: ")
    if car: carlist.append(car)
    else: break

carlist.sort()
print(f"Rekisterinumerot aakkosjärjestyksessä: {carlist}")


