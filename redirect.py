#!/usr/bin/python

print("Content-type: text/html")
print()

import cgi, cgitb

from send import send

cgitb.enable()

IP = "localhost"
PORT = 8001

data = cgi.FieldStorage().value
send(IP, PORT, data)

print("")
