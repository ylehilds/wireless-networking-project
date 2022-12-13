# wireless-networking-project
Wireless Networking Project

1. The file to push to ESP32 is located at: wireless-networking-project/bt/ESP32BluetoothReceivingData/ESP32BluetoothReceivingData.ino
2. The file to be ran on a Windows 11 + is located at: wireless-networking-project/bt/wav_bt.py. You need python 3 and bluetooth library, follow these steps to make sure you have the correct python libraries:

3. Download and run "Visual Studio Installer": https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
4. Install "Visual Studio Build Tools 2017", check "Visual C++ build tools" and "Universal Windows Platform build tools"
5. ```git clone https://github.com/pybluez/pybluez```
6. ```cd pybluez```
7. ```python setup.py install``` you may need to add --user flag at the end for this to work

once all libraries are installed correctly, then run the python file like this:
8. on Windows connect to ESP32 bluetooth by name, which should be: "ESP32test" then run the below python script
9. ```python C:\Users\lehid\OneDrive\Documents\repos\wireless-networking-project\bt\wav_bt.py C:\Users\lehid\OneDrive\Documents\repos\wireless-networking-project\sounds\```

10. now there should be a complete bluetooth interaction between ESP32 and Windows python script, where ESP32 buttons sends commands like: p,q,n
```
    ESP32: pin playPause = 22; Python: 'p'
    ESP32: pin next = 23; Python: 'n'
    ESP32: pin prev = 21; Python: 'q'
```
PS: Schematic and discussion how this project came to be is found in the BluetoothProjectReport.pdf / FinalProjectSlides.pdf / breadboardSchematic.png file
PS2: add more wav clip sounds from here: https://www.wavsource.com/movies/movies1.htm I have found that it works well with this project.