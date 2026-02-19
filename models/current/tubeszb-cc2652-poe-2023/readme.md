# TubesZB CC2652 PoE Coordinator

## Notice

The ESPHome configs for this device are superseded by the TubesZB-ESPHome-Builder repository.
Manifest filename: `tubeszb-cc2652p2-poe-2023.yaml`
- [tubeszb-cc2652p2-poe-2023.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-cc2652p2-poe-2023.yaml)

<p float="left">
 <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp" width="300" height = "300">
 <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022_open.webp" width="300" height="300">
 </p>

 Available to purchase at the [TubesZB Store](https://tubeszb.com/product/cc2652p2-based-zigbee-to-poe-coordinator-2023/) 

## Power Requirement
PoE switch or Injector required to power

IEEE 802.3-compliant, including pre-standard (legacy) PoE support. The PoE powering requires at least 37V DC to operate successfully

🔴 **_Do Not connect PoE and USB (internal USB port) at the same time - you will burn out the board or computer or both!_** 🔴

## ESP32 Flashing

Firmware is available in the [firmware directory for this model](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-cc2652-poe-2023/firmware/esphome).

Recommend the ESPHome Flasher tool:
https://github.com/esphome/esphome-flasher/releases

Windows will require the CH340 Serial driver. A version can be found [downloaded here](https://www.olimex.com/Products/Breadboarding/BB-CH340T/resources/CH341SER.zip)

Partially removed the board from the case to access the microUSB port on the Olimex ESP32-PoE module. Use a USB cable (not power only) to connect the the board to the computer doing the flashing. Reminder do not connect USB and Powered ethernet concurrently.


After the flashing completes the esp32 will automatically reset and boot the new FW while showing the console in the flashing tool window to confirm it was flashed okay.


## CC2652 Firmware Flashing

Firmware - use the **CC1352P2_CC2652P_launchpad_*.zip** based firmware available here:  
https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator/Z-Stack_3.x.0/bin

**Be sure you have a current backup of your coordinator before flashing as the update will erase the zigbee module completely** 

Zigbee2MQTT should automatically create a backup on Startup, so start and stop Z2M one time to be sure it is current. Check your z2m config folder for the backup json before flashing.

ZHA Also takes periodic auto backups and will restore the last one automatically when the zha is restarted after an update. you can also download a backup from the ZHA configuration page.

https://github.com/zigpy/zigpy-znp/blob/dev/TOOLS.md#backup-and-restore


The cc2538-bsl programmer available here: 
https://github.com/JelmerT/cc2538-bsl

(Please note the Dependecies called out on the cc2538-bsl main page: https://github.com/JelmerT/cc2538-bsl#dependencies )


### USB

USB can be used to flash the cc2652 module if you have an external USB to serial adapter and dupont connector cables.

(More details coming)

### Network

1. Go to the Coordinators web console in your browser - http://coordinatore_ip_address

2. Click the `Trigger Zigbee Module Bootloader` toggle in the web interface - the console will show a message after ~ 10 seconds

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_web2.png" width="300">

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_fw_debuglog.png" width="500">


3. Run the cc2538-bsl flasher
```
cc2538-bsl.py -p socket://IP:6638 -evw path_to_firmware_file/CC1352P2_CC2652P_launchpad_coordinator_20220219.hex
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


