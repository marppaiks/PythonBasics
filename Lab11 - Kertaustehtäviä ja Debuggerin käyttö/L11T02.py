#Tee funktiot: celToFah ja fahToCel

#Funktiot ottavat parametrikseen asteluvun ja muuttavat sen joko fahrenheitit celsiuksiksi tai celsius-asteet fahrenheitiksi.
# Muutettu astearvo palautetaan yhden desimaalin tarkkuudella.
#Testaa kumpikin funktio kutsumalla sitä käyttäjän antamilla luvuilla.
#Esimerkiksi testi print(celToFah(10.0)) palauttaa arvon 50.0

def celToFah(celsius):
    celToFah = celsius * 1.8 + 32
    format_celToFah = "{:.1f}".format(celToFah)
    return format_celToFah
print(celToFah(32.0))

def fahToCel(fahrenheit):
    fahToCel = ((fahrenheit - 32) * 5) / 9
    format_fahToCel = "{:.1f}".format(fahToCel)
    return format_fahToCel
print(fahToCel(88.0))
