#!/usr/bin/python

# © 2024 by Rowan Ackerman
# All parts of this and other files in this repository not autogenerated
# are under the copyright of Rowan Ackerman.

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
