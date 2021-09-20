#Laske ympyrän säde
#käytä laskemiseen funktiota

#Ympyrän
def circlearea(r):
    area = 3.141 * r * r
    return area

#Neliön
def squarearea(height):
    area = height * height
    return area

#Kolmion
def trianglearea(height, lenght):
    area = (height * lenght) / 2.0
    return area

#main eli "pääohjelma"
r = float(input("Anna ympyrän säde: "))
area = circlearea(r)
print(f"Ympyrän pinta-ala on {area}")

x = float(input("Anna neliön ala: "))
area = squarearea(x)
print(f"Neliön pinta-ala on {area}")

x = float(input("Anna kolmion leveys: "))
y = float(input("Anna kolmion korkeus: "))
area = trianglearea(x,y)
print(f"Kolmion pinta-ala on {area}")