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