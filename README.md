# TubesZB Coordinators and Routers

⚠️ **Site Re-Organization in progress** ⚠️

Information and documentation on TubeZB coordinators and routers. Pre-assembed hardware devices can be purchased from https://www.tubeszb.com

TubeZB Coordinators work via serial over Ethernet for use with any zigbee controller project that can access and interface with a remote Serial to IP bridge/proxy server device. 

This can today be used by home automation applications such as example; [Home Assistant (ZHA integration)](https://www.home-assistant.io/integrations/zha/) and [Zigbee2MQTT](https://www.zigbee2mqtt.io/).




## Current Products 
**Find latest Firmware and Source files**

| CC2652 Products | | |
| ----- | ------------ | ----------------- | 
|  <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp" width="100"> | [tubeszb-cc2652-poe-2022](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-cc2652-poe-2022) | CC2652P2 Radio Module + Olimex ESP32-PoE Module |
|  <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-eth_usb/images/tubeszb-cc2652-eth_usb_closed.jpg" width="100"> | [tubeszb-cc2652-eth_usb](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-cc2652-eth_usb) | CC2652P2 Radio Module + WirelessTag WT32-ETH01 ESP32 Module |
| pic | [tubeszb-router](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-router) | CC2652P2 Based Zigbee Router |

| EFR32 Products | | |
| -------------- | - | - |
| <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/current/tubeszb-efr32-MGM12-eth_usb/images/tubeszb-efr32-MGM12P-eth_usb.webp" width="100"> | [tubeszb-efr32-MGM12-eth_usb](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-efr32-MGM12-eth_usb) | MGM12P Radio Module + WirelessTag WT32-ETH01 ESP32 Module |



## Retired Products - Previous hardware versions 
**Find the latest Firmware and Source files**

| CC2652 Products | | |
| ----- | ------------ | ----------------- | 
| <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/retired/tubeszb-cc2652-eth/images/cc2652_eth.webp" width="100"> | [tubeszb-cc2652-eth](https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-cc2652-eth) | CC2652P2 Radio Module + WirelessTag WT32-ETH01 ESP32 Module |
|  <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/retired/tubeszb-cc2652-poe/images/tubeszb-cc2652-poe.webp" width="100"> | [tubeszb-cc2652-poe](https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-cc2652-poe) | CC2652P2 Radio Module + Olimex ESP32-PoE Module |

| EFR32 Products | | |
| -------------- | - | - |
| pic | [tubeszb-efr32-MGM112-pro1](https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-efr32-MGM112-pro1) | MGM12P Radio Module + WirelessTag WT32-ETH01 ESP32 Module |
| <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/retired/tubeszb-efr32-MGM210_Series_2/images/tubeszb-efr32-MGM210_Series_2.jpeg" width="100"> | [tubeszb-efr32-MGM210_Series_2](https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-efr32-MGM210_Series_2) | MGM210 Radio Module + WirelessTag WT32-ETH01 ESP32 Module |



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
The docker containers for Zigbee2MQTT do not seem to work well with mdns, so for coordinators WITH Ethernet use the ip address of the coordinator here.

in the Zigbee2MQTT `configuration.yaml`:

    ```
    serial:
      port: 'tcp://IPADDRESS:6638'

    ```
For coordinators WITHOUT Ethernet you need to specify the device port. Go to the HA command line (for exmaple using this https://community.home-assistant.io/t/home-assistant-community-add-on-ssh-web-terminal/33820) and type `ha hardware info` and find the adapter and look for the line `by_id`and enter that value in the Zigbee2MQTT `configuration.yaml`:

    ```
    serial:
      port: '/dev/serial/by-id/usb-1a86_TubesZB_971207DO-if00-port0'

    ```
## ESPHome

The ESP32 in the gateway runs ESPHome. Configured in ESPHome are switches in order to prep the zigbee modules for firmware updates if needed. **It is Highly Advised to Ignore these entities in HomeAssistant as accidential toggling could reset the zigbee modules.**

To access the ESPHome Web Interface on the gateway connect to it in your Browser via it's IP address or via these URLs:

CC2652p based gateways: `http://tube_zb_gw_cc2652p2.local`
EFR32 based gateways: `http://tube_zb_gw_efr32.local`


## Zigbee Module Firmware Updates:
This section relates to updating the firmware of the zigbee module. If you have an adapter WITH Ethernet and want to update the firmware of the ESP32 Ethernet module then go back to the top of this page and select the links to the firmware for the product you have. These links also have further information for how to flash the zigbee module and should be read in conjunction with the below https://github.com/tube0013/tube_gateways#current-products

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
