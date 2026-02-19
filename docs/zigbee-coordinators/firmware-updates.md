# Coordinator Firmware Updates

TubesZB coordinators have two independent firmwares:

- ESP32 firmware (ESPHome): handles Ethernet/USB bridging, web UI, and diagnostics.
- Zigbee radio firmware: the CC2652/CC1352 or EFR32 radio itself.

!!! warning "Back up before updating"
    Zigbee radio firmware updates erase the coordinator state. ZHA and Zigbee2MQTT both create automatic backups, but confirm you have a recent backup before updating.

## ESP32 Firmware (ESPHome)

ESPHome firmware is now built in the **TubesZB ESPHome Builder**. The standalone ESPHome Flasher app is no longer maintained and is not recommended.

### Recommended: Update from the device web UI

Modern TubesZB firmware supports updating directly from the coordinator without any external program.

1. Open the coordinator web UI at `http://IP_ADDRESS`.
2. Use the **Update** or **Firmware** option in the UI.
3. Upload the new `.bin` from the TubesZB ESPHome Builder.
4. Wait for the device to reboot and reconnect.

### Web flasher (USB)

If you need to flash over USB or recover a device, use the ESPHome Web Flasher:

1. Build or download the firmware `.bin` from the TubesZB ESPHome Builder.
2. Open `https://web.esphome.io` in a Chromium-based browser.
3. Connect the coordinator over USB and select the correct serial device.
4. Choose the `.bin` file and flash.

!!! tip "When to use the web flasher"
    Use the web flasher for first-time installs, recovery, or when the device web UI is unavailable.

## Zigbee Radio Firmware (CC2652/CC1352)

CC2652 and CC1352 radios update over the same TCP or USB path used for Zigbee traffic.

1. Download a coordinator firmware from the Z-Stack repository.
https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator/Z-Stack_3.x.0/bin
2. Install the cc2538-bsl flasher.
https://github.com/JelmerT/cc2538-bsl

### Ethernet update (PoE or Ethernet/USB in Ethernet mode)

1. Open the coordinator web UI at `http://IP_ADDRESS`.
2. Trigger the Zigbee bootloader from the web UI. The toggle is labeled "Trigger Zigbee Module Bootloader" or "Prep CC2652 for firmware" depending on the firmware build.
3. Run the flasher:

```bash
cc2538-bsl.py -p socket://IP_ADDRESS:6638 -evw path_to_firmware/CC1352P2_CC2652P_launchpad_coordinator_YYYYMMDD.hex
```

For CC2652 P7 models, use a `CC1352P7_coordinator_*.hex` firmware file.

### USB update (Ethernet/USB model in USB mode)

1. Hold the BSL button while plugging the USB cable in.
2. Run the flasher:

```bash
cc2538-bsl.py -p /dev/serial/by-id/usb-1a86_TubesZB_XXXXXXXX-if00-port0 -evw path_to_firmware/CC1352P2_CC2652P_launchpad_coordinator_YYYYMMDD.hex
```

Windows users may need the CH340 USB serial driver for USB flashing.
