#Tee ohjelma joka kysyy käyttäjältä kaksi kokonaislukua ja tulostaa niiden:
# summan
# erotuksen
# tulon
# osamäärän


text1 = input("Anna kokonaisluku: ")
text2 = input("Anna toinen kokonaisluku: ")

summa = int(text1) + int(text2)
erotus = int(text1) - int(text2)
tulo = int(text1) * int(text2)
osamäärä = int(text1) / int(text2)

print("Summa: ", summa)
print("Erotus: ", erotus)
print("Tulo: ", tulo)
print("Osamäärä", osamäärä)
