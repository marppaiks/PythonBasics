#Tee funktio calc_consumption. Sinne viedään parametreina:

# auton kulutus litraa/100km
# polttoaineen hinta euroa per litra
# kuljettu matka kilometreinä.
# calc_consumption-funktio palauttaa tietoina kuinka monta litraa polttoainetta on kulunut matkalla sekä polttoaineeseen kuluneen rahan määrän.
#Kysy käyttäjältä:
#kulutus, polttoaineen hinta ja kuljettu matka.
#Sen jälkeen kutsu calc_consumption-funktiota ohjelmasta. Tarkista että funktio laskee kulutuksen ja polttoaineen hinnan oikein.

def calc_consumption(kulutus, hinta, matka):
    kokonaiskulutus = (kulutus / 100) * matka
    kokonaishinta = kokonaiskulutus * hinta
    return (f"Fuel: {kokonaiskulutus:.2f} liter \nCost: {kokonaishinta:.2f} €")


matka = int(input("Enter trip lenght in km:"))
hinta = float(input("Enter fuel price/liter:"))
kulutus = float(input("Enter fuel consumption/100 km:"))

print(calc_consumption(kulutus,hinta,matka))
