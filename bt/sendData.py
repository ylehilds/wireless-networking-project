'''
  https://stackoverflow.com/questions/7485750/sending-messages-or-datas-with-bluetooth-via-python
  >>> from bluetooth import *
  >>> from pprint import pprint
  >>> devices = discover_devices()
  now you get the device BT address and put it in the command below to find the port you need to use in this script
  >>> devices
  >>> service = find_service(address='00:yy:72:zz:bb:aa')
  >>> pprint(service)
'''

#!/usr/bin/python

import bluetooth

def connect ():
    bd_addr = "30:AE:A4:D4:8D:52"
    port = 1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("hello!!")
    sock.close()

connect()