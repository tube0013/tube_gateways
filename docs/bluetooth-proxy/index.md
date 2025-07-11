# WT32-ETH01 Bluetooth Proxy Kit

<figure markdown>
  ![Bluetooth Proxy Kit](https://github.com/tube0013/tube_gateways/raw/main/models/current/tubeszb-wt32-eth01-bt-kit/images/Subject.png){ width="300" }
</figure>

The TubeZB Bluetooth Proxy Kit is a simple and effective way to extend the Bluetooth coverage of your Home Assistant instance. It uses a wired ethernet connection for maximum reliability.

---

## Getting Started

For initial setup and integration with Home Assistant, please follow the main Bluetooth Proxy getting started guide.

[:octicons-arrow-right-24: View Bluetooth Proxy Getting Started Guide](../getting-started/bluetooth-proxy.md)

---

## How It Works

This kit acts as a remote "ear" for Home Assistant. You can place it anywhere in your home where you have an ethernet connection. It will listen for Bluetooth Low Energy (BLE) advertisements from devices like temperature sensors, smart locks, and more. It then relays these messages back to Home Assistant over your wired network.

This allows you to integrate Bluetooth devices that are far away from your main Home Assistant server.

---

## Firmware

The device comes pre-flashed with a standard ESPHome Bluetooth proxy firmware. If you ever need to re-flash or update the device, you can do so easily.

### Flashing Instructions

1.  Connect the Bluetooth Proxy Kit to your computer using a **USB-C data cable**.
2.  Navigate to the **[TubesZB Web Flasher](https://tube0013.github.io/TubesZB-ESPHome-Builder/)**.
3.  Select "Bluetooth Proxy" from the device dropdown menu.
4.  Follow the on-screen instructions to connect to the device and flash the latest firmware.

### Advanced Users & Source YAML

This kit is based on the official ESPHome Wireless Tag WT32-ETH01 project. Advanced users who wish to compile their own custom firmware can find the base YAML configuration files in the **[ESPHome GitHub repository](https://github.com/esphome/bluetooth-proxies/tree/main/wt32)**.

For more in-depth details on how the proxy functionality works within ESPHome, please refer to the official **[ESPHome Bluetooth Proxy Documentation](https://esphome.io/components/bluetooth_proxy.html)**.