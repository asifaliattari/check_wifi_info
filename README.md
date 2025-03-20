# check_wifi_info
WiFi Network Manager is a Streamlit-based app designed to help users manage and check the details of their WiFi networks and devices connected to their router. 
WiFi Network Manager is a Streamlit-based app designed to help users manage and check the details of their WiFi networks and devices connected to their router. The app allows users to:

# View saved WiFi passwords.
List devices connected to the router.
Display the local IP and MAC addresses of connected devices.
Show the signal strength of the connected WiFi network.
Save WiFi passwords to a .txt file.

# Features:
View Saved WiFi Passwords: Displays saved WiFi passwords for all networks stored on your device.
List Connected Devices: Shows the IP and MAC addresses of devices connected to your router.
WiFi Signal Strength: Check the current signal strength of the connected WiFi network (in percentage).
Save WiFi Passwords: Save your WiFi passwords into a .txt file for easy reference.
Local IP Address: Displays the local IP address of your computer.

# Requirements:
Python 3.7+
Streamlit
speedtest-cli (optional if you plan to use the internet speed feature, otherwise not needed)

To install the required packages:

bash
Copy
pip install streamlit
How to Use:
Clone the repository:

bash
Copy
git clone https://github.com/yourusername/wifi-network-manager.git
Navigate into the app directory:

bash
Copy
cd wifi-network-manager
Run the Streamlit app:

bash
Copy
streamlit run app.py
