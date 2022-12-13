# wireless-networking-project
Wireless Networking Project

The file to push to ESP32 is located at: wireless-networking-project/bt/ESP32BluetoothReceivingData/ESP32BluetoothReceivingData.ino
The file to be ran on a Windows 11 + is located at: wireless-networking-project/bt/wav_bt.py. You need python 3 and bluetooth library, follow these steps to make sure you have the correct python libraries:

1. Download and run "Visual Studio Installer": https://www.visualstudio.com/pl/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
2. Install "Visual Studio Build Tools 2017", check "Visual C++ build tools" and "Universal Windows Platform build tools"
3. git clone https://github.com/pybluez/pybluez
4. cd pybluez
5. python setup.py install

once all libraries are installed correctly, then run the python file like this:

