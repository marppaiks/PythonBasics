nameList = []

while True:
    name = input("Enter student name:")
    if name: nameList.append(str(name))
    else: break

print(f"Student count: {len(nameList)}")
print(*nameList, sep = ", ")