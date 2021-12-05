from os import listdir

print(listdir("/"), end="\n\n") #/ spesifoi kansion mistä halutaan printata folderit

try:
    filename = ('C:\\') + 'ayho.txt'
    open(filename, "w")
except PermissionError:
    print("Sinulla ei ole oikeuksia avata tiedostoa c:n juuresta.")
