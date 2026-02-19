# Zigbee Coordinators

TubesZB coordinators provide a reliable Ethernet or USB bridge between your Zigbee radio and Home Assistant or Zigbee2MQTT. The two platform families below cover different radio stacks while sharing the same setup flow.

## [EFR32 Platform (Silicon Labs EZSP)](efr32-based/index.md)

EFR32 radios use the Silicon Labs EZSP/Ember stack. They are supported by both ZHA and Zigbee2MQTT and are a strong choice for modern Zigbee networks.

- ZHA radio type: **EZSP**
- Zigbee2MQTT adapter: **ember**

### MGM24

- 2.4 GHz radio
- TX power up to +19.9 dBm
- 32-bit ARM Cortex-M33, 78 MHz
- 1536 KB flash program memory
- 256 KB RAM data memory

### MGM21

- 2.4 GHz radio
- TX power up to +20 dBm
- 32-bit ARM Cortex-M33 with DSP instructions and floating point unit
- 1024 KB flash program memory
- 96 KB RAM data memory
- Embedded Trace Macrocell (ETM) for advanced debugging

### MGM12

- 32-bit ARM Cortex-M4 core, 40 MHz maximum operating frequency
- Up to 1 MB flash and 256 KB RAM
- Pin-compatible across EFR32MG families (5V-tolerant pins excluded)
- 12-channel Peripheral Reflex System, low-energy sensor interface, and multi-channel capacitive sense interface
- Autonomous hardware crypto accelerator and true random number generator
- Integrated PA with up to 19 dBm (2.4 GHz) or 20 dBm (Sub-GHz) TX power
- Integrated balun for 2.4 GHz
- Robust peripheral set and up to 65 GPIO

## [CC2652 Platform (TI ZNP)](cc2652-based/index.md)

CC2652/CC1352 radios use the Texas Instruments ZNP stack and are widely supported in both ZHA and Zigbee2MQTT. These models are known for broad device compatibility and a mature firmware ecosystem.

- ZHA radio type: **ZNP**
- Zigbee2MQTT adapter: **zstack**

### CC2652 / CC1352

- 48 MHz ARM Cortex-M4F processor
- 704 KB in-system programmable flash (352 KB on P2)
- 256 KB ROM for protocol and library functions
- 8 KB cache SRAM (or general-purpose RAM)
- 144 KB ultra-low leakage SRAM (80 KB on P2)
- Output power up to +20 dBm
- Z-Stack firmware supports 50 direct children, 100 normal routes, and 200 source routes

## Supported in ZHA and Zigbee2MQTT

Both CC2652 and EFR32 platforms are supported by Home Assistant's ZHA integration and Zigbee2MQTT. The main difference is the adapter selection in each platform's configuration. Setup steps and TCP/USB connection paths are the same across both families.

## Radio Migration Guides

- ZHA migration: <a href="https://www.home-assistant.io/integrations/zha/#migrating-to-a-new-zigbee-adapter-inside-zha" target="_blank" rel="noopener">Home Assistant ZHA migration guide</a>
- Zigbee2MQTT migration: <a href="https://www.zigbee2mqtt.io/guide/faq/#how-do-i-migrate-from-one-adapter-to-another" target="_blank" rel="noopener">Zigbee2MQTT adapter migration FAQ</a>

## Choose Your Path

- [CC2652-Based Coordinators](cc2652-based/index.md)
- [EFR32-Based Coordinators](efr32-based/index.md)
- [Coordinator Firmware Updates](firmware-updates.md)
