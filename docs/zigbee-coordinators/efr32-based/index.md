# EFR32-Based Coordinators

TubesZB EFR32 coordinators use Silicon Labs EZSP (Ember) radios and expose the Zigbee interface over TCP (Ethernet/PoE) or USB depending on model. These models work with ZHA and Zigbee2MQTT.

!!! tip "Start here"
    If you are setting up your coordinator for the first time, begin with the [Getting Started guide for Zigbee coordinators](../../getting-started/zigbee.md).

## Models

| Model | Connection | Radio | Photo | ESPHome Builder manifest |
| --- | --- | --- | --- | --- |
| EFR32 MGM210 PoE 2022/2023 | Ethernet (PoE) | EZSP | [enclosure reference](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp) | [tubeszb-efr32-mgm210-poe-2022.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-efr32-mgm210-poe-2022.yaml) and [tubeszb-efr32-mgm210-poe-2023.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-efr32-mgm210-poe-2023.yaml) |
| EFR32 MGM24 2023 | Ethernet (PoE) | EZSP | [connection diagram](https://github.com/tube0013/tube_gateways/raw/main/images/efr32_connection.png) | [tubeszb-efr32-mgm24-2023.yaml](https://github.com/tube0013/TubesZB-ESPHome-Builder/blob/main/manifests/tubeszb-efr32-mgm24-2023.yaml) |
| EFR32 MGM12 2022 | Ethernet or USB | EZSP | [front view](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-efr32-MGM12-eth_usb/images/tubeszb-efr32-MGM12P-eth_usb.webp) | Not yet in the ESPHome Builder manifests |

!!! note "ESPHome configs moved"
    ESPHome YAMLs in this repo are kept for historical reference and are not expected to compile with current ESPHome versions. Use the ESPHome Builder manifests when available.

## Model Highlights

### EFR32 MGM210 PoE 2022/2023

Photo: [enclosure reference](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp)

- PoE powered Ethernet coordinator
- EZSP radio
- TCP port `6638`

### EFR32 MGM24 2023

Photo: [connection diagram](https://github.com/tube0013/tube_gateways/raw/main/images/efr32_connection.png)

- PoE powered Ethernet coordinator
- EZSP radio
- TCP port `6638`

### EFR32 MGM12 2022

Photo: [front view](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-efr32-MGM12-eth_usb/images/tubeszb-efr32-MGM12P-eth_usb.webp)

- Ethernet or USB connectivity
- EZSP radio
- TCP port `6638` when in Ethernet mode

## ZHA and Zigbee2MQTT Setup

ZHA setup uses the EZSP radio type and connects over TCP or USB.

ZHA over Ethernet:
`socket://IP_ADDRESS:6638`

ZHA over USB:
Use the `/dev/serial/by-id/...` path shown in Home Assistant Hardware.

Zigbee2MQTT over Ethernet:

```yaml
serial:
  port: 'tcp://IP_ADDRESS:6638'
  adapter: ember
```

Zigbee2MQTT over USB:

```yaml
serial:
  port: '/dev/serial/by-id/usb-1a86_TubesZB_XXXXXXXX-if00-port0'
  adapter: ember
```

!!! note "Zigbee2MQTT firmware requirement"
    Zigbee2MQTT requires EFR32 coordinator firmware 7.4.x or newer.

## Firmware Updates

ESP32 firmware updates now use the TubesZB ESPHome Builder and the device web UI or the ESPHome Web Flasher. The standalone ESPHome Flasher app is no longer maintained.

See [Coordinator Firmware Updates](../firmware-updates.md) for the current workflow.

## Legacy Settings and Jumpers

Legacy EFR32 settings and jumper references are documented separately.

See [EFR32 Legacy Reference](legacy.md).
