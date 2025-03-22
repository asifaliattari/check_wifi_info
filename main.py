import streamlit as st
import subprocess
import psutil

# Function to get saved WiFi passwords
def get_saved_wifi_passwords():
    wifi_passwords = {}
    try:
        # Get all Wi-Fi profiles
        profiles = subprocess.check_output('netsh wlan show profiles', shell=True).decode('utf-8', errors="backslashreplace")
        profiles = [x.split(":")[-1][1:-1] for x in profiles.split("\n") if "All User Profile" in x]
        
        for profile in profiles:
            try:
                # Get the password for each profile
                password = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True).decode('utf-8', errors="backslashreplace")
                password = [x.split(":")[-1][1:-1] for x in password.split("\n") if "Key Content" in x]
                if password:
                    wifi_passwords[profile] = password[0]
                else:
                    wifi_passwords[profile] = "No password set"
            except subprocess.CalledProcessError:
                wifi_passwords[profile] = "No password found"
    except subprocess.CalledProcessError:
        wifi_passwords = {}
    return wifi_passwords

# Function to get connected devices on the same network
def get_connected_devices():
    devices = []
    try:
        # Run the arp command to get all devices connected to the same network
        result = subprocess.check_output('arp -a', shell=True).decode('utf-8', errors="backslashreplace")
        devices = [line.split()[0] for line in result.splitlines()[3:] if len(line.split()) >= 2]
    except subprocess.CalledProcessError:
        devices = []
    return devices

# Streamlit UI components
def app():
    st.title("WiFi Passwords and Connected Devices Viewer")

    # Button to get saved WiFi passwords
    if st.button('Show Saved WiFi Passwords'):
        st.subheader("Saved WiFi Passwords:")
        wifi_passwords = get_saved_wifi_passwords()
        if wifi_passwords:
            for wifi, password in wifi_passwords.items():
                st.write(f"{wifi}: {password}")
        else:
            st.write("No saved WiFi passwords found.")
    
    # Button to show connected devices
    if st.button('Show Connected Devices'):
        st.subheader("Devices Connected to the Network:")
        connected_devices = get_connected_devices()
        if connected_devices:
            for device in connected_devices:
                st.write(device)
        else:
            st.write("No devices found or unable to fetch connected devices.")

# Run the Streamlit app
if __name__ == "__main__":
    app()
