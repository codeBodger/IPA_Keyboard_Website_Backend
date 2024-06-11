import socket


def send(ip: str, port: int, data: bytes):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(data)
	s.close()
	fprint(str(data[:3]))
	return

def fprint(data: str) -> None:
	with open("log", "a") as f:
		f.write(f"Time:\t{data}\n")