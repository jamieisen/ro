import socket

class udpRX:
	UDP_IP = 0
	UDP_PORT = 0
	sock = 0

	def __init__(self,IP,PORT):
		self.UDP_IP = IP
		self.UDP_PORT = PORT
		self.sock = socket.socket(socket.AF_INET, # Internet
				     socket.SOCK_DGRAM) # UDP
		self.sock.bind((self.UDP_IP, self.UDP_PORT))

	def rx(self):
		data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
		#print "received message:", data
		return data

def main():
	#rx = udpRX("192.168.7.2",22)
	rx = udpRX("127.0.0.1",40001)
       	while True:
		str = rx.rx()
		print str

if __name__ == '__main__':
	main()
