import socket
import traceback
from datetime import datetime

TERMINATION_CODES = [
	"success",
	"nokey",
	"noclient"
]

def send(ip: str, port: int, data: bytes):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send(data)
		termination_code = int.from_bytes(s.recv(1), "big")
		recived = TERMINATION_CODES[termination_code]
		s.close()
		print(recived)
		fprint(f"{data}\t{recived}")
	except Exception as e:
		print("unknown")
		fprint(e, traceback.format_exc())
	return

def fprint(*text) -> None:
	with open("python-log", "a") as f:
		f.write(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\t")
		for part in text:
			f.write(f"{part}\n")
