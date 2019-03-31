'''
  https://stackoverflow.com/questions/7485750/sending-messages-or-datas-with-bluetooth-via-python
  >>> from bluetooth import *
  >>> from pprint import pprint
  >>> devices = discover_devices()
  now you get the device BT address and put it in the command below to find the port you need to use in this script
  >>> devices
  >>> service = find_service(address='00:yy:72:zz:bb:aa')
  >>> pprint(service)
  good reference for python receiving data: https://pymotw.com/2/socket/tcp.html
  good reference for arduino bluetooth writing to BT Serial and regular Serial: https://github.com/espressif/arduino-esp32/blob/master/libraries/BluetoothSerial/examples/SerialToSerialBT/SerialToSerialBT.ino
'''

#!/usr/bin/python
 
import bluetooth
import sys

def connect ():
    bd_addr = "30:AE:A4:D4:8D:52"
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    # sock.send("hello")
    # sock.close()

    try:
        # Send data
        message = 'This is the message.  It will be repeated.'
        # print(sys.stderr, 'sending "%s"' % message)
        sock.send(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(sys.stderr, 'received "%s"' % data)

    finally:
        print(sys.stderr, 'closing socket')
        sock.close()

connect()