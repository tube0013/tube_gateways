# Specific Configuration for the Tube EFR32 Gateways
Because the EFR32 gateways uses some firrmware settings different than the bellows defaults it is recommended set them in the configuration.yaml so bellows will utilize them.


## For 2022 EFR32 Pro V2 Coordinators:
**Add these lines to your confiuration.yaml file**

```
zha:
  custom_quirks_path: zha_custom_quirks  # Optional Customs Quirk Path
  zigpy_config:
    ota:                                 # Optional OTA device firmware settings
      otau_directory: /config/zigpy_ota
      ikea_provider: true
      ledvance_provider: true
    source_routing: true
    handle_unknown_devices: true
    ezsp_config:
      CONFIG_APS_UNICAST_MESSAGE_COUNT: 30
      CONFIG_TX_POWER_MODE: 3
      CONFIG_MAX_END_DEVICE_CHILDREN: 32
      CONFIG_BROADCAST_TABLE_SIZE: 60
      CONFIG_SOURCE_ROUTE_TABLE_SIZE: 200
      CONFIG_ROUTE_TABLE_SIZE: 32
      CONFIG_ADDRESS_TABLE_SIZE: 32
      CONFIG_PACKET_BUFFER_COUNT: 255
      CONFIG_BINDING_TABLE_SIZE: 32
      CONFIG_NEIGHBOR_TABLE_SIZE: 16
      CONFIG_MTORR_FLOW_CONTROL: 1
      CONFIG_MAX_HOPS: 5
```


