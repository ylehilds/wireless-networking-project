import wave
import serial
from struct import pack,unpack 
import serial.tools.list_ports

def getUSBDevice():
    # prints available devices
    x = serial.tools.list_ports.comports()
    for device in range(len(x)):
        print(x[device])
        if "CP210" in x[device].description:
            return x[device].device

wav = wave.open("sorry_dave.wav", mode="rb")

frame = wav.readframes(1)
print("Sending out: ", frame)
com = getUSBDevice()

ser = serial.Serial(port=com, baudrate=115200)
# ser.write(b'bob\n')
# ser.write(pack("<cc", frame, b'\n'))
ser.write(frame)

while True:
    if ser.in_waiting:
        print(ser.in_waiting)
        print("Recieved back: ", ser.readline())
