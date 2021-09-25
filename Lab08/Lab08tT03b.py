def checkint(param1):
    if param1 == 10 or param1 == 20:
        return "Luku on 10 tai 20"
    elif param1 == 100 or param1 == 200:
        return "Luku on 100 tai 200"
    else:
        return param1

param1 = int(input("Anna kokonaisluku: "))
print(checkint(param1))