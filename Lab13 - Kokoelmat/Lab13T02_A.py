#Tee ohjelma joka kysyy käyttäjältä kurssien arvosanoja (arvosana on kokonaisuluku 0,1,2,3,4 tai 5) ja tallentaa ne listaan.
#Käyttäjä voi syöttää niin monta kurssiarvosanaa kuin haluaa, syöttäminen lopetetaan tyhjällä syötteellä.
#Näytä lopuksi montako arvosanaa käyttäjä antoi ja arvosanojen keskiarvo.

gradeslist = []
    
while True:
    grade = input("Anna arvosana asteikolla 0-5: ")
    if not grade : break
    grade = int(grade)
    if grade <6:
        gradeslist.append(grade)
    elif grade >5: print("Epäsopiva arvosana! ")
    else: break

print(len(gradeslist), "kpl arvosanoja")
print("Arvosanojen keskiarvo on:", sum(gradeslist) / len(gradeslist))
