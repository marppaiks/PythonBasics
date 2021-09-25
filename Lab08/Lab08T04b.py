def checkpoints(points):
    if points == 0 or points == 1:
        return "Grade:  0"
    elif points == 2 or points == 3:
        return "Grade: 1"
    elif points == 4 or points == 5:
        return "Grade: 2"
    elif points == 6 or points == 7:
        return "Grade: 3"
    elif points == 8 or points == 9:
        return "Grade: 4"
    elif points == 10 or points == 11 or points == 12:
        return "Grade: 5"

points = int(input("Insert your points: "))
print(checkpoints(points))