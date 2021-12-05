def lotto():
    import random
    return random.randrange(1, 41)


numList = []

for i in range(7):
    numList.append(lotto())
    numList.sort(reverse=False)

print(*numList, sep = ",")