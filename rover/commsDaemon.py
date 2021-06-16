import threading
import socket
class ThreadWrapper(threading.Thread):
        def __init__(self, threadID, threadFunction, arg):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.arg = arg
                self.threadFunction = threadFunction
                self.isRunning = True

        def run(self):
                print "starting "
                self.threadFunction(self.threadID, self.arg)
                print "ending "


class CommsDriver(object):
        """docstring for CommsDriver"""
        def __init__(self, ip, port, parseFunction):
                super(CommsDriver, self).__init__()
                self.ip = ip
                self.port = port
                self.parseFunction = parseFunction
                self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
                self.sock.bind((self.ip, self.port))
                self.sock.settimeout(1)
                self.isRunning = False
                self.thread = ThreadWrapper( 0, self.networkThread, [self.parseFunction])

        def start(self):
                print "start CommsDriver"
                self.isRunning = True
                self.thread.start()

        def stop(self):
                print "stop CommsDriver"
                self.isRunning = False
                self.sock.close()

        def networkThread(self, threadID, arg):
                parseFunction = arg[0]
                # print "UDP target IP:", UDP_IP
                # print "UDP target port:", UDP_PORT
                print 'start network daemon'
                while self.isRunning:
                        try:
                                data, addr = self.sock.recvfrom(4096) # buffer size is 1024 bytes
                                print "received message:", data, addr[0], addr[1]
                                parseFunction(data, addr[0], addr[1])
                        except:
                                pass

        def sendto(self, msg, ip, port):
                try:
                        print 'commsDriver sends: ', msg, ip, port
                        self.sock.sendto(msg, (ip, port))
                except Exception as e:
                        print e

