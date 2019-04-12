import wave
import sys
from struct import pack,unpack 
import bluetooth
import time
import os


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
