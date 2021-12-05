# Mäkihypyssä käytetään viittä arvostelutuomaria.
# Kirjoita ohjelma, joka kysyy arvostelupisteet yhdelle hypylle ja tulostaa tyylipisteiden summan siten, että summasta on vähennetty pois pienin ja suurin tyylipiste.

gradesList = []

for i in range(5):
    gradesList.append(int(input("Give points:")))
    gradesList.sort(reverse=False)

del gradesList[-1]
del gradesList[0]

print(f"Total points are: {sum(gradesList)}")
