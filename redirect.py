#!/usr/bin/python

print("Content-type: text/html")
print()

import cgi, cgitb

from send import send

cgitb.enable()

IP = "localhost"
PORT = 8001

data = cgi.FieldStorage().value
data = data.split('\\')
activity = data[0]
data = data[1]
send(IP, PORT, data, activity)

print("")
