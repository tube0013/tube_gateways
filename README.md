# Tube's Zigbee Gateways

Information and documentation on Tube's Zigbee Gateways. Pre-assembed hardware devices can be purchased from https://www.tubeszb.com

The gateway hardware itself is made up of a WT32-ETH01 or Olimex ESP32-POE-ISO (which are ESP32 based boards with Ethernet) in combination with either a Texas Instruments CC2652P or a Silicon Labs EFR32 based Zigbee serial module.

Tube's Zigbee Gateways are primarly design to work as Zigbee serial module to Ethernet server as that make them compatible any application/project that can access and interface with a remote Serial to IP bridge/proxy server device as long as they support the Zigbee stack flashed on the Zigbee serial module firmware.

These Zigbee gateways/coordinators can today be used by home automation applications such as example; [Home Assistant (ZHA integration)](https://www.home-assistant.io/integrations/zha/), [Jeedom (Zigbee Plugin)](https://doc.jeedom.com/en_US/plugins/automation%20protocol/zigbee/), [openHAB (Zigbee Binding)](https://www.openhab.org/addons/bindings/zigbee/), and [Zigbee2MQTT](https://www.zigbee2mqtt.io/). 

Note! The [openHAB Zigbee Binding](https://www.openhab.org/addons/bindings/zigbee/) does not yet have suppprt for by the Z-Stack 3 Zigbee stack firmware used on the Texas Instruments CC2652 based gateways/coordinators, (more details on ).

## Getting up and Running

## ZHA
*For EFR32 Gateways see specific insturctions for config file* https://github.com/tube0013/tube_gateways/tree/main/tube_zb_gw_efr32

*Auto Discovery for EFR32 Gatways is currently broken in HA, Please ignore the discovered device and set up manually*

1. Connect the gateway to a ethernet cable which has access you your local network.
2. Power on the gateway with a micro usb cable and power supply. The link lights on the ethernet port will start blinking as it tries to negotiate a connection with your home network router.
3. Determine the device's ip address
    If your local network supports .local mdns addresses, the devices can be reached that way: 

    -for CC2652p based microUSB powered coordinators: tube_zb_gw_cc2652p2.local 

    -for CC2652p based PoE coordinators: tube_zb_gw_cc2652p2_poe.local

    -for EFR32 based coordinators: tube_zb_gw_efr32.local

    **Using a Reserved or static IP Address is strongly advised. Reserve the address in the router or use a static [ESPHome](https://github.com/tube0013/tube_gateways/tree/main/esphome#to-add-a-static-ip) build with static ip**

4. Configure your software to access the device.

    **For HomeAssistant's Built in ZHA implementation:**

    Add the ZHA Integration via the Add Integrations option:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/add_integration.png" width="300">

    In the next window use the dropdown to select Manual:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/manual.png" width="350">

    Select the Radio type:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/radio_type.png" width="400">

    *For CC2652p based gateways select ZNP*  
    *For EFR32 based gateways select EZSP*

    For the Specifying the Port Specific Settings: Enter socket://ip_or_localdns_name:6638 and Port Speed of 115200 and Software Flow Control.

    CC2652p Based example:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_connection.png" width="300">

    EFR32 Based example:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/efr32_connection.png" width="300">


## Zigbee2MQTT
*For Zigbee2mqtt - Only the CC2652p based gateway is supported at this time:*

No need to pass any devices through to Zigbee2MQTT docker container setups.
The docker containers for Zigbee2MQTT do not seem to work well with mdns, so use the ip address of the coordinator here.

in the Zigbee2MQTT `configuration.yaml`:

    ```
    serial:
      port: 'tcp://IPADDRESS:6638'

    ```

## ESPHome

The ESP32 in the gateway runs ESPHome. Configured in ESPHome are switches in order to prep the zigbee modules for firmware updates if needed. **It is Highly Advised to Ignore these entities in HomeAssistant as accidential toggling could rest the zigbee modules.**

To access the ESPHome Web Interface on the gateway connect to it in your Browser:

CC2652p based gateways: `http://tube_zb_gw_cc2652p2.local`
EFR32 based gateways: `http://tube_zb_gw_efr32.local`

## Tasmota

As an alternative to the default ESPHome firmware, Tube's Zigbee Gateways featuring ESP32 and running compatible Zigbee Coordinator firmware also support Zigbee2Tasmota (Z2T) version of Tasmota32 (Tasmota for ESP32). Zigbee2Tasmota (Z2T) can either be used as a simple serial-to-IP server the same way as ESPHome firmware or you can use its own native Zigbee implementation as a stand-alone Zigbee to MQTT bridge/gateway/hub. 

While not as user-friendly as ESPHome firmware used together with external implementations like Home Assistant's ZHA or Zigbee2MQTT, the real benifit with Zigbee2Tasmota (Z2T) is can be used as a stand-alone Zigbee to MQTT bridge/gateway/hub which is not dependent on any other Zigbee implementations.

To use this you flash the ESP32 chip with "tasmota32-zbbridge" firmware from the Tasmota project, which is ESP32 firmware variant of "tasmota-zbbridge" (that was initially designed to run ITead Sonoff ZBBridge hardware based on the older ESP8266/ESP8285 chips).

Note! Zigbee2Tasmota (Z2T own native Zigbee gateway implementation does not yet have support for  Z-Stack 3 Zigbee stack firmware used on the Texas Instruments CC2652 based gateways, as such Zigbee2Tasmota (Z2T) currenly only support Tube's Zigbee Gateways with Silicon Labs EFR32 via the EZSP v8 API/CLI and they are only tested with EmberZNet 6.7.9 firmware, however while not tested, the Texas Instruments based variants with Z-Stck 3 should in theory still work if you will only be using your Tube's Zigbee Gateway with the serial-to-IP functionaliy with external implementations that supports Z-Stack 3, like example Home Assistant ZHA, Jeedom Zigbee Plugin, and Zigbee2MQTT.

- https://tasmota.github.io/docs/Zigbee/
- https://github.com/arendst/Tasmota

## Zigbee Module Firmware Updates:

**CC2652p based Gateways:**  
Firmware - use the **CC1352P2_CC2652P_launchpad_*.zip** based firmware available here:  
https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator/Z-Stack_3.x.0/bin

**Be Sure to backup your device before updgrading as the update will erase the zigbee module completely** https://github.com/zigpy/zigpy-znp/blob/dev/TOOLS.md#backup-and-restore

Use the cc2538-bsl programmer available here: https://github.com/JelmerT/cc2538-bsl

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
**USB Version**
1. Connect the module while pushing the BSL button
2. Run the cc2538-bsl programmer:
```
 python3 cc2538-bsl.py -evw -p /dev/ttyUSB0 ./CC1352P2_CC2652P_launchpad_coordinator_20220219.hex
Opening port /dev/ttyUSB0, baud 500000
Reading data from ./CC1352P2_CC2652P_launchpad_coordinator_20220219.hex
Your firmware looks like an Intel Hex file
Connecting to target...
CC1350 PG2.0 (7x7mm): 352KB Flash, 20KB SRAM, CCFG.BL_CONFIG at 0x00057FD8
Primary IEEE Address: 00:12:4B:00:22:98:3A:E0
    Performing mass erase
Erasing all main bank flash sectors
    Erase done
Writing 360448 bytes starting at address 0x00000000
Write 104 bytes at 0x00057F988
    Write done
Verifying by comparing CRC32 calculations.
    Verified (match: 0xddfc152d)
```
**EFR32 based Gateways**

https://www.youtube.com/watch?v=zKrISuWEzL4tube-
