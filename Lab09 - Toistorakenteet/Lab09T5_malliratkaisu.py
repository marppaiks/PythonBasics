import random

def lotto():
    indexes = [(i+1) for i in range(40)]
    numbers = []

    for x in range(7):
        index = random.randrange(0,len(indexes)-1)
        numbers.append(indexes[index])
        indexes.pop(index)

    numbers.sort()
    string = ','.join(str(number) for number in numbers)
    return string