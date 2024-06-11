import socket

def send(ip: str, port: int, data: bytes):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send(data)
		s.close()
		fprint(str(data[:3]))
	except Exception as e:
		fprint(e.__traceback__)
	return

def fprint(data: str) -> None:
	with open("log", "a") as f:
		f.write(f"Time:\t{data}\n")