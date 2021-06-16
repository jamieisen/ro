from commsDaemon import *
import sys
sys.path.insert(0, "../lib")
from udpRX import *
import time
import serial
import socket
#from PCA9685_Driver import *
import Adafruit_PCA9685
import math

class Ares_Drive:
       #pwm = PWM()     # instantiate PCA9685
       pwm = Adafruit_PCA9685.PCA9685()
       IP = "192.168.2.96"
       #IP = "127.0.0.1"
       #IP = "10.198.187.237"
       #IP = "10.109.119.11"
       PORT = 15005
       #rx = udpRX(IP,PORT)
       cmd_tuple = 0
       L_PWM = 0
       L_DIR = 0
       R_PWM = 0
       R_DIR = 0
                       # PIN LAYOUT for PCA9685
       pwml_0 = 0
       pwmh_0 = 1
       dir_0 = 2
       pwml_1 = 4
       pwmh_1 = 5
       dir_1 = 6
       pwml_2 = 8
       pwmh_2 = 9
       dir_2 = 10
       pwml_3 = 12
       pwmh_3 = 13
       dir_3 = 14

       commsData = ""


       def __init__(self):
                print "Ares Drive System Online"
                #self.pwm.setPWMFreq(110)
		self.pwm.set_pwm_freq(110)
                self.comms = CommsDriver(self.IP, self.PORT, self.commsThread)
                self.comms.start()

       def listen(self):
                self.cmd_tuple = tuple(x.strip() for x in self.commsData.split(','))
                print self.cmd_tuple
                if len(self.cmd_tuple) < 4:
                        self.cmd_tuple = [0,0,0,0]
                #cmd = self.rx.rx()
                #cmd = self.commsData
                #print "cmd", cmd, ":"
                #if cmd == "":
                #       cmd = "h"
                #cmd = raw_input("wasd,h: ")
                #if cmd == "w":
                #       self.cmd_tuple = [99,0,99,0]
                #elif cmd == "a":
                #       self.cmd_tuple = [99,0,99,99]
                #elif cmd == "d":
                #       self.cmd_tuple = [99,99,99,0]
                #elif cmd == "s":
                #       self.cmd_tuple = [99,99,99,99]
                #elif cmd == "h":
                #       self.cmd_tuple = [0,0,0,0]
                #self.cmd_tuple = ""
                self.L_PWM = float(self.cmd_tuple[0])
                self.L_DIR = float(self.cmd_tuple[1])
                self.R_PWM = float(self.cmd_tuple[2])
                self.R_DIR = float(self.cmd_tuple[3])
                #self.pwm.setDuty(self.pwml_0,self.L_PWM)
                #self.pwm.setDuty(self.pwmh_0,self.L_PWM)
                self.setDuty(self.dir_0,self.L_DIR)
		#self.set_pulse(self.pwml_0,self.L_PWM)

                #self.pwm.setDuty(self.pwml_1,self.R_PWM)
                #self.pwm.setDuty(self.pwmh_1,self.R_PWM)
                #self.pwm.setDuty(self.dir_1,self.R_DIR)

                #self.pwm.setDuty(self.pwml_2,self.R_PWM)
                #self.pwm.setDuty(self.pwmh_2,self.R_PWM)
                #self.pwm.setDuty(self.dir_2,self.R_DIR)

                #self.pwm.setDuty(self.pwml_3,self.R_PWM)
                #self.pwm.setDuty(self.pwmh_3,self.R_PWM)
                #self.pwm.setDuty(self.dir_3,self.R_DIR)

       def commsThread(self, data, ip, port):
                print data, ip, port
                self.commsData = data

       def stop(self):
                self.comms.stop()

       def set_pulse(self, channel, pulse):
		pulse_length = 1000000
		pulse_length //= pulse_length
		pulse_length //= 4096
		pulse *= 1000
		pulse //= pulse_length
		pwm.set_pwm(channel, 0, pulse)

       def setDuty(self, channel, duty):
    		off = math.floor(duty*4095)-1
   		high,low = self.bytes(int(off))
    		high = int(high)
    		low = int(low)
    		on_low = 0x01
   	 	on_high = 0x00
    		off_low = low
    		off_high = high
		self.pwm.set_pwm(self, channel, on, off)

       def bytes(self, integer):
		return divmod(integer,0x100)

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

