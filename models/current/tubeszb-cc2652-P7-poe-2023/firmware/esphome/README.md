
# ESP32 Flashing

Firmware is available in this folder.

Recommend the ESPHome Flasher tool:
https://github.com/esphome/esphome-flasher/releases

Windows will require the CH340 Serial driver. A version can be found [downloaded here](https://www.olimex.com/Products/Breadboarding/BB-CH340T/resources/CH341SER.zip)

Partially removed the board from the case to access the microUSB port on the Olimex ESP32-PoE module. Use a USB cable (not power only) to connect the the board to the computer doing the flashing. Reminder do not connect USB and Powered ethernet concurrently.


After the flashing completes the esp32 will automatically reset and boot the new FW while showing the console in the flashing tool window to confirm it was flashed okay.


## ESPHome-flasher 

Fire up the flasher and select the correct port and point it to the downloaded FW bin:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_1.jpg" width="400">


Hit flash, and you should see something like this:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_2.jpg" width="400">


after about a minute or so:

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esphome_flasher_3.jpg" width="400">