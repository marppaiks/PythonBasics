def checkint(num):
    if num == 10 or num == 20:
        return "Luku on 10 tai 20"
    elif num == 100 or num == 200:
        return "Luku on 100 tai 200"
    else:
        return num

num = int(input("Anna kokonaisluku: "))
print(checkint(num))