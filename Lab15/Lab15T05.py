#Tee ohjelma, joka arpoo lottorivin ja tallentaa ne tekstitiedostoon 'lotto.txt'.
#Arvottu rivi sisältää seitsemän (7) numeroa väliltä 1-40. Varmista arpoessasi riviä että sama numero ei voi esiintyä kahta kertaa.

import random
import os
filename = os.path.expanduser('~/') + 'lotto.txt'
file = open(filename, "w")


lottonumerot = []
i=0
for i in range (7):
    numero = random.randint(1,40)
    while numero in lottonumerot:
         numero = random.randint(1,40)
    lottonumerot.append(numero)
    i += 1

lottonumerot.sort()
file.writelines(str(lottonumerot))
file.close

print(lottonumerot)
