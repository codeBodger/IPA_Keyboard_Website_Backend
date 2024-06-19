import socket
import traceback
from datetime import datetime

RESPONSE_CODES = [
	"success",
	"nokey",
	"noclient",
	"expired"
]

def send(ip: str, port: int, data: str, activity: str):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		if activity == "login":
			data = bytes(data, 'utf-8')
			s.send(b'\x00' + data)
			key = s.recv(18)
			response_code = int.from_bytes(s.recv(1), "big")
			print(key)
		elif activity == "send":
			data = int(data[:3]).to_bytes(1,"little") + bytes(data[3:], 'utf-8')
			s.send(b'\x01' + data)
			response_code = int.from_bytes(s.recv(1), "big")
		else:
			raise Exception(f"Bad activity: {activity}")
		recieved = RESPONSE_CODES[response_code]
		s.close()
		print(recieved)
		fprint(f"{activity}\t{data}\t{recieved}")
	except Exception as e:
		print("unknown")
		fprint(e, traceback.format_exc())
	return

def fprint(*text) -> None:
	with open("python-log", "a") as f:
		f.write(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\t")
		for part in text:
			f.write(f"{part}\n")
