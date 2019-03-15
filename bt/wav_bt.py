import wave
import serial
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

bd_addr = "30:AE:A4:D4:8D:52"
port = 1
sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
# sock.send("hello!!")
# sock.close()

wav = wave.open("sorry_dave.wav", mode="rb")
# com = getUSBDevice()
framerate = wav.getframerate()
print("framerate: ", framerate)
# ser = serial.Serial(port=com, baudrate=115200)
# time.sleep(.1)

# print(readbytes())
while True:
    x = time.time()
    frame = wav.readframes(framerate)
    if frame == b'':
        break
    # print(frame)
    # frame = unpack("<B", frame)[0]

    # ser.write(frame)
    sock.send(frame)
    T = 1 - (time.time() - x)
    time.sleep(T)
    print("time: ", time.time() - x)
    # ser.write(pack("<cc", frame, b'\n'))
    # ser.write(frame)
    # readbytes()

finally:
    sock.close()