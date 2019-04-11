import wave
import sys
from struct import pack,unpack 
# import serial.tools.list_ports
import bluetooth
import time

# def getUSBDevice():
#     # prints available devices
#     x = serial.tools.list_ports.comports()
#     for device in range(len(x)):
#         print(x[device])
#         if "CP210" in x[device].description:
#             return x[device].device

def readbytes():
    output = b''
    while ser.in_waiting:
        output += ser.read(size=ser.in_waiting)
        time.sleep(.001)
    return output

bd_addr ="cc:50:e3:80:a5:06"
# bd_addr = "30:AE:A4:D4:8D:52"

port = 1
x = None
paused = False
try:
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    # sock.send("hello!!")
    # sock.close()

    wav = wave.open("../sorry_dave.wav", mode="rb")
    # com = getUSBDevice()
    framerate = wav.getframerate()
    print("framerate: ", framerate)

    count = 0
    
    frame = wav.readframes(512)
    while True:
        if not paused:
            if frame == b'':
                break
            sock.send(frame)
            frame = wav.readframes(256)

        data = sock.recv(1) 
        print("recieved frame ", data)
        if "p" == data.decode("utf-8"):
            paused = not paused
            if not paused: # unpausing the audio stream
                frame = wav.readframes(512)
        elif "n" == data.decode("utf-8"):
            print("next")
        elif "q" == data.decode("utf-8"):
            print("prev")
finally:
    sock.close()