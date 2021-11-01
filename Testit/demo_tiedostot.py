#Demo tiedostojen käsittelystä
try:

    #absoluuttinen hakemistopolku
    filename = 'c:\\users\\AB6258\\testi.txt'

    #käytetään valmista kirjastoa, ja ohjataan tiedosto kirjautuneen käyttäjän kotihakemistoon
    import os
    filename = os.path.expanduser('~/') + 'testi2.txt'

    #avataan tiedosto, niin kerrotaan avataanko lukemista vai kirjoittamista varten
    file = open(filename, "w")

    #kirjoitetaan tekstitiedostoon
    #file = open("testi.txt", "w")
    #kirjoitetaan tiedostoon write-metodilla
    # \n tekee uuden rivin
    file.write("Creating a file with Python!\n")
    file.write("Today is 1.11.2021\n")

    #Jos haluatte kirjoittaa listan tiedostoon
    lista = ["aaa", "bbb", "ccc"]
    for x in lista:
        file.write(x + "\n")
    #VE2 listan kirjoitukselle
    lista2 = ["111", "222", "333", "444"]
    file.writelines(lista2) #huom listassa voi olla vain merkkijonoja

    #Tulostuksen voi ohjata myös tiedostoon konsolin/terminaalin sijasta
    print("This is a last line", file=file)
    #suljetaan tiedosto
    file.close()

    print("Homma hoidettu.")

except:
    print("Outs, jotain meni vikaan")