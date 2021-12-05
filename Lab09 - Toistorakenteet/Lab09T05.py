#Tee funktio lotto(), joka arpoo lottorivin seitsemän (7) numeroa väliltä 1-40 ja palauttaa sen merkkijonona, luvut eroteltuna pilkuilla.
#Siis esimerkiksi näin:   1,3,5,10,20,33,39

def lotto():
    import random
    return random.randrange(1, 41)


numList = []

for i in range(7):
    numList.append(lotto())
    numList.sort(reverse=False)

print(*numList, sep = ",")
