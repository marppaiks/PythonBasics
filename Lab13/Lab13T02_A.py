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