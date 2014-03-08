from time import sleep
import serial

class Port:

    def __init__(self, port = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00", baudrate = 115200):
        self.port = serial.Serial(port=port, baudrate=baudrate, timeout=0)
        self.port.setDTR(level=False)
        sleep(2)
        self.port.flush()

    def nonBlockingRead(self):
        return self.port.read()

    def write(self, message):
        self.port.write(message)
