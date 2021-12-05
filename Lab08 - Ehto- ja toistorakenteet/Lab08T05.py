def checknum(sum):
    if a <= 0:
        return b + c + d + e
    elif b <= 0:
        return a + c + d + e
    elif c <= 0:
        return a + b + d + e
    elif d <= 0:
        return a + b + c + e
    elif e <= 0:
        return a + b + c + d
    else:
        return a + b + c + d + e
    

a = int(input("Input number: "))
b = int(input("Input number: "))
c = int(input("Input number: "))
d = int(input("Input number: "))
e = int(input("Input number: "))


print(f"Sum is {checknum(sum)}")