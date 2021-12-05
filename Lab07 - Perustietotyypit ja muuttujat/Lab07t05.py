#Esittele muuttuja, johon tallennetaan pankkitilin saldo euroina (alku saldo on 2000 €).
#Tulosta pankkitilin saldo konsoliin. Kysy konsolissa kuinka monta euroa lisätään saldoon.
#Kysy konsolissa kuinka monta senttiä lisätään saldoon. Tulosta saldo konsoliin näiden muutosten jälkeen.

saldo = 2000
print("Account balance:", saldo, "€")

euros = input("How many euros will be added to the balance?: ")
print("You added", euros, "€")


cents = input("How many cents will be added to the balance?: ")
cents = int(cents) / 100
format_cents = "{:.2f}".format(cents)
print("You added ", cents, "€")

summa = int(saldo) + int(euros) + float(cents)

format_summa = "{:.2f}".format(summa)


print("Bank account balance: ", format_summa, "€")
