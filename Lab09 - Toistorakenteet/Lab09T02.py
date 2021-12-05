numList = []



while True:
    num = input("Anna luku: ")
    if num: numList.append(int(num))

    else: break

print(f"Lukuja annettu: {len(numList)}")
print(f"Lukujen summa: {sum(numList)}")