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
port = 1
x = None
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
    while True:
        frame = wav.readframes(512)
        if frame == b'':
            break
        # print(frame)
        # frame = unpack("<B", frame)[0]

        # ser.write(frame)
        sock.send(frame)
        data = sock.recv(16)
        print("next")
        # x = time.time()
        #         # Look for the response
        # amount_received = 0
        # amount_expected = len(frame)

        # while amount_received < amount_expected:
        #     data = sock.recv(16)
        #     y  = time.time() - x
        #     print("time: ", y, " approx. time per byte: ", y / 512, " max hz: ", 1.0 / (y/512))
        #     sys.exit()
            
        #     if x is None:
        #         x = time.time()
        #     elif time.time()  - x > 1.0:
        #         sys.exit()
        #     count += 1
        #     amount_received += len(data)
            # print("count: ", count, " ", sys.stderr, 'received "%s"' % data)
        # T = 1 - (time.time() - x)
        # time.sleep(T)
        # print("time: ", time.time() - x)
        # ser.write(pack("<cc", frame, b'\n'))
        # ser.write(frame)
        # readbytes()
finally:
    sock.close()