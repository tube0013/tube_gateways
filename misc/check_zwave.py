import serial
import time
import argparse
import sys

# Z-Wave Serial API constants
SOF = 0x01  # Start Of Frame
ACK = 0x06  # Acknowledge
NAK = 0x15  # Not Acknowledged

# Frame types
REQUEST = 0x00
RESPONSE = 0x01

# Z-Wave Commands
FUNC_ID_GET_VERSION = 0x15

def calculate_checksum(frame_data):
    """Calculates the Z-Wave checksum (XOR of all bytes)."""
    checksum = 0xFF
    for byte in frame_data:
        checksum ^= byte
    return checksum

def main():
    parser = argparse.ArgumentParser(description="Z-Wave Radio Basic Functionality Check")
    parser.add_argument("port", help="Serial port or socket URI (e.g., COM3, /dev/ttyACM0, or 'socket://host:port')")
    parser.add_argument("--timeout", type=float, default=2.0, help="Serial port read timeout in seconds")
    args = parser.parse_args()

    print(f"Attempting to connect to Z-Wave radio on {args.port}...")

    try:
        # --- THIS IS THE CORRECTED LINE ---
        # Use serial_for_url which is more robust for socket:// schemes.
        # Baudrate is ignored for sockets but is needed for real serial ports.
        ser = serial.serial_for_url(args.port, timeout=args.timeout)
        
    except serial.SerialException as e:
        print(f"Error: Could not open port {args.port}. {e}")
        sys.exit(1)

    with ser:
        print(f"Successfully opened port: {ser.name}")
        
        # Construct the GET_VERSION command frame
        frame_core = bytes([
            0x03, # Length of frame (this field + type + cmd)
            REQUEST, # Type: Request
            FUNC_ID_GET_VERSION # Command
        ])
        checksum = calculate_checksum(frame_core)
        command = bytes([SOF]) + frame_core + bytes([checksum])
        
        print(f"-> Sending GET_VERSION command: {command.hex(' ')}")
        ser.write(command)

        # Wait for ACK
        ack = ser.read(1)
        if not ack:
            print("Error: Timed out waiting for ACK from the controller.")
            sys.exit(1)
        if ack != bytes([ACK]):
            print(f"Error: Expected ACK (0x06) but received {ack.hex()}.")
            sys.exit(1)

        print("<- Received ACK (0x06). Controller is listening.")

        # Wait for the full response frame
        response = ser.read(1) # Read SOF
        if response != bytes([SOF]):
            print(f"Error: Expected SOF (0x01) for response frame but got {response.hex()}.")
            sys.exit(1)
        
        response_data = ser.read(128)
        if len(response_data) < 4:
            print("Error: Incomplete response frame received.")
            sys.exit(1)
            
        print(f"<- Received Response Frame: {response.hex(' ')} {response_data.hex(' ')}")

        # Decode and print the result
        version_string = response_data[3:3+12].decode('ascii', errors='ignore').strip('\x00')
        library_type = response_data[15]

        library_map = {
            0x01: "Static Controller", 0x02: "Controller", 0x03: "Enhanced Slave",
            0x04: "Slave", 0x05: "Installer", 0x06: "Routing Slave",
            0x07: "Bridge Controller", 0x08: "Device Under Test",
        }

        print("\n🎉 Success! Z-Wave Radio is alive and responding.")
        print("==============================================")
        print(f"  Z-Wave Library Version: {version_string}")
        print(f"  Library Type:           0x{library_type:02x} ({library_map.get(library_type, 'Unknown')})")
        print("==============================================")

if __name__ == "__main__":
    main()
