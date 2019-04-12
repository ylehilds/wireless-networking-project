import wave
import sys
from struct import pack,unpack 
import bluetooth
import time
import os

# bd_addr ="cc:50:e3:80:a5:06"
# # bd_addr = "30:AE:A4:D4:8D:52"

# port = 1
# paused = False
# newsong = False
# path = sys.argv[1]
# files = os.listdir(path)
# wav = None
# frame = None

# def loadWave():
#     global wav
#     global path
#     global files
#     global frame
#     global newsong
#     print(path+files[0])
#     try:
#         wav.close()
#     except:
#         print("failed")
#     wav = wave.open(path+files[0], mode="rb")
#     newsong = True
#     frame = wav.readframes(512)
#     print(frame)

# try:

#     sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#     sock.connect((bd_addr, port))
#     loadWave()
    
#     framerate = wav.getframerate()
#     print("framerate: ", framerate)

#     while True:
#         if not paused:
#             if frame == b'':
#                 # files = files[1:] + [files[0]]
#                 # loadWave()
#                 break
#             sock.send(frame)
#             if not newsong:
#                 frame = wav.readframes(256)
#                 newsong= False

#         data = sock.recv(1) 
#         # print("recieved frame ", data)
#         if "p" == data.decode("utf-8"):
#             paused = not paused
#             if not paused: # unpausing the audio stream
#                 frame = wav.readframes(512)
#         elif "n" == data.decode("utf-8"):
#             files = files[1:] + [files[0]]
#             loadWave()
#             print("next")
#         elif "q" == data.decode("utf-8"):
#             files = [files[-1]] + files[:-1]
#             loadWave()
#             print("prev")
# finally:
#     wav.close()
#     sock.close()

class BTSpeaker:
    bd_addr ="cc:50:e3:80:a5:06"
    # bd_addr = "30:AE:A4:D4:8D:52"

    port = 1
    paused = False
    newsong = False
    path = sys.argv[1]
    files = os.listdir(path)
    wav = None
    frame = None

    def __init__(self):
        self.sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((self.bd_addr, self.port))

        self.loadWave()

    def __del__(self):
        self.wav.close()
        self.sock.close()

    def loadWave(self):
        print(self.path+self.files[0])
        try:
            self.wav.close()
        except:
            # print("failed")
            pass
        self.wav = wave.open(self.path+self.files[0], mode="rb")
        self.newsong = True
        self.frame = self.wav.readframes(512)
        # print(self.frame)

    def run(self):
        while True:
            if not self.paused:
                if self.frame == b'':
                    self.files = self.files[1:] + [self.files[0]]
                    self.loadWave()
                    # break
                self.sock.send(self.frame)
                self.newsong= False
                if not self.newsong:
                    self.frame = self.wav.readframes(256)

            data = self.sock.recv(1) 
            if "p" == data.decode("utf-8"):
                self.paused = not self.paused
                if not self.paused: # unpausing the audio stream
                    self.frame = self.wav.readframes(512)
            elif "n" == data.decode("utf-8"):
                self.files = self.files[1:] + [self.files[0]]
                self.loadWave()
            elif "q" == data.decode("utf-8"):
                self.files = [self.files[-1]] + self.files[:-1]
                self.loadWave()

if __name__ == "__main__":
    bt = BTSpeaker()
    bt.run()