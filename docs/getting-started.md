# Getting Started

This guide will walk you through setting up your new TubeZB Coordinator.

## First Steps: Physical Setup

For **Network (Ethernet) Coordinators**:

1.  Connect the gateway to your local network using an ethernet cable.
2.  Power on the gateway using a 5v 1.5-2A power supply with a micro USB cable. The ethernet port's link lights will begin to blink as it connects to your network.
3.  Determine the device's IP address from your router's client list.

!!! tip "Use a Static IP"
    It is strongly advised to configure a static IP address or DHCP reservation for your coordinator in your router's settings. This prevents connection issues if the IP address changes.

For **USB Coordinators**:

1.  Simply plug the coordinator into an available USB port on your Home Assistant machine. It should be auto-discovered.

---

## Home Assistant (ZHA) Setup

Follow these instructions to configure your coordinator with the built-in ZHA integration.

### Method 1: Auto-Discovery (Recommended)

If Home Assistant discovers the device automatically, you will see a notification. Simply click through the configuration flow to add it to Home Assistant.

<figure markdown>
  ![ZHA Discovery Notification](https://github.com/tube0013/tube_gateways/raw/main/images/discover0.png){ width="400" }
  <figcaption>ZHA Discovery Notification</figcaption>
</figure>

<figure markdown>
  ![ZHA Discovery Configuration](https://github.com/tube0013/tube_gateways/raw/main/images/discover1.png){ width="400" }
  <figcaption>ZHA Discovery Configuration</figcaption>
</figure>

### Method 2: Manual Setup

If your coordinator is not discovered automatically, follow these steps:

1.  Navigate to **Settings > Devices & Services** and click **Add Integration**.
2.  Search for and select **Zigbee Home Automation**.
    ![Add ZHA Integration](https://github.com/tube0013/tube_gateways/raw/main/images/manual1.png){ width="400" }
3.  When asked, choose to **Set up another instance of Zigbee Home Automation**.
    ![Set up another instance](https://github.com/tube0013/tube_gateways/raw/main/images/manual2.png){ width="400" }
4.  Select the **Radio Type** based on your coordinator model:
    * For **CC2652p** based gateways, select **ZNP**.
    * For **EFR32** based gateways, select **EZSP**.
5.  In the Port Specific Settings dialog:
    * Enter `socket://IP_ADDRESS:6638` (replace `IP_ADDRESS` with your device's actual IP).
    * Set Port Speed to `115200`.
    * Select **Software** Flow Control.
    ![ZHA Serial Port Settings](https://github.com/tube0013/tube_gateways/raw/main/images/serialportsettings.png){ width="400" }

---

## Zigbee2MQTT Setup

!!! warning "ZHA vs. Zigbee2MQTT"
    A coordinator can only be controlled by **one** service at a time. If Home Assistant auto-discovers the device for ZHA, you **must** choose to **Ignore** it before setting up Zigbee2MQTT.
    ![Ignore ZHA Discovery](https://github.com/tube0013/tube_gateways/raw/main/images/ignore.png){ width="300" }

!!! note "EFR32 Support"
    At this time, only CC2652p based gateways are officially supported by Zigbee2MQTT. EFR32 gateways may work but are not recommended.

### Configuring the `serial` section

Whether you are using the Zigbee2MQTT addon or a standalone `configuration.yaml` file, you will need to edit the `serial` section.

1.  Navigate to the Zigbee2MQTT addon **Configuration** tab or open your `configuration.yaml` file.
2.  Find the `serial:` block. If it doesn't exist, add it.
3.  Use the tabs below to copy the correct configuration for your device.

<figure markdown>
  ![Zigbee2MQTT Addon Configuration](https://community-assets.home-assistant.io/original/3X/8/8/882560527d35352c87513069752533277c2509c3.png){ width="600" }
  <figcaption>Editing the serial settings in the addon configuration tab.</figcaption>
</figure>

=== "Network Coordinator (Ethernet)"

    For coordinators connected via Ethernet, use the `tcp://` port format. Replace `IP_ADDRESS` with your device's actual IP.

    ```yaml
    serial:
      port: 'tcp://IP_ADDRESS:6638'
      # adapter: zstack  # For CC2652 based radios
      # adapter: ember   # For EFR32 based radios
    ```

=== "USB Coordinator"

    For coordinators connected via USB, find the device path under **Settings > System > Hardware > All Hardware**. It will start with `/dev/serial/by-id/...`.

    ```yaml
    serial:
      port: '/dev/serial/by-id/usb-1a86_TubesZB_971207DO-if00-port0'
      # adapter: zstack  # For CC2652 based radios
      # adapter: ember   # For EFR32 based radios
    ```

---

## ESPHome Web Interface

The ESP32 microcontroller inside the gateway runs ESPHome. You can access its web interface by navigating to the device's IP address in a browser.

!!! danger "Ignore ESPHome Entities in Home Assistant"
    ESPHome creates switch entities in Home Assistant that are used to prep the Zigbee module for firmware updates. It is **highly advised** to ignore or disable these entities. Accidentally toggling them can reset the Zigbee module and disrupt your network.

## Firmware Updates
Firmware update instructions can be found on the individual product pages.