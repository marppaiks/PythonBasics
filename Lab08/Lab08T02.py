#Tee ohjelma joka kysyy käyttäjältä 3 kokonaislukua ja tulostaa niistä suurimman.

def maximum(a, b, c):
     
    if a >= b and a >=c:
        return a
    if b >= a and b >=c:
        return b
    if c >=a and c >=b:
        return c
     
# Driver code
a = int(input("Input integer: "))
b = int(input("Another integer: "))
c = int(input("One more: "))

print(maximum(a, b, c))
