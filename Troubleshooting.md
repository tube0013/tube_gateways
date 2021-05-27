**Troubleshooting and best practices guides**

Instructions of reflashing the ESP32 when it is not connecting to ethernet and the leds on the esp32 ethernet jack will be solid green and not blinking:

You will need an Serial to USB TTL adaptor - I use one similar to this one and it works well: https://www.amazon.com/HiLetgo-FT232RL-Converter-Adapter-Breakout/dp/B00IJXZQ7C

Grab the current esp fw bin file: 

CC2652P2 based Coordinator:
https://github.com/tube0013/tube_gateways/raw/main/tube_zb_gw_cc2652p2/tube_zb_gw_cc2652p2_(2021_04_08).bin

EFR32 based Coordinator:
https://github.com/tube0013/tube_gateways/tree/main/tube_zb_gw_efr32/Firmware/ESP32

I use the esphome flasher tool which works well for me:
https://github.com/esphome/esphome-flasher/releases

you’ll need 3 jumper wires, the board has pins, so will need females on that end and female/male on the other depending on your Serial TTL adaptor board.

  <img src="https://github.com/tube0013/tube_gateways/raw/main/images/esp_flash_wires.jpg" width="400">


TX on the Serial TTL adaptor goes to the eRX pin on the board (red wire in pic)

RX on the Serial TTL adaptor goes to the eTX pin on the board (orange wire in pic)

Ground from the Serial TTL adaptor goes to the Ground pin on the board (closest to 3.3v) (brown wire in pic)

Use the jumper from the 3.3v_Bridge on the board (or another female to female jumper wire) to bridge the ground and IO0 pins (the spacing is tight I found tweezer so pinch nosed pliers best for adding the jumper)

Once all that is connected up, power on by plugging in the micro usb or by using a 4th jumper wire to connect the 3.3 volts on the Serial TTL adaptor to the 3.3v pin on the board.

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

### Knowing which devices are supported

Due to how Zigbee implementation works there should not really be any need of compatibility lists of supported devices for the simple reason that practically all devices Zigbee Home Automation that are fully compliant with the standards and specifications as set by the [Zigbee Alliance](https://zigbeealliance.org) should technically be compatible with with each Zigbee network implementations/application that already supports that other devices of the same type that uses the same features and functions. 

The fact remains, however, that some hardware manufacturers do not always fully comply with each specification set by the Zigbee Alliance], which can cause a few devices to only partially work or not work at all with some Zigbee network implementations/application, but the developers of those implementations can code and add exception workarounds for such deviation issues via specific device handling. As such you usually assume that almost all standard Zigbee devices should work and if they do not they you will normally need to submit a feature request to the home automation implementations/application that you use for its developers to add a device handler for any device that you find not fully working.

Tip to new users is that, while there is no official list of supported devices, some users take comfort that blakadder maintains an unofficial Zigbee Device Compatibility Repository which anyone can submit compatibility reports to, it can be found at [zigbee.blakadder.com](https://zigbee.blakadder.com) and currently contains independent compatibility lists and device pairing tips for several home automation gateway/bridge/hub softwares, including but not limited to open source Zigbee implementations such as; Home Assistant ZHA, Tasmota, Zigbee2MQTT, and ZiGate.

#### Best practices for avoiding pairing difficulties

-	If possible try to pair your Zigbee devices in their intended final location, (and not pair it next to the Zigbee coordinator and then need to move it after). 
    -	Pairing a Zigbee device next to the Zigbee coordinator and then moving it later can result in a dropped/lost connections or other issues.
-	Zigbee devices that have in the past been connected used to a other Zigbee coordinator (hub/bridge/gateway/controller) can usually only be added/paired in the Zigbee network implementations/application that you use after they have been restored to their factory reset settings. 
    -	If the device you want to add is not brand new and as such never paired before then you always have to make sure to first manually reset the device to its factory default settings before you will be able add/pair it.
-	Some battery-operated Zigbee devices are known to have problems with pairing if they have Low battery voltage. 
    -	Some people have reported replacing the battery on their newly received Xiaomi/Aqara devices solved pairing issues.
-	Check that you have enough Zigbee router devices (also known as Zigbee signal repeaters or range extenders) and if you do not have any, invest and add some mains-powered devices that will work as Zigbee routers. 
    -	Aim to start out with mains-powered devices before adding battery-operated devices as a "weak" Zigbee network mesh (e.g., the device is too far from the Zigbee coordinator or a Zigbee router) may prevent some devices from being paired. Zigbee router devices are also needed to increase the maximum of devices that can be connected to your Zigbee mesh network. 
    -	Note that some Zigbee devices are not fully compatible with all brands of Zigbee router devices. Xiaomi/Aqara devices are for example known not to work with Zigbee router devices from Centralite, General Electrics, Iris, Ledvance/OSRAM/ LIGHTIFY/Sylvania, Orvibo, PEQ, Securifi, and SmartThings/Samsung. Better results can usually be achieved by using mains-powered devices IKEA and Nue/3A Home or dedicated DIY routing devices based on Texas Instruments CC253x/CC26x2 and XBee Series 2/3 Zigbee radios.
-	Be patient as the pairing of some Zigbee devices may require multiple attempts and you may sometimes need to try again and again.
    -	 Some devices, like example those from Xiaomi/Aqara, are known to not be 100% compliant with the standard Zigbee specifications and may therefor require many paring attempts over 10-20 minutes or longer.

### Improving Zigbee network range and signal reception

Low signal quality and enviroment noise can lead to transmission errors or other related issues. This section has a list of fundamental tips on how to improve signal quality. Improving signal quality also maximizes range and resolves most problems related to transmission errors. Please try to follow at least some of these recommendations before posting on the community forums or reporting issues to developers and submitting debug logs.

1. Add more Zigbee routers between devices far away and the next closest router. Distribute more Zigbee routers in areas with poor reception. Zigbee network topology uses a "mesh network" design which means that each device that acts as a Zigbee router will extend the range of your Zigbee network as a whole. While there are exceptions, almost all permanently powered devices serve as a Zigbee router. Adding more permanently powered Zigbee devices allows getting better coverage. There are also dedicated Zigbee routers which you can [find by doing a community search for "Zigbee signal repeater" or "Zigbee range extender"](https://community.home-assistant.io/t/advice-on-zigbee-range-extending/175882/)). Devices that can not act as routers are typically battery-operated and known as "end devices". Some end devices have issues connecting through routers (e.g. Xiaomi/Aqara devices).
2. Locate and position the Zigbee coordinator away from Wi-Fi access-points/routers or other sources of 2.4GHz signals and electrictronic fields to avoid signal interference, as well as moving you Zigbee coordinator away from any other devices/appliances that might not have proper electrictronic shielding (that included the computer appliance for your home automation and any harddrives as they are especially know for emitting interfering electronic interference or radio frequency interference, also known as EMI and RFI). The best location depends on your building's floorplan. Ideally, you want to place the Zigbee coordinator somewhere in the middle. Building materials do influence signal quality too, for example, dense/thick concrete, bricks, masonry, etc. dampen all wireless signals. Place the Zigbee coordinator with some distance from walls, ceilings and floors. Also, try different orientations of your Zigbee antenna (or your whole Zigbee coordinator adapter if it has an internal antenna). Some Antennas have a stronger signal in a certain direction. Simply changing orientation can improve signal quality already. 
3. Use a long USB extension cable if you have a Zigbee coordinator USB stick/dongle . This allows positioning the Zigbee coordinator adapter for better signal quality. Please see tips about location and positioning in point #2 above. Note: A bad USB extension cable may lead to connection issues between the system and the Zigbee coordinator adapter, symptoms of this are disconnection messages.
4. Zigbee and Wi-Fi can operate on various overlapping channels in the 2.4GHz spectrum. A busy Wi-Fi access-points/routers that are operating in the same frequency range (overlapping channels) as your Zigbee coordinator will drown out the Zigbee traffic, especially if they are located close to each other. To avoid interference between Zigbee and Wi-Fi try to choose channels without overlap. Check the channel your Wi-Fi access-points/routers are using (either by checking on the router's web interface or using a Wi-Fi analyzer app). The Zigbee channel is currently not shown in the Home Assistant front-end but you can find the channel in the logs (watch out for Network parameters log entry with the channel number, e.g., `radioChannel=15`). Changing the channel of the Zigbee network needs recreating it and re-join/re-pair all of your Zigbee devices. Typically it's a lot easier to change the channel used by your Wi-Fi. See [this article for Wi-Fi and Zigbee channels coexistance](https://www.metageek.com/training/resources/zigbee-wifi-coexistence.html) to avoid using overlapping frequency ranges.
5. Update the firmware on your Zigbee coordinator adapter and your Zigbee devices. Note that depending on your hardware the latest Zigbee coordinator firmware might not always be the one recommended by the community so it is advised to ask before upgrading.
6. If your Zigbee coordinator adapter has a removable antenna (e.g., with an SMA-connector) then you have the option of using a high-gain antenna. Note that antennas with higher gain have directionality: You might have better reception on the same floor, but reception across floors might suffer. In addition, you also have the option to use an antenna extension-cable if needed (usually using just a USB extension cable for your Zigbee coordinator adapter is the better alternative). This should really only be needed if you are trying to cover a long distance, like to another building or very dense/thick walls, ceilings and floors.
7. If you have not already, buy more powerful Zigbee radio hardware with better radio range, preferably with an external antenna. If you are not only experimenting but want a permanently stable and healthy Zigbee network with potentially many devices then you should consider upgrading to a more powerful Zigbee coordinator USB adapter. Generally, those with an external antenna will have better range, therefore you will also want to avoid buying an internal adapter unless it has an external antenna. Note: Because Zigbee is based on mesh networking technology just buying a  more powerful Zigbee radio hardware adapter does not replace the need to add and use Zigbee routers between devices far away and the next closest router as suggested in point #1 above.

#### Using router devices

Zigbee uses mesh networking technology as standard by design and adding devices capable of acting as Zigbee router (sometimes also known as Zigbee signal repeaters or extenders) is very important because they increasing the total number of Zigbee devices that your Zigbee coordinator can control in its network as well as having an integral role in extending the overall range and coverage of your Zigbee network mesh. Fact is that without haveing at least a couple good Zigbee router devices available you will normally not have a stable Zigbee network.

The total number of Zigbee devices that you have on a Zigbee network depends on a few things, but you should know that Zigbee coordinator hardware and firmware usually only start to play a larger role in a once you have around 40 devices or more in your Zigbee mesh network. More important is how many directly connected devices ("direct children") versus how many routers are and can be connected to your Zigbee coordinator. Each type and model of Zigbee coordinator also gave a different limit for how many child devices that can connect directly to it. Even if that limit is low on your Zigbee coordinator, if your Zigbee coordinator hardware is powerful and its firmware capable of it then you can still have a total of hundreds or even thousands of Zigbee devices as long as they are indirecly connected through a mesh network with Zigbee router devives instead.

The least powerful Zigbee coordinator hardware supported by Zigpy is CC2530/2531 and its default firmware, only supports 15 devices connected directly to the coordinator. However, by having a backbone of good always-on Zigbee routers in your Zigbee network, the mesh network size can be extended exponentionally. You can assume that most, if not all mains-powered/AC-powered devices, e.g., wall-plugs and always powered-on lightbulbs in your Zigbee network can serve as a Zigbee router and can typically each act as a router for around 5 additional end devices, while some dedicated Zigbee router devices can each act as a router for as many as 50 devices. You can for example use a DIY CC2530/CC2531 with router firmware which have a limit of 21 devices, while a DIY CC2652 (CC2652P/CC2652R) with router firmware which have a limit of 50 devices, or the IKEA TRÅDFRI Signal Repeater which can route about 10-20 devices.
