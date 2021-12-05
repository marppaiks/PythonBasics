#Toteuta funktio isthiszero(num). Funktiolla välitetään yksi parametri. Funktio palauttaa true jos parametrin arvo on nolla.
#Funktio palauttaa false, jos parametri on luku mutta ei nolla. Funktio nostaa TypeError-poikkeuksen, jos parametri ei ole luku.

#Kokeile kutsua  ohjelmasta funktioita eri arvoilla. Toteuta kutsuvalla ohjelmalle try - except. Mitä havaitset?
#Vastaukset tehtävän alkuun kommentteina.


#Havaitsin, että tehtävänanto on epäselvä.
#En osannut tulkita, haluttiinko tässä että numeroiksi käy vain intit ja floatit, vai haluttiinko myös str-tyyppiset numerot.
#Ohjelma tulkitsee nyt str-tyyppiset TypeErrorina, vaikka niissä ei olisi kirjaimia.


def isthiszero(num):
    try:
        if type(num) is int or type(num) is float:
            return num == 0
        else:
            raise TypeError
    except TypeError:
        return "Virhe: Ei ollut numero"

print(isthiszero("0"))
print(isthiszero("kakka"))
print(isthiszero(0))
print(isthiszero(1.7))
print(isthiszero(1))
