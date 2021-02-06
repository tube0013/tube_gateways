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

    **For CC2652p based gateways select ZNP**
    **For EFR32 based gateways select EZSP**

    For the Specifying the Port Specific Settings: Enter socket://ip_or_localdns_name:6638

    **CC2652p Based example:**

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/cc2652_connection.png" width="300">

    **EFR32 Based example:**

    <img src="https://github.com/tube0013/tube_gateways/raw/main/images/efr32_connection.png" width="300">
   