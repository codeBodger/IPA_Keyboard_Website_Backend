#!/usr/bin/python

print("Content-type: text/html")
print()

import cgi, cgitb

from send import send

cgitb.enable()

IP = "localhost"
PORT = 8001

data = cgi.FieldStorage().value
data = bytes(data, 'utf-8')
data = data.split(b'\\')
data = b'\\' + int(data[0]).to_bytes(1,"little") + data[1]
send(IP, PORT, data)

print("")
