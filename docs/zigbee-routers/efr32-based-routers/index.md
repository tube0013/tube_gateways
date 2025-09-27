# EFR32 Based Zigbee Router

This page contains technical details for the Tube's EFR32 based Zigbee Routers, including button functions and firmware update procedures.

---

## Getting Started

Initial pairing is simple and works the same way as other TubeZB routers. Please follow the main router getting started guide for instructions.

[:octicons-arrow-right-24: View Router Getting Started Guide](../../getting-started/router.md)

---

## Device Operations

The single button on the EFR32 router has multiple functions depending on the state of the device and the duration of the press.

!!! tip "Settings are Temporary"
    Toggled statuses from a short button press (like network steering) only remain active while the router is powered on. Power cycling the router will reset it to its default behavior.

### If the Router is NOT Joined to a Network:

* **Short Press:** Toggles "Network Steering". This starts or stops the router's attempt to find and join a Zigbee network. This is useful if you want to power on the device without it immediately trying to pair.
* **Long Press (>5s):** Reboots the router into bootloader mode. This is used to prepare the device for a firmware update.

### If the Router IS Joined to a Network:

* **Short Press:** Toggles "Source Route Discovery". This is an advanced feature that is generally not needed for most networks. It starts/stops the broadcasting of MTORRs (Many-to-One Route Requests).
* **Long Press (>5s):** Makes the router leave its current Zigbee network. It will need to be re-paired after this action.

---

## Firmware Updates

### Firmware Source

The recommended firmware for these routers is developed by Nerivec and is available for download from the **[silabs-firmware-builder releases page](https://github.com/Nerivec/silabs-firmware-builder/releases)**.

### Flashing Methods

There are two primary methods for flashing firmware to the EFR32 routers.

#### Method 1: Universal Silicon Labs Flasher (Advanced)

This is a Python-based command-line tool for flashing Silicon Labs devices. It is a powerful tool for users who are comfortable working in a terminal.

1.  **Install the Tool:** Follow the installation instructions on the **[Universal Silicon Labs Flasher GitHub page](https://github.com/NabuCasa/universal-silabs-flasher/)**.
2.  **Enter Bootloader Mode:** Before flashing, you must put the router into bootloader mode. While the device is powered on, press and hold the button for more than 5 seconds until the LED changes.
3.  **Run the Flasher:** Use the tool to flash the downloaded firmware file. The command will look something like this:
    ```bash
    universal-silabs-flasher --device /dev/tty.usbmodem1101 flash --firmware your-firmware-file.gbl
    ```

#### Method 2: Tube's Home Assistant Addon (Recommended for HA Users)

For users running Home Assistant OS or Supervised, the easiest method is to use the TubesZB Addon, which provides a user-friendly interface for flashing.

1.  Install the **[TubesZB Addon Repository](https://github.com/tube0013/tubeszb_addons)** in Home Assistant.
2.  Install the appropriate flashing utility from the addon store.
3.  Follow the instructions within the addon's documentation to flash your router.