## Zigbee Module Firmware Updates:
This section relates to updating the firmware of the zigbee module. If you have an adapter WITH Ethernet and want to update the firmware of the ESP32 Ethernet module then go back to the top of this page and select the links to the firmware for the product you have. These links also have further information for how to flash the zigbee module and should be read in conjunction with the below https://github.com/tube0013/tube_gateways#current-products

**CC2652p based Gateways:**  
Firmware - use the **CC1352P2_CC2652P_launchpad_*.zip** based firmware available here:  
https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator/Z-Stack_3.x.0/bin

**Both Zigbee2MQTT and ZHA have automatic backups. It is still advised to confirm/save ahead of a FW update **
For ZHA, go to Settings > Devices & Services > ZHA - Cnnfigure and Click Download Backup

For Z2M check he Z2M Config folder for a backup.json or similar named file, and check the date stamp. If not recent shutdown and restart Z2M to generate a more current version.


Use the cc2538-bsl programmer available here: https://github.com/JelmerT/cc2538-bsl
(Please note the Dependecies called out on the cc2538-bsl main page: https://github.com/JelmerT/cc2538-bsl#dependencies )


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

## ESP32 Serial Flash

You will need an Serial to USB TTL adaptor - I use one similar to this one and it works well: [HiLetgo CP2102 USB to TTL UART](https://amzn.to/44PcsrF)


Grab the current esp fw bin file: https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-cc2652-eth/firmware/esphome

I use the esphome flasher tool which works well for me:
https://github.com/esphome/esphome-flasher/releases

you’ll need 3 jumper wires, the board has pins, so will need females on that end and female/male on the other depending on your Serial TTL adaptor board.

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esp_flash_wires.jpg" width="400">


TX on the Serial TTL adaptor goes to the eRX pin on the board (red wire in pic)

RX on the Serial TTL adaptor goes to the eTX pin on the board (orange wire in pic)

Ground from the Serial TTL adaptor goes to the Ground pin on the board (closest to 3.3v) (brown wire in pic)

Use the jumper from the 3.3v_Bridge on the board (or another female to female jumper wire) to bridge the ground and IO0 pins (the spacing is tight I found tweezer so pinch nosed pliers best for adding the jumper)

Once all that is connected up, power on by plugging in the micro usb or by using a 4th jumper wire to connect the 3.3 volts on the Serial TTL adaptor to the 3.3v pin on the board.

## Flashing

Fire up the flasher and select the correct port and point it to the downloaded FW bin:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_1.jpg" width="400">


Hit flash, and you should see something like this:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_2.jpg" width="400">


after about a minute or so:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_3.jpg" width="400">

pull the power, and move the jumper back to the 3.3v_Bridge. you can leave the cables connected to do a test boot with serial logging if you want. Just plug it back in, and hit the show logs button in the flasher:

you should see something like this if not connected to ethernet, or maybe on it’s first try of connecting:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_4.jpg" width="400">


if connected to network, should see something like this:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_5.jpg" width="400">

