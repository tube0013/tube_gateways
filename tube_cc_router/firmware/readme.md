Changes made from stock Z-Stack FW (https://github.com/Koenkk/Z-Stack-firmware/tree/master/router/Z-Stack_3.x.0):

Model Id and Manufacturer:

Application/zcl_genericapp.c:

Lines 98-100
```
const uint8_t zclGenericApp_ManufacturerName[] = { 7, 'T','u','b','e','s','Z','B' };
const uint8_t zclGenericApp_ModelID[] = { 14, 't','u','b','e','s','z','b','.','r','o','u','t','e','r' };
const uint8_t zclGenericApp_SwBuildID[] = { 8, '2','0','2','2','0','1','1','1' };
```

Always on LED:

/syscfg/ti_drivers_config.c:

Line: 240:

```
    GPIOCC26XX_DIO_06 | GPIO_CFG_OUT_STD | GPIO_CFG_OUT_STR_MED | GPIO_CFG_OUT_HIGH,
```

TX 9 db:

/Stack/Config/f8wrouter.opts:

Added:

```
-DPHY_TX_POWER_FREQ_2_4_G=9

```

