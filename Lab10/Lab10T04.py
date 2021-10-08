def calc_consumption(kulutus, hinta, matka):
    kokonaiskulutus = (kulutus / 100) * matka
    kokonaishinta = kokonaiskulutus * hinta
    return (f"Fuel: {kokonaiskulutus:.2f} liter \nCost: {kokonaishinta:.2f} €")


matka = int(input("Enter trip lenght in km:"))
hinta = float(input("Enter fuel price/liter:"))
kulutus = float(input("Enter fuel consumption/100 km:"))

print(calc_consumption(kulutus,hinta,matka))
