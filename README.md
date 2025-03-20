🛠️ WiFi and Network Information Manager
A Streamlit web application that helps users retrieve saved WiFi passwords, check connected devices, and find their local IP address.

🔥 Features
✅ Check Saved WiFi Passwords – Retrieve stored WiFi passwords (Windows only).
✅ View Connected Devices – List devices currently connected to your network (Windows only).
✅ Find Your Local IP Address – Display your local machine’s IP address.
✅ User-Friendly Interface – Simple and interactive UI using Streamlit.

🛠️ Technologies Used
🔹 Python
🔹 Streamlit
🔹 Subprocess
🔹 Regex
🔹 Platform

📌 How to Run
1️⃣ Clone this repository:

bash
Copy
Edit
git clone https://github.com/YOUR-USERNAME/wifi-network-info.git
cd wifi-network-info
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
⚠️ Important Notes
WiFi password retrieval is Windows-only (uses netsh commands).
Connected devices detection works on Windows using arp -a.
Local IP address retrieval supports both Windows and Linux/macOS.
🚀 Future Enhancements
✅ Support for Linux/macOS WiFi password retrieval
✅ Advanced network scanning for connected devices
✅ UI improvements with better formatting