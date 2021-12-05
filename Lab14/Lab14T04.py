#Tee kokoelma, jossa on 5 tekstiä eli merkkijonoa.
#Kysy käyttäjältä indeksi mihin kohtaan listaa käyttäjä haluaa syöttää uuden tekstin.
#Kysy käyttäjältä uusi teksti ja laita se listaan käyttäjän antamaan indeksiin. Tulosta listan sisältö.

#Korjaa ohjelma niin ettei se kaadu, jos käyttäjä syöttää indeksin, joka on listan ulkopuolella.
#Kerro käyttäjälle mikäli indeksi ei ole kelvollinen ja pyydä syöttämään se uudestaan.

kokoelma = ['kissa', 'koira', 'auto', 'tuoli', 'lamppu']

try:
    indeksi = int(input("Mihin kohtaan listaa haluat uuden tekstin (numero): "))
    syöte = input("Uusi teksti: ")
    kokoelma[indeksi] = syöte
    print(kokoelma)

except IndexError:
    print("Listalla ei ollut antamaasi kohtaa.")
    indeksi = int(input("Mihin kohtaan listaa haluat uuden tekstin (numero): "))
    kokoelma[indeksi] = syöte
    print(kokoelma)
