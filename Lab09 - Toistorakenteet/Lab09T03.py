#Tee ohjelma, joka kysyy ensin käyttäjältä jonkin luvun väliltä 1-10.
#Tämän jälkeen näytä luvut yhdestä annettuun lukuun ja luvun neliön.

numList = []
luku = int(input("Anna numero väliltä 1-10: "))

if luku >0 and luku <10:
    for i in range(luku):
        numList.append(i + 1)
    
    for i, luku in enumerate(numList):
        print(f"Luvun {luku} neliö on {luku ** 2}")
