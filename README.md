# TubesZB Coordinators and Routers

⚠️ **Site Re-Organization in progress** ⚠️

Information and documentation on TubeZB coordinators and routers. Pre-assembed hardware devices can be purchased from https://www.tubeszb.com

TubeZB Coordinators work via serial over Ethernet for use with any zigbee controller project that can access and interface with a remote Serial to IP bridge/proxy server device. 

This can today be used by home automation applications such as example; [Home Assistant (ZHA integration)](https://www.home-assistant.io/integrations/zha/) and [Zigbee2MQTT](https://www.zigbee2mqtt.io/).




## Current Products 
**Find latest Firmware and Source files**

| **CC2652 Products** | | |
| ----- | ------------ | ----------------- | 
|  <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/current/tubeszb-cc2652-poe-2022/images/tubeszb-cc2652-poe-2022.webp" width="100"> | [tubeszb-cc2652-poe-2022](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-cc2652-poe-2022) | CC2652P2 Radio Module + Olimex ESP32-PoE Module |
|  <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-cc2652-eth_usb/images/tubeszb-cc2652-eth_usb_closed.jpg" width="100"> | [tubeszb-cc2652-eth_usb](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-cc2652-eth_usb) | CC2652P2 Radio Module + WirelessTag WT32-ETH01 ESP32 Module |
| pic | [tubeszb-router](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-router) | CC2652P2 Based Zigbee Router |
| **EFR32 Products** | | |
| <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/current/tubeszb-efr32-MGM12-eth_usb/images/tubeszb-efr32-MGM12P-eth_usb.webp" width="100"> | [tubeszb-efr32-MGM12-eth_usb](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-efr32-MGM12-eth_usb) | MGM12P Radio Module + WirelessTag WT32-ETH01 ESP32 Module |
| BT Proxy | | |
| <img src="https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-wt32-eth01-bt-kit/images/Subject.png" width="100"> | [tubeszb-wt32-eth01-bt-kit](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-wt32-eth01-bt-kit) | WirelessTag WT32-ETH01 ESP32 Module with USB-C for Power/Flashing |




## Retired Products - Previous hardware versions 
**Find the latest Firmware and Source files**

| **CC2652 Products** | | |
| ----- | ------------ | ----------------- | 
| <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/retired/tubeszb-cc2652-eth/images/cc2652_eth.webp" width="100"> | [tubeszb-cc2652-eth](https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-cc2652-eth) | CC2652P2 Radio Module + WirelessTag WT32-ETH01 ESP32 Module |
|  <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/retired/tubeszb-cc2652-poe/images/tubeszb-cc2652-poe.webp" width="100"> | [tubeszb-cc2652-poe](https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-cc2652-poe) | CC2652P2 Radio Module + Olimex ESP32-PoE Module |
| **EFR32 Products** | | |
| pic | [tubeszb-efr32-MGM112-pro1](https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-efr32-MGM112-pro1) | MGM12P Radio Module + WirelessTag WT32-ETH01 ESP32 Module |
| <img src="https://raw.githubusercontent.com/tube0013/tube_gateways/main/models/retired/tubeszb-efr32-MGM210_Series_2/images/tubeszb-efr32-MGM210_Series_2.jpeg" width="100"> | [tubeszb-efr32-MGM210_Series_2](https://github.com/tube0013/tube_gateways/tree/main/models/retired/tubeszb-efr32-MGM210_Series_2) | MGM210 Radio Module + WirelessTag WT32-ETH01 ESP32 Module |



## Getting up and Running

## ZHA
*For EFR32 Gateways see specific insturctions for config file* visit product page

1. Connect the gateway to a ethernet cable which has access you your local network.
2. Power on the gateway with a micro usb cable and 5v 1.5 - 2 amp power supply. The link lights on the ethernet port will start blinking as it tries to negotiate a connection with your home network router.

If the Device is AutoDiscovered, click through the Config flow to add it to HA. 


 <img src="https://github.com/tube0013/tube_gateways/raw/main/images/discover0.png" width="300">

 <img src="https://github.com/tube0013/tube_gateways/raw/main/images/discover1.png" width="300">

If not move on to the below steps.

3. Determine the device's ip address

    **Using a Reserved or static IP Address is strongly advised. Reserve the address in the router **

4. Configure your software to access the device.

    **For HomeAssistant's Built in ZHA implementation:**

    Add the ZHA Integration via the Add Integrations option:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/manual1.png" width="300">

    In the next dialog select *Set up another instance of Zigbee Home Automation*:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/manual2.png" width="300">

    Select the Radio type:

    *For CC2652p based gateways select ZNP*
    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/radiotypeznp.png" width="300">

    *For EFR32 based gateways select EZSP*
    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/radiotypeezsp.png" width="300">

    For the Specifying the Port Specific Settings: Enter socket://ip_or_localdns_name:6638 and Port Speed of 115200 and Software Flow Control.

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/serialportsettings.png" width="300">



## Zigbee2MQTT
*For Zigbee2mqtt - Only the CC2652p based gateway is supported at this time, EFR32 may work but is not recommended*

### Network Coordinators 
No need to pass any devices through to Zigbee2MQTT docker container setups.
The docker containers for Zigbee2MQTT do not wrk well with mdns, so for coordinators WITH Ethernet use the ip address of the coordinator here.

Following the Zigbee2MQTT docs, you can skip to step 3. 
https://www.zigbee2mqtt.io/advanced/remote-adapter/connect_to_a_remote_adapter.html#_3-configure

in the Zigbee2MQTT `configuration.yaml`:

    ```
    serial:
      port: 'tcp://IPADDRESS:6638'

 
### USB Connected Coordinantors - NO Ethernet 

If not using HAOS be sure to pass the device through to the docker container. Donig that is outside the scope of this documentation.

Find the Devices port:

For using HAOS:
Settings > System > Hardware > 3 Dot menu > All Hardware

OR

Go to the HA command line (for exmaple using this https://community.home-assistant.io/t/home-assistant-community-add-on-ssh-web-terminal/33820) type `ha hardware info` and find the adapter and look for the line `by_id`.

It should look something like 

```
/dev/serial/by-id/usb-1a86_TubesZB_971207DO-if00-port0

```

But may not match exactly depending on the OS/System



Enter that value in the Zigbee2MQTT Addon confi or  `configuration.yaml`:

    ```
    serial:
      port: '/dev/serial/by-id/usb-1a86_TubesZB_971207DO-if00-port0'

    ```

## ESPHome

The ESP32 in the gateway runs ESPHome. Configured in ESPHome are switches in order to prep the zigbee modules for firmware updates if needed. **It is Highly Advised to Ignore these entities in HomeAssistant as accidential toggling could reset the zigbee modules.**

To access the ESPHome Web Interface on the gateway connect to it in your Browser via it's IP address.

Binaries and yaml configs for the devices are under the individual product pages.



## Firmware update instructions are under the individual product pages.

