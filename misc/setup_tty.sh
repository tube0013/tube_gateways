#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

# --- Cleanup Function ---
# This function will be called when the script exits, to clean up temporary files.
cleanup() {
    echo "" # Newline for cleaner exit
    echo "🧹 Running cleanup of /tmp directory..."
    rm -rf /tmp/tty0tty
    echo "✅ Temporary files removed."
}

# Trap the exit signal to run the cleanup function
trap cleanup EXIT

# --- Main Functions ---

# Function for the entire first-time installation process
install_tty0tty() {
    echo "➡️ Step 1: Detecting OS and installing dependencies..."

    # Check /etc/os-release for the OS ID
    if grep -q 'ID=raspbian' /etc/os-release; then
        echo "   - Raspberry Pi OS detected."
        HEADERS_PACKAGE="raspberrypi-kernel-headers"
    else
        echo "   - Debian/Ubuntu based OS detected."
        HEADERS_PACKAGE="linux-headers-$(uname -r)"
    fi

    sudo apt-get update
    sudo apt-get install -y git build-essential "$HEADERS_PACKAGE" socat

    echo "➡️ Step 2: Downloading, building, and installing the tty0tty kernel module..."
    rm -rf /tmp/tty0tty
    git clone https://github.com/freemed/tty0tty.git /tmp/tty0tty

    cd /tmp/tty0tty/module
    echo "   - Compiling module (make)..."
    make
    echo "   - Installing module (sudo make modules_install)..."
    sudo make modules_install
    cd - &>/dev/null

    echo "➡️ Step 3: Updating module dependencies..."
    sudo depmod -a

    echo "➡️ Step 4: Configuring module to load on boot..."
    if grep -q "^tty0tty$" /etc/modules; then
        echo "✅ Module is already configured to load on boot."
    else
        echo "tty0tty" | sudo tee -a /etc/modules
        echo "✅ Module added to /etc/modules to persist across reboots."
    fi
}

# Function to run the final setup and socat bridge
run_setup_and_bridge() {
    echo "➡️ Step A: Loading tty0tty module into the kernel..."
    # Load module if it's not already loaded
    if ! lsmod | grep -q 'tty0tty'; then
        sudo modprobe tty0tty
    fi
    ls -l /dev/tnt* &> /dev/null || { echo "❌ ERROR: /dev/tnt* devices not found! Aborting."; exit 1; }
    echo "✅ Module loaded successfully. Virtual ports created."

    echo "➡️ Step B: Checking user group permissions..."
    if groups $(whoami) | grep -q '\bdialout\b'; then
        echo "✅ User $(whoami) is already in the 'dialout' group."
    else
        echo "⚠️  User not in 'dialout' group. Adding..."
        sudo adduser $(whoami) dialout
        RELOGIN_MSG="You must log out and log back in for group changes to take effect."
        if grep -q 'ID=raspbian' /etc/os-release; then
            RELOGIN_MSG="A full reboot is recommended on Raspberry Pi for group changes to apply."
        fi
        echo "🔔 IMPORTANT: $RELOGIN_MSG"
        echo "After completing that, please re-run this script."
        exit 1
    fi

    echo "--------------------------------------------------------------------------"
    read -p "➡️ Step C: Please enter the IP address and port of your device (e.g., 192.168.1.100:9999): " ZIGBEE_TARGET

    if [[ ! "$ZIGBEE_TARGET" == *":"* ]]; then
        echo "❌ ERROR: Invalid format. Please use IP:PORT format."
        exit 1
    fi

    echo ""
    echo "✅ All set! Starting the bridge..."
    echo "--------------------------------------------------------------------------"
    echo "🟢 SOCAT IS RUNNING."
    echo "   Bridging virtual port /dev/tnt1 to TCP target ${ZIGBEE_TARGET}"
    echo ""
    echo "   INSTRUCTIONS:"
    echo "   1. Keep this terminal window open!"
    echo "   2. Open Chrome/Chromium and navigate to your web flashing page."
    echo "   3. When prompted, select '/dev/tnt0' as the serial port."
    echo ""
    echo "   Press [CTRL+C] in this window to stop the connection."
    echo "--------------------------------------------------------------------------"

    socat /dev/tnt1,raw,echo=0 tcp:$ZIGBEE_TARGET
}


# --- Main Script Logic ---
# Check if the module is already known to the system.
if modinfo tty0tty &>/dev/null; then
    echo "✅ tty0tty module is already installed. Skipping installation."
else
    echo "ℹ️ tty0tty module not found. Starting first-time installation..."
    install_tty0tty
fi

# Run the final setup steps
run_setup_and_bridge