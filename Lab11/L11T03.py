#Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen.
#Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja näyttää ne yhtenä rivinä pilkulla erotettuna.

nameList = []

while True:
    name = input("Enter student name:")
    if name: nameList.append(str(name))
    else: break

print(f"Student count: {len(nameList)}")
print(*nameList, sep = ", ")
