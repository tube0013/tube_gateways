# Getting Started with Bluetooth Proxies

This guide will walk you through setting up your new TubeZB Bluetooth Proxy.

## What is a Bluetooth Proxy?

A Bluetooth Proxy extends the range of Bluetooth reception for your Home Assistant instance. If you have Bluetooth devices (like temperature sensors, smart locks, etc.) that are too far away from your main Home Assistant machine to connect reliably, you can place a proxy closer to them. The proxy will listen for Bluetooth signals and relay them back to Home Assistant over your network (WiFi or Ethernet).

## Physical Setup

1. Connect the Bluetooth Proxy to your local network using an ethernet cable (recommended for best reliability).

2. Power on the device using a 5V USB-C power supply.

## Home Assistant Setup

Tube's Bluetooth Proxies run ESPHome. When you connect it to your network, Home Assistant should automatically discover it.

1. Ensure your Bluetooth Proxy is powered on and connected to the same network as your Home Assistant instance.

2. A notification should appear in **Settings > Devices & Services** for a new ESPHome device.

3. Click **Configure** and then **Submit** to add the proxy to your system.

That's it! The proxy will now automatically start listening for Bluetooth devices and forwarding the data. You don't need to do anything else. You can confirm it's working by seeing new Bluetooth devices appear in Home Assistant that were previously out of range.