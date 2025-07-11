# Getting Started with the Z-Wave PoE Kit

This guide will walk you through setting up your new TubeZB Z-Wave PoE Kit with Home Assistant.

!!! info "For New Z-Wave Networks"
    This guide covers the process for creating a brand new Z-Wave network. If you need to migrate an existing network from a different Z-Wave stick, please refer to the advanced documentation (coming soon).

## 1. Physical Setup

Your setup steps will depend on whether you purchased the kit with the Zooz Z-Wave module pre-installed or the "No Radio" version.

### Option A: Kit with Pre-installed Zooz ZAC93

If you purchased the kit with the Zooz ZAC93 module included, it comes pre-installed and ready to go.

1.  Connect the Z-Wave PoE Kit to your local network using an ethernet cable that provides Power over Ethernet (PoE).
2.  The device will power on and connect to your network.
3.  Find the IP Address assigned to the device from your router's client list.

!!! tip "Use a DHCP Reservation (Recommended)"
    To ensure the device's IP address doesn't change, it is strongly advised to configure a **DHCP Reservation** for it in your router's settings. This links the device's unique MAC address to a specific IP, so it gets the same one every time it connects.

    !!! info "Advanced: Static IP Firmware"
        Setting a true static IP requires custom firmware. For advanced users who need this, you can build a custom firmware binary using the **[TubesZB ESPHome Firmware Builder](https://github.com/tube0013/TubesZB-ESPHome-Builder)**.

!!! success "Register Your Zooz Module!"
    If you purchased a kit including the Zooz ZAC93, be sure to **[register your module with Zooz](https://www.getzooz.com/register/)** within 30 days of purchase. This gives you a 5-Year Extended Warranty, direct access to firmware updates, and expedited support.

### Option B: Kit with No Radio (Bring Your Own Module)

If you purchased the "No Radio" version of the kit, you will need to provide and install your own compatible Z-Wave module.

#### Compatible Modules

This kit is designed for Z-Wave modules that use the Raspberry Pi GPIO pin layout.

* **[Zooz 800 Long Range ZAC93](https://amzn.to/3O2ewpM)**
* **[Z-Wave.me RaZberry 7 Pro](https://amzn.to/41XOFVK)**

!!! info "Affiliate Link Disclosure"
    The links above are Amazon affiliate links. As an Amazon Associate, I earn from qualifying purchases.

#### Installation

1.  Carefully open the 3D printed enclosure.
2.  Align the GPIO pins on your Z-Wave module with the female GPIO header on the Olimex ESP32-PoE board.
3.  Press down firmly and evenly to seat the module securely. Ensure all pins are correctly engaged.
4.  Close the enclosure.
5.  Follow the steps in **Option A** to connect the device to your network and find its IP address.

---

## 2. Home Assistant Setup

The recommended method for using this Z-Wave kit is with the **Z-Wave JS UI** addon in Home Assistant.

1.  **Install and Start the Addon:**
    * Click the badge below to open the Z-Wave JS UI addon page in your Home Assistant instance and click **Install**.

    [![Open your Home Assistant instance and show the dashboard of an add-on.](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_zwavejs2mqtt&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository)

    * Once installed, go to the **Info** tab and **Start** the addon.

2.  **Configure the Addon via the Web UI:**
    * After the addon has started, click **Open Web UI**.
    * In the Z-Wave JS UI interface, navigate to **Settings** (the gear icon) and then select **Z-Wave**.
    * In the **Serial Port** field, enter the network path for your Z-Wave kit, replacing `IP_ADDRESS` with the IP you found earlier:
      ```
      tcp://IP_ADDRESS:6638
      ```
    * **Generate and Save Security Keys:**
        !!! danger "Critical Step for New Networks"
            If you are setting up a **new** network, you **must** generate new security keys. These keys are essential for securely including devices and for backing up your network.
            1. Scroll down to the **Security Keys** section.
            2. Click the refresh icon next to **each** of the four keys (`S2_AccessControl`, `S2_Authenticated`, `S2_Unauthenticated`, and `S0_Legacy`) to generate new random values.
            3. **Copy and save these keys somewhere safe**, like a password manager. You will need them if you ever have to restore your network.

    * Click **Save** at the bottom of the page. The addon will restart and connect to your Z-Wave PoE Kit. You can check the **Control Panel** to see your Z-Wave stick appear as the controller.

3.  **Install the Z-Wave JS Integration:**
    * Navigate back to Home Assistant and go to **Settings > Devices & Services**.
    * Home Assistant should now auto-discover the Z-Wave JS integration. Click **Configure** and follow the prompts to add it.
    * If it is not discovered, click **Add Integration**, search for **Z-Wave**, and follow the prompts. It will automatically connect to the running Z-Wave JS UI addon.
