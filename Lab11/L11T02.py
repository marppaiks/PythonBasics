def celToFah(celsius):
    celToFah = celsius * 1.8 + 32
    format_celToFah = "{:.1f}".format(celToFah)
    return format_celToFah
print(celToFah(32.0))

def fahToCel(fahrenheit):
    fahToCel = ((fahrenheit - 32) * 5) / 9
    format_fahToCel = "{:.1f}".format(fahToCel)
    return format_fahToCel
print(fahToCel(88.0))
