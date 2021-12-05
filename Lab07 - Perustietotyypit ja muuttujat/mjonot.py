#Demo merkkijonoista
name = "Jaska"
name2 = "Janica"

#HUOM, entäs input, eli käyttäjän syöte
name = input("Ole hyvä, anna nimesi: ")
#tervehditään meidän kavereita
#merkkijonoja yhdistetään + operaattorilla
uusi = name + name2
print(uusi)
print("Hello" + name)
print("Hello", name, name2, uusi)

#tervehditään muodossa "Hello: Jaska"
print("Hello:", name)

#VE2 voi tehdä myös näin
output = "Hello: " + name
print(output)

#tervehditään käyttäjää tyyliin "Hello Janica, mitäpä kuuluu?"
output = "Hello " + name2 + ", mitäpä kuuluu?"
print(output)

#VE2 käytetään f-sanaa (format)
print(f"Hello {name2}, mitäpä kuuluu?")

