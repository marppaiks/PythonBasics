#Luetaan olemassa oleva tekstitiedosto
try:
    f = open("Z:/autot.txt", "r")
    lines = f.readlines()
    f.close()
    print(lines)
    for x in lines:
        print("Tallissa on:", x)
    print("Homma hoidettu")

except:
    print("Ohjelman suortus keskeytynyt virheen takia")