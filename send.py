import socket


def send(ip: str, port: int, data: bytes):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(data)
	s.close()
	print(str(data[:3]))
	return
