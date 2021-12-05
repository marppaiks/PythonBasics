#Tee ohjelma, jossa yrität muuttaa listan sellaista arvoa, jota ei ole olemassa.
#Alusta siis lista, jossa on neljä elementtiä ja sen jälkeen yritä muuttaa viidettä elementtiä.
#Tarkista millaisen poikkeuksen saat.
#Korjaa ohjelma niin ettei se kaadu.

lista = [1,2,3,4]

try:
    lista[4] = "Testi"

except IndexError:
    print("Listassa ei ole elementtiä, jota yrität muuttaa.")
