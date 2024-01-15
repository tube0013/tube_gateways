# Tube's Router

Device should go into pairing mode as soon as it is powered up for the first time.

To factory reset, open case (it's a friction fit) and a single press of the BSL button will reset the device.

FW Updates require the use of a serial to usb converter.
hold the BSL button when powering the device, keep it held for ~10 seconds to get the device into bootloader mode. Release the button and then use the Use the cc2538-bsl programmer available here: https://github.com/JelmerT/cc2538-bsl to update the FW. if it stalls or fails just repeat.

Devices shipped in 2021 are flashed with Firmware from the Z-Stack Router FW Repository: https://github.com/Koenkk/Z-Stack-firmware/tree/master/router/Z-Stack_3.x.0/bin  specfically the CC1352P2_CC2652P_launchpad_router_* FW.

In 2022 I made some tweaks to the FW and it can be found here along with the changes described: https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-router/firmware

## Flashing the Router

To flash new firmware onto the router you will need a USB to Serial adaptor. Something like this will work well and is similar to the ones I uses: [CP2102 USB to TTL modules](https://amzn.to/3HjQ7bx) Note generally you can find adaptors with the cp210x, ch340 for FTDI chips. most are supported fine on Linux or Mac but you may need drivers for Windows.

Just with the coordinator firmware you'll need the cc2538-bsl programmer available here: https://github.com/JelmerT/cc2538-bsl

Using the dupont jumper wires, connect them to the serial adaptor using the 3.3v, GND, RX and TX pins. line up the other end of the wires so that they are in the GND,TX,RX,3.3v order. these will connect to the router's GND,RX,TX, and 3.3v pins.

With the USB cto serial adaptor plugged into a computer, hold the 4 dupont connectors together lined up in order. Hold the BSL button down while sliding the 4 connectors over the pins on the board.


[![TubesZB Router FW Update Wiring Setup](https://github.com/tube0013/tube_gateways/raw/main/images/youtube--OCORSnwCDtw-c05b58ac6eb4c4700831b2b3070cd403.jpeg)](https://youtu.be/OCORSnwCDtw "TubesZB Router FW Update Wiring Setup")


At this point the cc2652 module should be in bootloader mode, and flashing can be done with the cc2538-bsl tool.

```cc2538-bsl.py -p /dev/cu.usbserial-00F9450F -evw /PATH_TO/tubeszb_router_20220111.hex```