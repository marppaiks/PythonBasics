#Tee ohjelma, joka kysyy käyttäjältä viikon kunkin päivän sademäärän.
#Sademäärä annetaan kokonaislukuna, jollei kyseisenä päivänä ole satanut käyttäjä antaa luvuksi 0.
#Laske ja näytä viikon kokonaissademäärä.

numList = []

for i in range(7):
    numList.append(int(input("Insert number (rainfall): ")))

print(f"Rainfall sum is {sum(numList)}")
