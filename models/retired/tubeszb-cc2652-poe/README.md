## Zigbee Module Firmware Updates:
This section relates to updating the firmware of the zigbee module. If you have an adapter WITH Ethernet and want to update the firmware of the ESP32 Ethernet module then go back to the top of this page and select the links to the firmware for the product you have. These links also have further information for how to flash the zigbee module and should be read in conjunction with the below https://github.com/tube0013/tube_gateways#current-products

**CC2652p based Gateways:**  
Firmware - use the **CC1352P2_CC2652P_launchpad_*.zip** based firmware available here:  
https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator/Z-Stack_3.x.0/bin

**Both Zigbee2MQTT and ZHA have automatic backups. It is still advised to confirm/save ahead of a FW update **
For ZHA, go to Settings > Devices & Services > ZHA - Cnnfigure and Click Download Backup

For Z2M check he Z2M Config folder for a backup.json or similar named file, and check the date stamp. If not recent shutdown and restart Z2M to generate a more current version.


Use the cc2538-bsl programmer available here: https://github.com/JelmerT/cc2538-bsl

**Ethernet version :**
1. Prep the Module for firmware update:

Click the button to intiate the bootloader mode for the module:

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_web1.png" width="300">

Watch the Debug output and when pompted go to step 2.

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_fw_debuglog.png" width="500">


2. Run the cc2538-bsl programmer:
```
cc2538-bsl.py -p socket://tube_zb_gw_cc2652p2.local:6638  -evw ../CC1352P2_CC2652P_launchpad_20210120.hex
Opening port socket://tube_zb_gw_cc2652p2.local:6638, baud 500000
Reading data from ../CC1352P2_CC2652P_launchpad_20210120.hex
Your firmware looks like an Intel Hex file
Connecting to target...
CC1350 PG2.0 (7x7mm): 352KB Flash, 20KB SRAM, CCFG.BL_CONFIG at 0x00057FD8
Primary IEEE Address: 00:12:4B:00:21:B4:97:D8
    Performing mass erase
Erasing all main bank flash sectors
    Erase done
Writing 360448 bytes starting at address 0x00000000
Write 104 bytes at 0x00057F980
    Write done
Verifying by comparing CRC32 calculations.
    Verified (match: 0xdb4192ef)
```