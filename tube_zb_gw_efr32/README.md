# Specific Configuration for the Tube EFR32 Gateways
Because the EFR32 gateways uses some higher firmware settings it is recommended set them in the configuration.yaml so bellows will utilize them.


Add these lines to your configuration.yaml file:

```
zha:
  zigpy_config:
    source_routing: true
    ezsp_config:
      CONFIG_APS_UNICAST_MESSAGE_COUNT: 30
      CONFIG_MAX_END_DEVICE_CHILDREN: 64
      CONFIG_SOURCE_ROUTE_TABLE_SIZE: 200
      CONFIG_ROUTE_TABLE_SIZE: 16
      CONFIG_ADDRESS_TABLE_SIZE: 32
      CONFIG_PACKET_BUFFER_COUNT: 254
      CONFIG_BINDING_TABLE_SIZE: 32
      CONFIG_NEIGHBOR_TABLE_SIZE: 26
```

**Note if using HA lower than 2021.03.x you will need to use lower values as bellows was not able to use the higher values until the release bundled with 2021.03.**

Use these lines if using HA < 2021.03

```
zha:
  zigpy_config:
    source_routing: true
    ezsp_config:
      CONFIG_APS_UNICAST_MESSAGE_COUNT: 30
      CONFIG_MAX_END_DEVICE_CHILDREN: 32
      CONFIG_SOURCE_ROUTE_TABLE_SIZE: 200
      CONFIG_ROUTE_TABLE_SIZE: 16
      CONFIG_ADDRESS_TABLE_SIZE: 32
      CONFIG_PACKET_BUFFER_COUNT: 254
      CONFIG_BINDING_TABLE_SIZE: 32
      CONFIG_NEIGHBOR_TABLE_SIZE: 16
```




# Using the onboard headers/jumpers to select the serial output

The 2 groups of four headers control the connection of the serial.

  eTX and eRX connect to the esp’s main/flashing serial connection * *see note below*

  sTX and sRX are the TX and RX pins on the built I serial module.

  zTX and zRX are the TX and RX pins on the zigbee modules

  ezTX and ezRX are the secondary uart pins for the esp for use when running the coordinator through Ethernet

Jumpers all the way toward to esp module as pictured the serial runs to the esp for network usage:

 <img src="https://github.com/tube0013/tube_gateways/raw/main/images/efr32_ztoeth.png" width="300">


Move the jumpers to the middle two pins and the zigbee serial goes through the embedded serial converter:

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/efr32_ztos.png" width="300">

*My goal was to have the esp’s main flashing/log console serial connection available by moving it all the way to the other side however I messed up the TX>RX and RX>TX here (and it’s the one place I can’t fix it with firmware) so jumpers are needed to connect the sTX to the eRX in the other row and the sRX to the eTX. Then the esp is available over serial and the log for esphome should show when connected to serial.

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/efr32_etos.png" width="300">

Finaly by connecting ground to IO0, you and powering up the gw, the ESP32 will be in flash mode and flashable over serial if needed.

<img src="https://github.com/tube0013/tube_gateways/raw/main/images/efr32_espflash.png" width="300">
