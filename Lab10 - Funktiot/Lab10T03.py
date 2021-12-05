def average(num1, num2, num3):
    keskiarvo = (num1 + num2 + num3) / 3
    format_keskiarvo = "{:.1f}".format(keskiarvo)
    return format_keskiarvo

print(average(21,31,42))