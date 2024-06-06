from http.server import HTTPServer, BaseHTTPRequestHandler
import traceback
from send import send

IP = "localhost"
PORT = 8001


class MyHandler(BaseHTTPRequestHandler):
	def end_headers (self):
		self.send_header('Access-Control-Allow-Origin', '*')
		BaseHTTPRequestHandler.end_headers(self)
		
	# def do_GET(self):
	# 	try:
	# 		with open('templates/index2.html', 'r') as f:
	# 			content = f.read()
	# 		self.send_response(200)
	# 		self.send_header('Content-type', 'text/html')
	# 		self.end_headers()
	# 		self.wfile.write(bytes(content, 'utf8'))
	# 	except:
	# 		self.send_response(404)
	# 		self.send_header('Content-type', 'text/html')
	# 		self.end_headers()
	# 		self.wfile.write(b'404: File not found')

	def do_POST(self):
		try:
			data = self.rfile.read(int(self.headers.get('Content-Length')))
			# print(31,data)
			data = data.split(b'\\')
			data = b'\\' + int(data[0]).to_bytes(1,"little") + data[1]
			# print(data)
			send(IP, PORT, data)
		except:
			# print(37r, "do_POST error: ", end="")
			print(37, "do_POST error: ", end="")
			traceback.print_exc()


def main():
	httpd = HTTPServer(('', 8080), MyHandler)
	httpd.serve_forever()
	return

if __name__ == "__main__":
	main()
