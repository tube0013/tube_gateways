# Flashing Firware on a TubesZB MGM24 Coordinator using Universal-silabs-flasher

This guide provides step-by-step instructions for flashing a Network Co-Processor (NCP) `.gbl` firmware file to the Tube's Zigbee MGM24 PoE Coordinator over a remote TCP socket using the `universal-silabs-flasher`.

If you use HAOS and can install addons I recommend you use the [TubesZB Silicon Labs Flasher Add-on](https://github.com/tube0013/tubeszb_addons/blob/main/tzb-silabs-flasher/DOCS.md)

## Requirements

- **Tube's Zigbee MGM24 PoE Coordinator**
- **NCP `.gbl` file** for the MGM24 (e.g., `your_firmware.gbl`)  
  - You can download the latest `.gbl` firmware files from the [Tube Gateways Firmware Repository](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-efr32-MGM24/firmware/mgm24/ncp).
- **Universal Silabs Flasher** software
- A computer with **Python 3.7+**
- **IP Address and Port** of the remote device socket

## Installation

### Step 1: Set Up a Python Virtual Environment

1. **Install Python 3.7+**  
   Make sure Python 3.7 or higher is installed. You can check your version by running:  
   ```python3 --version```

2. **Create a Virtual Environment**  
   In the directory where you want to set up the project, create a virtual environment:  
   ```python3 -m venv env```

3. **Activate the Virtual Environment**  
   - On **Linux/macOS**:  
     ```source env/bin/activate```
   - On **Windows**:  
     ```.\env\Scripts\activate```

   You should now see `(env)` at the beginning of your command line, indicating that the virtual environment is active.

### Step 2: Install Universal Silabs Flasher

Install `universal-silabs-flasher` directly from PyPI:  
```pip install universal-silabs-flasher```

For more details, you can visit the [universal-silabs-flasher GitHub repository](https://github.com/NabuCasa/universal-silabs-flasher).

## Flashing the Firmware Over a TCP Socket

1. **Get the Device IP Address and Port**  
   Ensure you have the correct IP address and port for the MGM24 Coordinator's remote TCP socket.

2. **Disable ZHA/Zigbee2MQTT**
   Ensure no services are connecting to the TCP Serial Port. You can check this by going to the coordinator's web frontend and observing the Serial Connected sensor state.

3. **Flash the NCP `.gbl` File**  
   Use `universal-silabs-flasher` to flash the `.gbl` file to the MGM24 Coordinator over the TCP socket by specifying the address in `socket://IP_ADDRESS:PORT` format:  
   ```universal-silabs-flasher --device socket://<IP_ADDRESS>:<PORT> --bootloader-baudrate 115200 --ezsp-baudrate 115200 flash --firmware--firmware your_firmware.gbl```

   Replace `<IP_ADDRESS>` and `<PORT>` with the actual IP address and port of your coordinator, and `your_firmware.gbl` with the path to your `.gbl` file.

   **Example Command:**  
   ```universal-silabs-flasher --device socket://192.168.1.100:6638 --bootloader-baudrate 115200 --ezsp-baudrate 115200 flash --firmware--firmware your_firmware.gbl```

4. **Wait for Flashing to Complete**  
   The flashing process will take a minute or 2 to complete. Once finished, you should see the progress bar showing 100% indicating that the firmware has been flashed successfully.

5. **Deactivate the Virtual Environment**  
   After you're done, you can deactivate the virtual environment by running:  
   ```deactivate```

6. **Restart ZHA/Zigbee2MQTT**
   Check logs for any errors.

## Troubleshooting

- **Errors*  
  Make sure ZHA or Zigbee2MQTT are shutdown and nothing is accessing the TCP Serial Port
  Ensure that the coordinator is properly connected and that the correct IP address and port are specified.

---

## Additional Resources

- [TubesZB GitHub Resository](https://github.com/tube0013/tube_gateways)
- [Universal Silabs Flasher GitHub Repository](https://github.com/NabuCasa/universal-silabs-flasher)
- [Latest NCP Firmware Files for MGM24 Coordinators](https://github.com/tube0013/tube_gateways/tree/main/models/current/tubeszb-efr32-MGM24/firmware/mgm24/ncp)

---

This guide should help you flash the NCP firmware to the Tube's Zigbee MGM24 PoE Coordinator over a TCP socket using a Python virtual environment.
