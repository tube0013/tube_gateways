# TubesZB CC2652P2 Zigbee Router

This page contains technical details for the TubesZB CC2652P2 Zigbee Router, including factory reset and firmware update procedures.

---

## Device Operations

### Factory Reset

If you need to re-pair the router or start fresh, you can perform a factory reset.

1.  Carefully open the router's enclosure to access the circuit board.
2.  Locate the small button labeled **BSL** (Boot Strap Loader).
3.  With the router powered on, give the **BSL** button a single, quick press.

The device will reset and should immediately enter pairing mode again.

---

## Firmware Updates

Updating the firmware on the CC2652P2 module requires a physical connection to a computer and the use of a specific flashing tool.

**Required Tool:** [cc2538-bsl.py](https://github.com/JelmerT/cc2538-bsl)

The flashing process differs slightly depending on whether your router has a USB-C or a Micro-USB port.

### Flashing a Router with a USB-C Port

Newer routers with a USB-C port have a built-in serial-to-USB converter, which simplifies the process.

1.  Press and hold the **BSL** button on the router's circuit board.
2.  While still holding the button, plug the router into your computer using a USB-C cable.
3.  Continue holding the BSL button for about 10 seconds, then release. The device is now in bootloader mode.
4.  Use the `cc2538-bsl.py` tool to flash the new firmware.

### Flashing a Router with a Micro-USB Port

Older routers with a Micro-USB port require an external USB-to-Serial adapter for flashing.

!!! warning "Serial Adapter Required"
    You will need a 3.3V USB-to-Serial TTL adapter to flash this device. Adapters using CP210x, CH340, or FTDI chips are common and will work.
    * [Example CP2102 USB to TTL module (Affiliate Link)](https://amzn.to/3HjQ7bx)

#### Flashing Steps

1.  **Connect the Adapter:** Use dupont jumper wires to connect your serial adapter to the router's programming pins. The connection order is critical:

| Serial Adapter | Router Pin |
| :------------- | :--------- |
| 3.3V           | 3.3V       |
| GND            | GND        |
| RX             | TX         |
| TX             | RX         |

2.  **Enter Bootloader Mode:**
    * Plug the USB-to-Serial adapter into your computer.
    * Press and hold the **BSL** button on the router.
    * While holding the button, slide the 4 connected dupont wires over the corresponding pins on the router.
    * Release the BSL button. The device is now in bootloader mode.

3.  **Flash the Firmware:** Use the `cc2538-bsl.py` tool to flash the new firmware.

    [![TubesZB Router FW Update Wiring Setup](https://github.com/tube0013/tube_gateways/raw/main/images/youtube--OCORSnwCDtw-c05b58ac6eb4c4700831b2b3070cd403.jpeg)](https://youtu.be/OCORSnwCDtw "TubesZB Router FW Update Wiring Setup")

#### Example Flash Command

The command will look similar to this. Replace the port and file path with your own.

```bash
cc2538-bsl.py -p /dev/cu.usbserial-00F9450F -evw /PATH_TO/tubeszb_router_20220111.hex