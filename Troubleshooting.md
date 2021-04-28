for the FW grab the esp fw bin file here: https://github.com/tube0013/tube_gateways/raw/main/tube_zb_gw_cc2652p2/tube_zb_gw_cc2652p2_(2021_04_08).bin

I use the esphome flasher tool which works well for me:
https://github.com/esphome/esphome-flasher/releases

you’ll need 3 jumper wires, the board has pins, so will need females on that end and female/male on the other depending on your Serial TTL adaptor board.

TX on the Serial TTL adaptor goes to the eRX pin on the board (red wire in pic)
RX on the Serial TTL adaptor goes to the eTX pin on the board (orange wire in pic)
Ground from the Serial TTL adaptor goes to the Ground pin on the board (closest to 3.3v) (brown wire in pic)
Use the jumper from the 3.3v_Bridge on the board to bridge the ground and IO0 pins (the spacing is tight I found tweezer so pinch nosed pliers best for adding the jumper)
once all that is connected up, power on by plugging in the micro usb or by using a 4th jumper wire to connect the 3.3 volts on the Serial TTL adaptor to the 3.3v pin on the board.

IMG_5795
IMG_5795
3024×4032 2.36 MB
Fire up the flasher and select the correct port and point it to the downloaded FW bin:

image
image
1458×388 54.9 KB
HIt flash, and you should see something like this:

image
image
1406×934 90.2 KB
after about a minute or so:

image
image
1270×336 35.5 KB
pull the power, and move the jumper back to the 3.3v_Bridge. you can leave the cables connected to do a test boot with serial logging if you want. Just plug it back in, and hit the show logs button in the flasher:

you should see something like this if not connected to ethernet, or maybe on it’s first try of connecting:

image
image
1384×968 240 KB
if connected to network, should see something like this:

image
image
1384×922 270 KB
