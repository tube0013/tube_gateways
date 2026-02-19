# EFR32 Legacy Reference

This page captures legacy settings and jumper references for retired EFR32-based coordinators.

!!! note "Historical reference only"
    These settings apply to older 6.9.x firmware and pre-2021 Home Assistant builds. Current models usually do not need them.

## Legacy Jumper Reference (EFR32 Pro and Series 2)

Zigbee serial routed to Ethernet (ESP32):

<figure markdown>
  ![EFR32 Zigbee to Ethernet](https://github.com/tube0013/tube_gateways/raw/main/images/efr32_ztoeth.png){ width="360" }
  <figcaption>Jumpers toward the ESP32 route Zigbee serial to Ethernet.</figcaption>
</figure>

Zigbee serial routed to the onboard USB serial adapter:

<figure markdown>
  ![EFR32 Zigbee to Serial](https://github.com/tube0013/tube_gateways/raw/main/images/efr32_ztos.png){ width="360" }
  <figcaption>Middle jumpers route Zigbee serial to the USB adapter.</figcaption>
</figure>

ESP32 flashing mode:

<figure markdown>
  ![EFR32 ESP32 flashing](https://github.com/tube0013/tube_gateways/raw/main/images/efr32_espflash.png){ width="360" }
  <figcaption>Ground IO0 during boot to enter ESP32 flash mode.</figcaption>
</figure>
