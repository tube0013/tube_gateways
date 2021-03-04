# Specific Configuration for the Tube EFR32 Pro Gateway
Because the Pro gateway uses some higher firmware settings it is recommended set them in the configuration.yaml so bellows will utilize them:

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