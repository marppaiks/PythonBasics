#Tee ohjelma, jolla yrität lukea Windows-koneella kaikki tiedostot kovalevyn C:n juuresta
#(macOS/Linux/Unix- koneilla yritä lukea käyttäjän juurihakemisto).
#Näytä tiedostot konsolilla. Koeta sen jälkeen lisätä tiedosto 'ayho.txt' C:n juureen
#(macOS/Linux/Unix -koneilla käyttäjän juurihakemistoon).

#Mitä tapahtui? Korjaa ohjelma niin, ettei se kaadu.

from os import listdir

print(listdir("/"), end="\n\n") #/ spesifoi kansion mistä halutaan printata folderit

try:
    filename = ('C:\\') + 'ayho.txt'
    open(filename, "w")
except PermissionError:
    print("Sinulla ei ole oikeuksia avata tiedostoa c:n juuresta.")
