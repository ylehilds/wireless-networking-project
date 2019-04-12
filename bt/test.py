import os
import wave

path = "/home/cramsted/Documents/School/sound_bytes/"
files = os.listdir(path)

for i in files:
    w = wave.open(path+i, mode='rb')
    print("{}: {}".format(i, w.getframerate()))