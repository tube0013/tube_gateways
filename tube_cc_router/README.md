# Tube's Router

Device should go into pairing mode as soon as it is powered up for the first time.

To factory reset, open case (it's a friction fit) and a single press of the BSL button will reset the device.

FW Updates require the use of a serial to usb converter.
hold the BSL button when powering the device, keep it held for ~10 seconds to get the device into bootloader mode. Release the button and then use the Use the cc2538-bsl programmer available here: https://github.com/JelmerT/cc2538-bsl to update the FW. if it stalls or fails just repeat.

Devices shipped in 2021 are flashed with Firmware from the Z-Stack Router FW Repository: https://github.com/Koenkk/Z-Stack-firmware/tree/master/router/Z-Stack_3.x.0/bin  specfically the CC1352P2_CC2652P_launchpad_router_* FW.

In 2022 I have made some tweaks to the FW and it can be found here: https://github.com/tube0013/tube_gateways/tree/main/tube_cc_router/firmware

Changes include a tubeszb model id, upping TZ power to 9db and enabling an always on LED to better show power state. I will doucment the changes to the default z-stack-fw in the near future.

