#import a datetime library to access current date and time
import datetime

#declare a variable named 'msg' and set some text to it
msg = "Python rokkaa"

#show message into console
print(msg)

#print the current
print(datetime.datetime.now())

#read text from console and echo back
text = input("Kirjoita jotain tekstiä: ")
print ("Kirjoitit: ")
print(text)
