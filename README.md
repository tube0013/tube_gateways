# Tube's Zigbee Gateways
Information and Documentation on Tube's Zigbee Gateways

Tube's Zigbee Gateways are serial over ethernet zigbee gateways for use with any project that can access a remote serial device. The gateway is made up of a WT32-ETH01 module which is an ESP32 with ethernet and either a CC2652p Zigbee Module or an EFR32 based Zigbee module.

## Getting up and Running
1. Connect the gateway to a ethernet cable which has access you your local network.
2. Power on the gateway with a micro usb cable and power supply.
3. Determine the device's ip address
    If your local network supports .local mdns addresses, the devices can be reached that way:
    -for CC2652p based gatways: tube_zb_gw_cc2652p2.local
    -for EFR32 based gateways: tube_zb_gw_efr32.local
   
    **If using an IP Address besure it is reserved in your router so it does not change**
    
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

    For the Specifying the Port Specific Settings: Enter socket://ip_or_localdns_name:6638

    CC2652p Based example:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_connection.png" width="300">

    EFR32 Based example:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/efr32_connection.png" width="300">
   

    **For Zigbee2mqtt - Only the CC2652p based gateway is supported at this time:**

    in the Zigbee2MQTT `configuration.yaml` 

    ```
    serial:
      port: 'tcp://tube_zb_gw_cc2652p2.local:6638'

    ```

## ESPHome

The ESP32 in the gateway runs ESPHome. Configured in ESPHome are switches in order to prep the zigbee modules for firmware updates if needed. **It is Highly Advised to Ignore these entities in HomeAssistant.

To access the ESPHome Web Interface on the gateway connect to it in your Browser:

CC2652p based gateways: `http://tube_zb_gw_cc2652p2.local`
EFR32 based gateways: `http://tube_zb_gw_efr32.local`


## Zigbee Module Firmware Updates:

**CC2652p based Gateways:**
Firmware - use the **CC1352P2_CC2652P_launchpad_*.zip** based firmware available here: 
https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator/Z-Stack_3.x.0/bin

Use the cc2538-bsl programmer available here: https://github.com/JelmerT/cc2538-bsl

    1. Prep the Module for firmware update:

    Click the button to intiate the bootloader mode for the module:

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_web1.png" width="300">
    
    Watch the Debug output and when pompted go to step 2.

     <img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_fw_debuglog.png" width="300">


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






