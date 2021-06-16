from commsDaemon import *
import sys
sys.path.insert(0, "../lib")
from udpRX import *
import time
import serial
import socket
from PCA9685_PWM_Driver import *

class Ares_Drive:
       pwm = PWM()     		# instantiate PCA9685
       #IP = "192.168.7.2"	# beaglebone IP
       #IP = "127.0.0.1"	# local IP
       IP = "10.198.187.237"	# mesh IP
       PORT = 15005		# port >10000
       cmd_tuple = 0		# instantiate data
       L_PWM = 0
       L_DIR = 0
       R_PWM = 0
       R_DIR = 0
       commsData = ""
       pwml_0 = 0		# PIN LAYOUT for PCA9685
       pwmh_0 = 1
       dir_0 = 2
       pwml_1 = 3
       pwmh_1 = 4
       dir_1 = 5
       pwml_2 = 6
       pwmh_2 = 7
       dir_2 = 8
       pwml_3 = 9
       pwmh_3 = 10
       dir_3 = 11

       def __init__(self):
                print "Ares Drive System Online"
                self.pwm.setPWMFreq(110)
                self.comms = CommsDriver(self.IP, self.PORT, self.commsThread)
                self.comms.start()

       def listen(self):
                self.cmd_tuple = tuple(x.strip() for x in self.commsData.split(','))
                print self.cmd_tuple
                if len(self.cmd_tuple) < 4:
                        self.cmd_tuple = [0,0,0,0]

                self.L_PWM = float(self.cmd_tuple[0])
                self.L_DIR = float(self.cmd_tuple[1])
                self.R_PWM = float(self.cmd_tuple[2])
                self.R_DIR = float(self.cmd_tuple[3])
                self.pwm.setDuty(self.pwml_0,self.L_PWM)	# set motor 0
                self.pwm.setDuty(self.pwmh_0,self.L_PWM)
                self.pwm.setDuty(self.dir_0,self.L_DIR)
                self.pwm.setDuty(self.pwml_1,self.R_PWM)	# set motor 1
                self.pwm.setDuty(self.pwmh_1,self.R_PWM)
                self.pwm.setDuty(self.dir_1,self.R_DIR)
                self.pwm.setDuty(self.pwml_2,self.R_PWM)	# set motor 2
                self.pwm.setDuty(self.pwmh_2,self.R_PWM)
                self.pwm.setDuty(self.dir_2,self.R_DIR)
                self.pwm.setDuty(self.pwml_3,self.R_PWM)	# set motor 3
                self.pwm.setDuty(self.pwmh_3,self.R_PWM)
                self.pwm.setDuty(self.dir_3,self.R_DIR)

       def commsThread(self, data, ip, port):
                print data, ip, port
                self.commsData = data

       def stop(self):
                self.comms.stop()

def main():
        delay = 0.001
        ares = Ares_Drive()
        while True:
                try:
                        ares.listen()
                        time.sleep(delay)
                except KeyboardInterrupt:
                        ares.stop()
                        break

if __name__== "__main__":
        main()

