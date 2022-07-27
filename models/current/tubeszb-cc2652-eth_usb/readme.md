## TubesZB CC2652 Ethernet/USB Coordiniator

<p float="left">
 <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-eth_usb/images/tubeszb-cc2652-eth_usb_closed.jpg" width="300" height = "300">
 <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-eth_usb/images/tubeszb-cc2652-eth_usb_open.jpg" width="300" height="300">
 </p>

 Available to purchase at the [TubesZB Store](https://www.tubeszb.com/product/cc2652_coordinator/39) 


 This is the second version of the TubesZB CC2652 Ethernet Coordinator. It takes the place of both the Original CC2652 Ethernet Coordninator and the Original TubesZB USB Coordinator as it can be bought/made with or without ethernet. For the USB only variation ethernet can be added at a later time. Adding it is shown in this short YouTube video: https://youtu.be/qbWw0O2dzP0

***

## Jumper Discriptions:

### Zigbee connection over Ethernet (Serial over TCP):

Jumpers positioned on the 2 header pins closes to the Female headers for the WT032-E01 ESP32 module:

<img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/V2_tube_zb_gw_cc2652p2/V2_ZB_2_ETH.JPG" width="300">

---

### Zigbee connection via USB:

Jumpers positions on the middle 2 header pins:

<img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/V2_tube_zb_gw_cc2652p2/V2_ZB_2_USB.JPG" width="300">

---

### ESP32 Flashing Mode - ESP32 serial connection via USB:

Jumpers positons on the 2 headers pins furthest from the female headers:

<img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/V2_tube_zb_gw_cc2652p2/V2_ESP32_2_USB.JPG" width="300">

---

### Zigbee over Ethernet with ESP32 Debug over USB access:

2 pairs of jumpers side by side:

<img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/V2_tube_zb_gw_cc2652p2/V2_ZB_2_ETH_and_ESP32_2_USB.JPG" width="300">


## ESP32 Flashing

Firmware is available in the [firmware directory for this model](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-cc2652-eth_usb/firmware/esphome).

Recommend the ESPHome Flasher tool:
https://github.com/esphome/esphome-flasher/releases

Windows will require the CH340 Serial driver. I version can be found [downloaded here](https://www.olimex.com/Products/Breadboarding/BB-CH340T/resources/CH341SER.zip)

Move the jumpers to the ESP32 Flashing mode as described above.

Press and hold the button labeled BOOT on the main pcb board while plugging the USB into the computer that will be flashing the device.

After the flashing completes you can tap the ERST button to do a first boot of the new FW while showing the console in the flashing tool window to confirm it was flashed okay.


## CC2652 Firmware Flashing

Firmware - use the **CC1352P2_CC2652P_launchpad_*.zip** based firmware available here:  
https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator/Z-Stack_3.x.0/bin

**Be sure you have a current backup of your coordinator before flashing as the update will erase the zigbee module completely** 

Zigbee2MQTT should automatically create a backup on Startup, so start and stop Z2M one time to be sure it is current. Check your z2m config folder for the backup json before flashing.

ZHA will be getting built in Backups in Home Assistant in the very near future (as of late July 2022 - https://github.com/home-assistant/core/pull/75791 ), until then:

https://github.com/zigpy/zigpy-znp/blob/dev/TOOLS.md#backup-and-restore


The cc2538-bsl programmer available here: 
https://github.com/JelmerT/cc2538-bsl


### USB
Move jumpers to Zigbee to USB mode as shown above.

Windows will require the CH340 Serial driver. I version can be found [downloaded here](https://www.olimex.com/Products/Breadboarding/BB-CH340T/resources/CH341SER.zip)

1. Hold the BSL button while plugging in the usb cable.
2. Run the cc2538-bsl flasher:
```
cc2538-bsl.py -p /dev/serial/by-id/usb-1a86_TubesZB_971207DO-if00-port0 -evw path_to_firmware_file/CC1352P2_CC2652P_launchpad_coordinator_20220219.hex
```
Note firmware file name will be different depending on version

3. Confirm the successful flash via the out put from the cc2638-bsl.py script:
```
Verifying by comparing CRC32 calculations.
    Verified (match: 0xddfc152d)
```

### Network
Jumpers in Zigbee to Ethernet mode as shown above

1. Go to the Coordinators web console in your browser - http://coordinatore_ip_address

2. Click the Prep cc2652 for firmware toggle in the web interface - the console will show a message after ~ 10 seconds

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_web1.png" width="300">

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_fw_debuglog.png" width="500">


3. Run the cc2538-bsl flasher
```
cc2538-bsl.py -p socket://IP:6638 path_to_firmware_file/CC1352P2_CC2652P_launchpad_coordinator_20220219.hex
```
Note firmware file name will be different depending on version
Flashing over network serial will take approxiamately 5 minutes.

4. Confirm the successful flash via the out put from the cc2638-bsl.py script:
```
Verifying by comparing CRC32 calculations.
    Verified (match: 0xddfc152d)
```




