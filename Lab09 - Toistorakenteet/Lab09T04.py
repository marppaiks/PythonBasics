#Tee ohjelma, joka kysyy käyttäjältä käyttäjän etu ja sukunimen.
#Tulosta käyttäjän etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia.
#Tämän jälkeen tulosta käyttäjän sukunimi käänteisessä järjestyksessä.

etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")


print(etunimi[0] * len(etunimi), sukunimi[::-1])
