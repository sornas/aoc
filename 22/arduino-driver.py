import serial
import sys
import time

def main():
    to_send = "".join(sys.stdin).replace("\n", "\r")
    ser = serial.Serial("/dev/ttyACM0")
    ser.baudrate = 57600
    ser.readline() # wait for one line
    ser.write(bytes(to_send, "ascii"))
    ser.close()

main()
