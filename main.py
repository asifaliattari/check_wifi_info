import streamlit as st
import subprocess
import re


# Function to get WiFi password
def get_wifi_password():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", result.stdout)
        
        wifi_data = {}
        for profile in profiles:
            profile = profile.strip()
            result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
            password_match = re.search(r"Key Content\s*:\s*(.*)", result.stdout)
            wifi_data[profile] = password_match.group(1) if password_match else "No Password Found"
        
        return wifi_data
    except Exception as e:
        return {"Error": str(e)}

# Function to get connected devices
def get_connected_devices():
    try:
        result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        devices = re.findall(r"(\d+\.\d+\.\d+\.\d+)", result.stdout)
        return devices
    except Exception as e:
        return ["Error: " + str(e)]

# Function to get the local machine's IP address
def get_local_ip():
    try:
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        match = re.search(r"IPv4 Address[.\s]+: (\d+\.\d+\.\d+\.\d+)", result.stdout)
        return match.group(1) if match else "Error"
    except Exception as e:
        return str(e)

# Function to get WiFi signal strength
def get_signal_strength():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
        match = re.search(r"Signal\s*:\s*(\d+)", result.stdout)
        return f"{match.group(1)}%" if match else "Error retrieving signal"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to get the MAC address of connected devices
def get_mac_addresses():
    try:
        result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        mac_addresses = re.findall(r"([a-fA-F0-9]{2}[:]){5}[a-fA-F0-9]{2}", result.stdout)
        return mac_addresses
    except Exception as e:
        return ["Error: " + str(e)]

# Save WiFi password to file
def save_wifi_password_to_file(wifi_data):
    try:
        with open("wifi_passwords.txt", "w") as f:
            for wifi, password in wifi_data.items():
                f.write(f"WiFi: {wifi}\nPassword: {password}\n\n")
        return "WiFi passwords saved to wifi_passwords.txt"
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Check Wifi Password and Connected Devices")

option = st.sidebar.radio("Select an option", ["Check WiFi Password", "Connected Devices",  "Signal Strength", "Save WiFi Password"])

# Check saved WiFi passwords
if option == "Check WiFi Password":
    st.subheader("Saved WiFi Passwords")
    passwords = get_wifi_password()
    for wifi, pwd in passwords.items():
        st.write(f"**{wifi}**: {pwd}")

# List connected devices to the router
elif option == "Connected Devices":
    st.subheader("Devices Connected to Router")
    devices = get_connected_devices()
    st.write("Connected IPs:")
    for device in devices:
        st.write(device)

# Show WiFi signal strength
elif option == "Signal Strength":
    st.subheader("WiFi Signal Strength")
    signal_strength = get_signal_strength()
    st.write(f"Signal Strength: {signal_strength}")

# Save WiFi password to file
elif option == "Save WiFi Password":
    st.subheader("Save Your WiFi Passwords to a File")
    passwords = get_wifi_password()
    if passwords:
        result = save_wifi_password_to_file(passwords)
        st.write(result)
    else:
        st.write("No WiFi passwords found.")

# Show connected device IP and MAC
local_ip = get_local_ip()
mac_addresses = get_mac_addresses()

st.sidebar.subheader("Your Local IP Address")
st.sidebar.write(local_ip)

st.sidebar.subheader("Connected Devices' MAC Addresses")
if mac_addresses:
    for mac in mac_addresses:
        st.sidebar.write(mac)
else:
    st.sidebar.write("No devices found.")
