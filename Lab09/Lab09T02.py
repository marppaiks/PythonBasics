#Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja. Lukuja kysytään siihen saakka kunnes käyttäjä antaa tyhjän syötteen.
#Laske kuinka monta lukua käyttäjä antoi, laske myös annettujen lukujen summa.
#Näytä annettujen lukujen lukumäärä ja summa käyttäjälle.

numList = []



while True:
    num = input("Anna luku: ")
    if num: numList.append(int(num))

    else: break

print(f"Lukuja annettu: {len(numList)}")
print(f"Lukujen summa: {sum(numList)}")
