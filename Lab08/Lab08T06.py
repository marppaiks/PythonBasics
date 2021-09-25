def checkleap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return "Is leap year!"
            else:
                return "Is not leap year!"
        else:
            return "Is leap year!"
    else:
        return "Is not leap year"

year = int(input("Insert year: "))
print(checkleap(year))