import argparse
import asyncio
import sys
import logging
import os
import traceback

# Configure basic logging
logging.basicConfig(level=logging.INFO)
# Set library logging to WARNING to keep the output clean
logging.getLogger("bellows").setLevel(logging.WARNING)
logging.getLogger("zigpy_znp").setLevel(logging.WARNING)


# --- Check for and import required libraries ---
try:
    from bellows.zigbee.application import ControllerApplication as BellowsApp
    # We need the types for the getValue call
    import bellows.types
    BELLOWS_AVAILABLE = True
except ImportError:
    BELLOWS_AVAILABLE = False

try:
    from zigpy_znp.zigbee.application import ControllerApplication as ZNPApp
    ZNP_AVAILABLE = True
except ImportError:
    ZNP_AVAILABLE = False

# --- EZSP (Bellows) Checker ---
async def check_ezsp(device_path, baudrate):
    """Attempts to connect to a device as an EZSP coordinator."""
    if not BELLOWS_AVAILABLE:
        return False

    print("\n--- [1/2] PROBING FOR EZSP (Silicon Labs) ---")
    radio = None
    try:
        config = {
            'device': {'path': device_path, 'baudrate': baudrate},
            'database_path': None, # No database needed for this check
        }
        radio = BellowsApp(config=config)
        # Use .connect() for a low-level check without forming a network
        await radio.connect()
        
        # Fetch only the firmware version info
        version_info_list = await radio._ezsp.getValue(
            bellows.types.EzspValueId.VALUE_VERSION_INFO
        )
        
        # The value is the second element in the returned list
        version_info_bytes = version_info_list[1]
        
        # Parse the binary data into a readable version string
        if len(version_info_bytes) >= 6:
            major = version_info_bytes[2]
            minor = version_info_bytes[3]
            patch = version_info_bytes[4]
            build = version_info_bytes[5]
            firmware_version = f"{major}.{minor}.{patch}.{build}"
        else:
            firmware_version = version_info_bytes.hex(' ') # Fallback to hex
        
        print("\n✅ SUCCESS: Detected EZSP-based coordinator.")
        print("==============================================")
        print(f"  Firmware:       {firmware_version}")
        print("==============================================")
        return True
    
    except Exception:
        print(f"  INFO: Device is not responding as EZSP.")
        return False
    finally:
        if radio:
            # Gracefully handle disconnection errors
            try:
                await radio.disconnect()
            except Exception:
                pass

# --- ZNP (zigpy-znp) Checker ---
async def check_znp(device_path, baudrate):
    """Attempts to connect to a device as a ZNP coordinator."""
    if not ZNP_AVAILABLE:
        return False

    print("\n--- [2/2] PROBING FOR ZNP (Texas Instruments) ---")
    znp = None
    try:
        config = {'device': {'path': device_path, 'baudrate': baudrate}}
        znp = ZNPApp(config=config)
        # Use .connect() for a low-level check
        await znp.connect()
        
        # Fetch only the version information
        version_info = znp._znp.version
        
        print("\n✅ SUCCESS: Detected ZNP-based coordinator.")
        print("==============================================")
        print(f"  Protocol:     ZNP")
        print(f"  Z-Stack Ver:  {version_info}")
        print("==============================================")
        return True

    except Exception:
        print(f"  INFO: Device is not responding as ZNP.")
        return False
    finally:
        if znp:
            # Gracefully handle disconnection errors
            try:
                await znp.disconnect()
            except Exception:
                pass

async def main():
    """Main function to parse args and run checks."""
    if not BELLOWS_AVAILABLE or not ZNP_AVAILABLE:
        print("\n❌ FATAL: Required libraries 'bellows' or 'zigpy-znp' could not be imported.")
        print("Please ensure they are installed in the correct environment:")
        print("  pip install bellows zigpy-znp")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Universal Zigbee Coordinator Check")
    parser.add_argument("device", help="Serial port or socket URI (e.g., /dev/ttyACM0 or 'socket://host:port')")
    parser.add_argument("--baudrate", type=int, default=115200, help="Baud rate for the serial connection")
    args = parser.parse_args()

    print(f"\nStarting Zigbee radio check on {args.device} at {args.baudrate} baud...")

    if await check_ezsp(args.device, args.baudrate):
        sys.exit(0)

    if await check_znp(args.device, args.baudrate):
        sys.exit(0)

    print("\n❌ FAILED: Could not detect a known Zigbee radio (EZSP or ZNP).")
    print("Please check the following:")
    print("  1. The device path is correct.")
    print("  2. The device is properly plugged in and powered.")
    print("  3. The baud rate is correct (115200 is common, but some use 57600).")
    print("  4. The device is not in use by another program (e.g., Home Assistant, Zigbee2MQTT).")
    sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting.")

