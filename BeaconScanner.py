#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import ScanUtility
import bluetooth._bluetooth as bluez
import time

#Set bluetooth device. Default 0.
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print ("\n *** Looking for BLE Beacons ***\n")
	print ("\n *** CTRL-C to Cancel ***\n")
except:
	print ("Error accessing bluetooth")

#ScanUtility.hci_enable_le_scan(sock)
#Scans for iBeacons
try:
    while True:
        ScanUtility.hci_enable_le_scan(sock)
        returnedList = ScanUtility.parse_events(sock, 10)
        major = returnedList[0]["major"]
        minor = returnedList[0]["minor"]
        for item in returnedList:
            print(item)
            print("")
        if ((int(major) == 1) and (int(minor) ==2)) :
            print("Seems you around ,come to try our the 20% sales")
        time.sleep(5)
except KeyboardInterrupt:
    pass
