# TubesZB CC2652 PoE Coordiniator

<p float="left">
 <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp" width="300" height = "300">
 <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022_open.webp" width="300" height="300">
 </p>

 Available to purchase at the [TubesZB Store](https://www.tubeszb.com/product/cc2652_coordinator/47) 

## Power Rquirement
PoE switch or Injector required to power

IEEE 802.3-compliant, including pre-standard (legacy) PoE support. The PoE powering requires at least 37V DC to operate successfully

**_Do Not connect PoE and USB (internal USB port on Olime module) at the same time - you will burn out the board or computer or both!_**

## ESP32 Flashing

*Note currently ESPHome Releases 2021.10 do not have reliable serial connections to the zigbee module exhibiting in frequent (every few hours) disconnections.*

Firmware is available in the [firmware directory for this model](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-cc2652-poe=2022/firmware/esphome).

Recommend the ESPHome Flasher tool:
https://github.com/esphome/esphome-flasher/releases

Windows will require the CH340 Serial driver. I version can be found [downloaded here](https://www.olimex.com/Products/Breadboarding/BB-CH340T/resources/CH341SER.zip)

Partially removed the board from the case to access the microUSB port on the Olimex ESP32-PoE module. Use a USB cable (not power only) to connect the the board to the computer doing the flashing. Reminder do not connect USB and Powered ethernet concurrently.


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

Retry the above steps if bootloader mode is not detected by the script:

```
ERROR: Timeout waiting for ACK/NACK after 'Synch (0x55 0x55)'
```

Another option is to trigger the bootloader manually, to do this, pop the top with the device unpowered, hold down the BSL button while plugging in power, it's important to hold it for several seconds as the ESP32 will trigger a reset of the zigbee module after it boots. Then try the update script again



