# Tube USB CC2652P2 USB Coordinator

This device functions just as any other USB "Stick" with HA/Z2M. You plug it into your device running HA or z2m, and locate the serial port ceated, typically you will want to use the serial/by-id device so it stays consistent an example would be:

```
/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0
```

HA should autodetect the serial port and show it as an option when setting up ZHA.

For z2m you need to device the port in Z2M's configuration.yaml file.