# ESP32-Beacons-advertising

A simple project that Make ESP32 Module Advertising iBeacon and it can be read by your Raspberry Pi or any BLE Scanner Application.


Additionally to detect BLE devices you need to enable the following:

1. Go to ESP32-Beacons-advertising
 directory that on youy Raspberry Pi

```
cd /lib/systemd/system
```
2. Edit a file
```
sudo vim bluetooth.service
```
Add ```--experimental``` after  ```ExecStart=/usr/local/libexec/bluetooth/bluetoothd```

3. Save and exit vim
Shift + Colon, then type ```wq!``` - to write and quit.

4. Restart daemon
```
sudo systemctl daemon-reload
```
5. Restart bluetooth
```
sudo systemctl restart bluetooth
```

## Quick Start

Download files.

Go to 
```
cd Downloads/ESP32-Beacons-advertising
```
Copy ESP32-ibeacons.c++ file ,and move it into your ESP32 Module
```
Run
```
Back to your Raspberry Pi
```
python Sudo BeaconScanner.py
```
Run


