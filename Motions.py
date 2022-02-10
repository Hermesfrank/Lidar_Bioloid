import serial
from time import sleep

# open serial port; RPi talks to robot controller this way
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)


def forward():
    ser.write(b'\xFF\x55\x01\xFE\x00\xFF')

def back():
    ser.write(b'\xFF\x55\x02\xFD\x00\xFF')

def right():
    ser.write(b'\xFF\x55\x08\xF7\x00\xFF')

def left():
    ser.write(b'\xFF\x55\x04\xFB\x00\xFF')

def stop():
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')
    sleep(1)
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')
