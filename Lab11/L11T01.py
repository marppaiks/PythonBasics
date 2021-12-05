#Tee funktio time, joka muuttaa parametrinä saadun sekuntiarvon muotoon tunnit:minuutit:sekunnit.
#Esimerkiksi luvulle 10000, palautetaan tieto seuraavassa muodossa "02:46:40"

def time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return (f"{h:02d}:{m:02d}:{s:02d}")

print(time(10000))
