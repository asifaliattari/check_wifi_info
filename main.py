import streamlit as st
import subprocess
import re
import platform

# Function to get WiFi password (Windows-only)
def get_wifi_password():
    try:
        system = platform.system()
        if system == 'Windows':
            st.write("Running on Windows.")  # Debug line
            result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
            profiles = re.findall(r"All User Profile\s*:\s*(.*)", result.stdout)

            wifi_data = {}
            for profile in profiles:
                profile = profile.strip()
                result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
                password_match = re.search(r"Key Content\s*:\s*(.*)", result.stdout)
                wifi_data[profile] = password_match.group(1) if password_match else "No Password Found"
            
            return wifi_data
        else:
            st.write(f"WiFi password retrieval is supported only on Windows, but you are on {system}.")  # Debug line
            return {"Error": f"WiFi password retrieval is supported only on Windows, but you are on {system}."}
    except Exception as e:
        return {"Error": str(e)}

# Function to get connected devices (Works on Windows, Linux/macOS alternative could be added)
def get_connected_devices():
    try:
        system = platform.system()
        if system == 'Windows':
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
            devices = re.findall(r"(\d+\.\d+\.\d+\.\d+)", result.stdout)
            return devices
        else:
            return ["Error: Device detection is supported only on Windows."]
    except Exception as e:
        return ["Error: " + str(e)]

# Function to get the local machine's IP address
def get_local_ip():
    try:
        system = platform.system()
        if system == 'Windows':
            result = subprocess.run(["ipconfig"], capture_output=True, text=True)
            match = re.search(r"IPv4 Address[.\s]+: (\d+\.\d+\.\d+\.\d+)", result.stdout)
            return match.group(1) if match else "Error"
        else:
            # For Linux/macOS, use 'hostname' to get the local IP
            result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
            return result.stdout.strip() if result.returncode == 0 else "Error"
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("WiFi and Network Information Manager")

option = st.sidebar.radio("Select an option", ["Check WiFi Password", "Connected Devices", "Your Local IP"])

if option == "Check WiFi Password":
    st.write(f"Platform: {platform.system()}")  # Debug line
    if platform.system() == 'Windows':
        st.subheader("Saved WiFi Passwords")
        passwords = get_wifi_password()
        if "Error" in passwords:
            st.write(passwords["Error"])
        else:
            for wifi, pwd in passwords.items():
                st.write(f"**{wifi}**: {pwd}")
    else:
        st.write("WiFi password retrieval is supported only on Windows.")

elif option == "Connected Devices":
    st.subheader("Devices Connected to Your Network")
    devices = get_connected_devices()
    if "Error" in devices:
        st.write(devices[0])
    else:
        st.write("Connected Devices IPs:")
        for device in devices:
            st.write(device)

elif option == "Your Local IP":
    st.subheader("Your Local IP Address")
    local_ip = get_local_ip()
    st.write(local_ip)
import streamlit as st
import subprocess
import re
import platform

# Function to get WiFi password (Windows-only)
def get_wifi_password():
    try:
        system = platform.system()
        if system == 'Windows':
            st.write("Running on Windows.")  # Debug line
            result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
            profiles = re.findall(r"All User Profile\s*:\s*(.*)", result.stdout)

            wifi_data = {}
            for profile in profiles:
                profile = profile.strip()
                result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
                password_match = re.search(r"Key Content\s*:\s*(.*)", result.stdout)
                wifi_data[profile] = password_match.group(1) if password_match else "No Password Found"
            
            return wifi_data
        else:
            st.write(f"WiFi password retrieval is supported only on Windows, but you are on {system}.")  # Debug line
            return {"Error": f"WiFi password retrieval is supported only on Windows, but you are on {system}."}
    except Exception as e:
        return {"Error": str(e)}

# Function to get connected devices (Works on Windows, Linux/macOS alternative could be added)
def get_connected_devices():
    try:
        system = platform.system()
        if system == 'Windows':
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
            devices = re.findall(r"(\d+\.\d+\.\d+\.\d+)", result.stdout)
            return devices
        else:
            return ["Error: Device detection is supported only on Windows."]
    except Exception as e:
        return ["Error: " + str(e)]

# Function to get the local machine's IP address
def get_local_ip():
    try:
        system = platform.system()
        if system == 'Windows':
            result = subprocess.run(["ipconfig"], capture_output=True, text=True)
            match = re.search(r"IPv4 Address[.\s]+: (\d+\.\d+\.\d+\.\d+)", result.stdout)
            return match.group(1) if match else "Error"
        else:
            # For Linux/macOS, use 'hostname' to get the local IP
            result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
            return result.stdout.strip() if result.returncode == 0 else "Error"
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("WiFi and Network Information Manager")

option = st.sidebar.radio("Select an option", ["Check WiFi Password", "Connected Devices", "Your Local IP"])

if option == "Check WiFi Password":
    st.write(f"Platform: {platform.system()}")  # Debug line
    if platform.system() == 'Windows':
        st.subheader("Saved WiFi Passwords")
        passwords = get_wifi_password()
        if "Error" in passwords:
            st.write(passwords["Error"])
        else:
            for wifi, pwd in passwords.items():
                st.write(f"**{wifi}**: {pwd}")
    else:
        st.write("WiFi password retrieval is supported only on Windows.")

elif option == "Connected Devices":
    st.subheader("Devices Connected to Your Network")
    devices = get_connected_devices()
    if "Error" in devices:
        st.write(devices[0])
    else:
        st.write("Connected Devices IPs:")
        for device in devices:
            st.write(device)

elif option == "Your Local IP":
    st.subheader("Your Local IP Address")
    local_ip = get_local_ip()
    st.write(local_ip)
import streamlit as st
import subprocess
import re
import platform

# Function to get WiFi password (Windows-only)
def get_wifi_password():
    try:
        system = platform.system()
        if system == 'Windows':
            st.write("Running on Windows.")  # Debug line
            result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
            profiles = re.findall(r"All User Profile\s*:\s*(.*)", result.stdout)

            wifi_data = {}
            for profile in profiles:
                profile = profile.strip()
                result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
                password_match = re.search(r"Key Content\s*:\s*(.*)", result.stdout)
                wifi_data[profile] = password_match.group(1) if password_match else "No Password Found"
            
            return wifi_data
        else:
            st.write(f"WiFi password retrieval is supported only on Windows, but you are on {system}.")  # Debug line
            return {"Error": f"WiFi password retrieval is supported only on Windows, but you are on {system}."}
    except Exception as e:
        return {"Error": str(e)}

# Function to get connected devices (Works on Windows, Linux/macOS alternative could be added)
def get_connected_devices():
    try:
        system = platform.system()
        if system == 'Windows':
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
            devices = re.findall(r"(\d+\.\d+\.\d+\.\d+)", result.stdout)
            return devices
        else:
            return ["Error: Device detection is supported only on Windows."]
    except Exception as e:
        return ["Error: " + str(e)]

# Function to get the local machine's IP address
def get_local_ip():
    try:
        system = platform.system()
        if system == 'Windows':
            result = subprocess.run(["ipconfig"], capture_output=True, text=True)
            match = re.search(r"IPv4 Address[.\s]+: (\d+\.\d+\.\d+\.\d+)", result.stdout)
            return match.group(1) if match else "Error"
        else:
            # For Linux/macOS, use 'hostname' to get the local IP
            result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
            return result.stdout.strip() if result.returncode == 0 else "Error"
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("WiFi and Network Information Manager")

option = st.sidebar.radio("Select an option", ["Check WiFi Password", "Connected Devices", "Your Local IP"])

if option == "Check WiFi Password":
    st.write(f"Platform: {platform.system()}")  # Debug line
    if platform.system() == 'Windows':
        st.subheader("Saved WiFi Passwords")
        passwords = get_wifi_password()
        if "Error" in passwords:
            st.write(passwords["Error"])
        else:
            for wifi, pwd in passwords.items():
                st.write(f"**{wifi}**: {pwd}")
    else:
        st.write("WiFi password retrieval is supported only on Windows.")

elif option == "Connected Devices":
    st.subheader("Devices Connected to Your Network")
    devices = get_connected_devices()
    if "Error" in devices:
        st.write(devices[0])
    else:
        st.write("Connected Devices IPs:")
        for device in devices:
            st.write(device)

elif option == "Your Local IP":
    st.subheader("Your Local IP Address")
    local_ip = get_local_ip()
    st.write(local_ip)
import streamlit as st
import subprocess
import re
import platform

# Function to get WiFi password (Windows-only)
def get_wifi_password():
    try:
        system = platform.system()
        if system == 'Windows':
            st.write("Running on Windows.")  # Debug line
            result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
            profiles = re.findall(r"All User Profile\s*:\s*(.*)", result.stdout)

            wifi_data = {}
            for profile in profiles:
                profile = profile.strip()
                result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
                password_match = re.search(r"Key Content\s*:\s*(.*)", result.stdout)
                wifi_data[profile] = password_match.group(1) if password_match else "No Password Found"
            
            return wifi_data
        else:
            st.write(f"WiFi password retrieval is supported only on Windows, but you are on {system}.")  # Debug line
            return {"Error": f"WiFi password retrieval is supported only on Windows, but you are on {system}."}
    except Exception as e:
        return {"Error": str(e)}

# Function to get connected devices (Works on Windows, Linux/macOS alternative could be added)
def get_connected_devices():
    try:
        system = platform.system()
        if system == 'Windows':
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
            devices = re.findall(r"(\d+\.\d+\.\d+\.\d+)", result.stdout)
            return devices
        else:
            return ["Error: Device detection is supported only on Windows."]
    except Exception as e:
        return ["Error: " + str(e)]

# Function to get the local machine's IP address
def get_local_ip():
    try:
        system = platform.system()
        if system == 'Windows':
            result = subprocess.run(["ipconfig"], capture_output=True, text=True)
            match = re.search(r"IPv4 Address[.\s]+: (\d+\.\d+\.\d+\.\d+)", result.stdout)
            return match.group(1) if match else "Error"
        else:
            # For Linux/macOS, use 'hostname' to get the local IP
            result = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
            return result.stdout.strip() if result.returncode == 0 else "Error"
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("WiFi and Network Information Manager")

option = st.sidebar.radio("Select an option", ["Check WiFi Password", "Connected Devices", "Your Local IP"])

if option == "Check WiFi Password":
    st.write(f"Platform: {platform.system()}")  # Debug line
    if platform.system() == 'Windows':
        st.subheader("Saved WiFi Passwords")
        passwords = get_wifi_password()
        if "Error" in passwords:
            st.write(passwords["Error"])
        else:
            for wifi, pwd in passwords.items():
                st.write(f"**{wifi}**: {pwd}")
    else:
        st.write("WiFi password retrieval is supported only on Windows.")

elif option == "Connected Devices":
    st.subheader("Devices Connected to Your Network")
    devices = get_connected_devices()
    if "Error" in devices:
        st.write(devices[0])
    else:
        st.write("Connected Devices IPs:")
        for device in devices:
            st.write(device)

elif option == "Your Local IP":
    st.subheader("Your Local IP Address")
    local_ip = get_local_ip()
    st.write(local_ip)
