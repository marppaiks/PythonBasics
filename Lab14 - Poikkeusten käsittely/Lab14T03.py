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
