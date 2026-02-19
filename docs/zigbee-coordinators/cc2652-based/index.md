# CC2652-Based Coordinators

TubesZB CC2652 coordinators use the TI ZNP stack and expose the Zigbee radio over TCP (Ethernet/PoE) or USB. These models work with both ZHA and Zigbee2MQTT.

!!! tip "Start here"
    If you are setting up your coordinator for the first time, begin with the [Getting Started guide for Zigbee coordinators](../../getting-started/zigbee.md).

## Models

| Model | Connection | Radio | ESPHome Builder manifest |
| --- | --- | --- | --- |
| CC2652 PoE 2022 | Ethernet (PoE) | CC2652P2 | [tubeszb-cc2652p2-poe-2022.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-cc2652p2-poe-2022.yaml) |
| CC2652 PoE 2023 | Ethernet (PoE) | CC2652P2 | [tubeszb-cc2652p2-poe-2023.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-cc2652p2-poe-2023.yaml) |
| CC2652 P7 PoE 2023 | Ethernet (PoE) | CC1352P7 | [tubeszb-cc2652p7-poe-2023.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-cc2652p7-poe-2023.yaml) |
| CC2652 Ethernet/USB 2022/2023 | Ethernet or USB | CC2652P2 | [tubeszb-cc2652p2-ethusb-2022.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-cc2652p2-ethusb-2022.yaml) and [tubeszb-cc2652p2-ethusb-2023.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-cc2652p2-ethusb-2023.yaml) |

!!! note "ESPHome configs moved"
    ESPHome YAMLs in this repo are kept for historical reference and are not expected to compile with current ESPHome versions. Use the ESPHome Builder manifests above for active builds.

## Model Highlights

### CC2652 PoE 2022

Photo: [front view](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp)

- PoE powered Ethernet coordinator
- CC2652P2 radio (ZNP)
- TCP port `6638`

### CC2652 PoE 2023

Photo: [front view](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp)

- PoE powered Ethernet coordinator
- CC2652P2 radio (ZNP)
- TCP port `6638`

### CC2652 P7 PoE 2023

Photo: [front view](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp)

- PoE powered Ethernet coordinator
- CC1352P7 radio (ZNP)
- TCP port `6638`

### CC2652 Ethernet/USB 2022/2023

Photo: [closed view](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-eth_usb/images/tubeszb-cc2652-eth_usb_closed.jpg)

- Works over Ethernet or USB
- CC2652P2 radio (ZNP)
- TCP port `6638` when in Ethernet mode

## Power and Safety

PoE models require a PoE switch or injector and at least 37V DC. USB-only models use standard 5V power.

!!! danger "Do not mix power sources"
    Do not connect PoE and USB power at the same time. Doing so can permanently damage the board or your computer.

## ZHA and Zigbee2MQTT Setup

ZHA setup uses the ZNP radio type and connects over TCP or USB.

ZHA over Ethernet:
`socket://IP_ADDRESS:6638`

ZHA over USB:
Use the `/dev/serial/by-id/...` path shown in Home Assistant Hardware.

Zigbee2MQTT over Ethernet:

```yaml
serial:
  port: 'tcp://IP_ADDRESS:6638'
  adapter: zstack
```

Zigbee2MQTT over USB:

```yaml
serial:
  port: '/dev/serial/by-id/usb-1a86_TubesZB_XXXXXXXX-if00-port0'
  adapter: zstack
```

## Firmware Updates

ESP32 firmware updates now use the TubesZB ESPHome Builder and the device web UI or the ESPHome Web Flasher. The standalone ESPHome Flasher app is no longer maintained.

See [Coordinator Firmware Updates](../firmware-updates.md) for the current workflow.

## CC2652 Ethernet/USB Jumper Modes

These images apply to the CC2652 Ethernet/USB coordinator.

Zigbee over Ethernet (serial over TCP):

<figure markdown>
  ![Zigbee to Ethernet jumpers](https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/current/tubeszb-cc2652-eth_usb/images/V2_ZB_2_ETH.JPG){ width="360" }
  <figcaption>Jumpers closest to the female headers route Zigbee to Ethernet.</figcaption>
</figure>

Zigbee over USB:

<figure markdown>
  ![Zigbee to USB jumpers](https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/current/tubeszb-cc2652-eth_usb/images/V2_ZB_2_USB.JPG){ width="360" }
  <figcaption>Middle jumpers route Zigbee to USB.</figcaption>
</figure>

ESP32 flashing mode:

<figure markdown>
  ![ESP32 flashing jumpers](https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/current/tubeszb-cc2652-eth_usb/images/V2_ESP32_2_USB.JPG){ width="360" }
  <figcaption>Jumpers farthest from the female headers route the ESP32 serial to USB.</figcaption>
</figure>

Zigbee over Ethernet with ESP32 debug over USB:

<figure markdown>
  ![Zigbee to Ethernet and ESP32 debug](https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/current/tubeszb-cc2652-eth_usb/images/V2_ZB_2_ETH_and_ESP32_2_USB.JPG){ width="360" }
  <figcaption>Two jumper pairs enable Zigbee over Ethernet while keeping ESP32 debug on USB.</figcaption>
</figure>

## Legacy Models

Retired CC2652 coordinators and legacy instructions are kept in the legacy page.

See [CC2652 Legacy Models](legacy.md).
