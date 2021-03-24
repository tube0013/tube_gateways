# esphome configs

This folder contains the yaml configurations and required additional includes to build the esphome serial seriver used on the gateways.

By default the firmware uses DHCP. if you need a static IP it will need to be modified and reflashed.

## Get esphome up and running

Option one use the esphome add-on with a supervised HomeAssistant install:
https://esphome.io/guides/getting_started_hassio.html

Option two standalone esphome instance (baremetal or docker):
https://esphome.io/guides/getting_started_command_line.html


Download the .yaml and .h and .cpp files to your esphome folder.

## To add a static IP:

**Warning: An Error in the ip configuration could cause the gw to not connect and require a flash with an Serial to USB converter**

Edit the yaml for your corresponding gateway.

in the Ethernet section add the IP section following it:

```
esphome:
  name: tube_zb_gw_cc2652p2
  platform: ESP32
  board: esp-wrover-kit

  includes:
    - stream_server.h
    - stream_server.cpp

ethernet:
  type: LAN8720
  mdc_pin: GPIO23
  mdio_pin: GPIO18
  clk_mode: GPIO0_IN
  phy_addr: 1
  power_pin: GPIO16

  # Optional manual IP
  manual_ip:
    static_ip: 10.0.0.42
    gateway: 10.0.0.1
    subnet: 255.255.255.0
```

Save the yaml

In the web interface select the 3 dots to bring up the options for the device and select compile. when complete it will have a link to download the .bin file.

 <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome2.png" width="200">


Save the bin file and use the gateway's web interface to upload and reflash the gateway.

 <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_ota.png" width="300">