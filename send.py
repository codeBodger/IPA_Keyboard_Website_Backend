import socket
import traceback
from datetime import datetime

def send(ip: str, port: int, data: bytes):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send(data)
		s.close()
		fprint(str(data[:3]))
	except Exception as e:
		fprint(e, traceback.format_exc())
	return

def fprint(*text) -> None:
	with open("log", "a") as f:
		f.write(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\t")
		for part in text:
			f.write(f"{part}\n")