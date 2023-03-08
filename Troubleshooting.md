# Troubleshooting

## Zigbee2MQTT startup - Error: SRSP - SYS - ping after 6000ms

If you see this message in your z2m Logs with a network connected coordiator: 
```
Error: Failed to connect to the adapter (Error: SRSP - SYS - ping after 6000ms)
```

Please reflash the esphome firmware to the esp32 via serial. For current devices, see the Devices page in the repo, for the original rectangular coordinator see below.

Unfortunately I do not know the casue for this error. It occurs on a small number of devices, and sometimes after doing an OTA ESP32 FW update. It seems specifict to Zigbee2mqtt as the zigpy based tools continue to work fine with the devices. The most reliable fix has been a full serial flash of esphome which does a full esp32 erase before writing the firmware.



## What you need:

For the original rectangular cc2652 coordinator you will need an Serial to USB TTL adaptor - I use one similar to this one and it works well: https://www.amazon.com/HiLetgo-FT232RL-Converter-Adapter-Breakout/dp/B00IJXZQ7C


Grab the current esp fw bin file from your device's firmware/esphome folder on this repo either under models/current or retired. The readme on the devices folder will also have serial flashing instructions.

I use the esphome flasher tool which works well for me:
https://github.com/esphome/esphome-flasher/releases

you’ll need 3 jumper wires, the board has pins, so will need females on that end and female/male on the other depending on your Serial TTL adaptor board.

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esp_flash_wires.jpg" width="400">


TX on the Serial TTL adaptor goes to the eRX pin on the board (red wire in pic)

RX on the Serial TTL adaptor goes to the eTX pin on the board (orange wire in pic)

Ground from the Serial TTL adaptor goes to the Ground pin on the board (closest to 3.3v) (brown wire in pic)

Use the jumper from the 3.3v_Bridge on the board (or another female to female jumper wire) to bridge the ground and IO0 pins (the spacing is tight I found tweezer so pinch nosed pliers best for adding the jumper)

Once all that is connected up, power on by plugging in the micro usb or by using a 4th jumper wire to connect the 3.3 volts on the Serial TTL adaptor to the 3.3v pin on the board.

## Flashing

Fire up the flasher and select the correct port and point it to the downloaded FW bin:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_1.jpg" width="400">


Hit flash, and you should see something like this:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_2.jpg" width="400">


after about a minute or so:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_3.jpg" width="400">

pull the power, and move the jumper back to the 3.3v_Bridge. you can leave the cables connected to do a test boot with serial logging if you want. Just plug it back in, and hit the show logs button in the flasher:

you should see something like this if not connected to ethernet, or maybe on it’s first try of connecting:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_4.jpg" width="400">


if connected to network, should see something like this:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_5.jpg" width="400">

