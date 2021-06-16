import socket

class udpTX:
	UDP_IP = 0
	UDP_PORT = 0
	sock = 0
	data = 0

	def __init__(self,IP,PORT):
		self.UDP_IP = IP
		self.UDP_PORT = PORT
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        def tx(self,data):
		self.sock.sendto(data, (self.UDP_IP, self.UDP_PORT))

def main():
        tx = udpTX("192.168.7.2",40001)
        while True:
		message = "hello"
                tx.tx(message)

if __name__ == "__main__":
	main()
