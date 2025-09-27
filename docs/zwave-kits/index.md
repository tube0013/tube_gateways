# Z-Wave PoE Kit

<figure markdown>
  ![Z-Wave PoE Kit](https://tubeszb.com/wp-content/uploads/2024/01/img_3540-768x1024.jpeg){ width="400" }
</figure>

The TubeZB Z-Wave PoE Kit provides a reliable, network-connected Z-Wave radio for Home Assistant. It is powered by Power over Ethernet (PoE) and uses an ESP32 microcontroller to bridge the Z-Wave serial module to your network.

---

## Getting Started

For initial setup and integration with Home Assistant, please follow the main Z-Wave getting started guide.

[:octicons-arrow-right-24: View Z-Wave Getting Started Guide](../getting-started/z-wave.md)

---

## Hardware Components

The Z-Wave PoE Kit consists of two main printed circuit boards (PCBs):

1.  **Olimex ESP32-PoE Board:** This is the brains of the device. It's an ESP32 development board that includes a built-in PoE module, allowing it to be powered directly from a compatible network switch or injector. It runs a custom ESPHome firmware to manage the network connection and communication with the Z-Wave radio.

2.  **Raspberry Pi GPIO to Olimex UEXT Converter:** This is a custom adapter board designed specifically to connect Z-Wave modules with a Raspberry Pi GPIO-style header to the Olimex board's UEXT connector. You can find more details on the [converter's product page](https://tubeszb.com/product/raspberry-pi-gpio-to-olimex-uext-for-z-wave-adaptors/).

### 3D Printed Enclosure

For those who wish to print their own case, the STL files are available on GitHub.

[:octicons-file-zip-16: Download Case STL Files](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-zw-kit/Case)

---

## Firmware Updates

There are two separate firmwares on this device that can be updated: the **ESPHome firmware** on the ESP32, and the **firmware on the Z-Wave radio module** itself.

### ESPHome Firmware (ESP32)

The ESPHome firmware handles the network connectivity. You can update it using the web-based flashing tool. For advanced users, the base ESPHome YAML configuration is also available.

- **[View the current ESPHome YAML Configuration](https://raw.githubusercontent.com/tube0013/TubesZB-ESPHome-Builder/refs/heads/main/manifests/tubeszb-zw.yaml)**

#### Flashing Instructions

1.  **Disconnect PoE Power:**
    !!! danger "CRITICAL SAFETY WARNING"
        You **MUST** unplug the ethernet cable providing PoE before connecting the device to your computer via USB. Failure to do so can permanently damage the USB port on the ESP32 board and potentially the USB controller on your computer.

2.  **Access the USB Port:**
    * Remove the lid from the 3D-printed enclosure.
    * Gently lift the end of the boards near the ethernet port to pivot the assembly upwards. This will expose the micro-USB port on the Olimex ESP32-PoE board.

3.  **Connect to Computer:**
    * Connect a micro-USB data cable from the ESP32 board to your computer.

4.  **Flash the Firmware:**
    * **For standard DHCP firmware:** Use the **[TubesZB Web Flasher](https://tube0013.github.io/TubesZB-ESPHome-Builder/)**. Select "TubesZB ZWave Kit" from the dropdown and follow the on-screen instructions to connect and flash.
    * **For a static IP:** You must first build a custom firmware binary. Go to the **[TubesZB ESPHome Builder repository](https://github.com/tube0013/TubesZB-ESPHome-Builder)** and create a new issue using the "ESPHome Static IP Configuration" template. Fill out your network details, and a GitHub Action will automatically compile a firmware for you to download and flash.

### Z-Wave Radio Firmware

Updating the firmware on the Z-Wave radio module itself depends on the model you are using.

#### Zooz ZAC93 Module

The firmware on the Zooz ZAC93 module can be updated directly through the Z-Wave JS UI in Home Assistant.

1.  Obtain the correct firmware file from the **[Zooz OTA Firmware Files page](https://www.support.getzooz.com/kb/article/1158-zooz-ota-firmware-files/)**.
2.  In the Z-Wave JS UI, navigate to the **Control Panel**.
3.  Select your Zooz controller node.
4.  Expand the **Advanced** actions.
5.  Under **Firmware update**, upload the file and begin the process.

#### Z-Wave.me RaZberry 7 Pro Module

Updating the RaZberry module is a more advanced process that currently requires a Raspberry Pi.

1.  Safely shut down your Z-Wave PoE Kit and remove the RaZberry module.
2.  Install the RaZberry module onto the GPIO header of a Raspberry Pi.
3.  Download and install the **[Z-Way software](https://z-wave.me/z-way/download-z-way/)** from Z-Wave.me on the Raspberry Pi.
4.  Access the Z-Way Expert UI in your browser.
5.  Use the built-in firmware update tool within the Expert UI to flash the new firmware onto the module.
6.  Once complete, remove the module from the Raspberry Pi and reinstall it in your Z-Wave PoE Kit.