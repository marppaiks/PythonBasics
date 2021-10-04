print("Testataan for-looppia")

names = ['Arska', 'Jaska', 'Kalle']
for name in names:
    print("Hello", name)

#lisääminen
newname = input("Anna nimi: ")
#merkkijono voidaan käydä läpi for-loopilla merkki kerrallaan 
for x in newname:
    print(x)
names.append(newname)
for name in names:
    print("Hello again", name)

#viittaus lisan alkioon indeksin avulla
a = len(names)
for i in range(a):
    print("listan", i, "jäsen on", names[i])
