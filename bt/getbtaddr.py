'''
Setting up pybluez on windows: 

I successfully installed pybluez for Windows 10 with Python 3.7.

Download and run "Visual Studio Installer": https://www.visualstudio.com/pl/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
Install "Visual Studio Build Tools 2017", check "Visual C++ build tools" and "Universal Windows Platform build tools"
git clone https://github.com/pybluez/pybluez
cd pybluez
python setup.py install
'''

import bluetooth as bt
from pprint import pprint
import pdb; pdb.set_trace()

devices = bt.discover_devices()
#   now you get the device BT address and put it in the command below to find the port you need to use in this script
devices
service = bt.find_service(address='00:yy:72:zz:bb:aa')
pprint(service)