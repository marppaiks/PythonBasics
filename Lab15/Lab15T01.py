import os
try:
    filename = os.path.expanduser('~/') + 'nimet.txt'

    file = open(filename, "w") #Avataan tiedosto kirjoittamista varten
    name = "*"
    i = 0
    while i < 3:
        name = input("Anna sukunimi: ")
        if i <3:
            file.write(name + "\n")
            i += 1
    file.close()
    print(i, "sukunimeä kirjattu:", filename)

    dump = input("Paina enter-näppäintä jatkaaksesi")
    file = open(filename, "r") #Avataan tiedosto lukemista varten
    lines = file.readlines()
    for line in lines:
        print(line)

except:
    print("Jotain meni vikaan.")

finally:
    file.close()

