gradesList = []

for i in range(5):
    gradesList.append(int(input("Give points:")))
    gradesList.sort(reverse=False)

del gradesList[-1]
del gradesList[0]

print(f"Total points are: {sum(gradesList)}")