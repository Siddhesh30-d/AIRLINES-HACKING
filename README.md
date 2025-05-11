# AIRLINES-HACKING
A Python-based tool that scans local Wi-Fi networks to detect connected devices and test network segmentation, especially in in-flight environments. It uses ARP scanning to identify IP and MAC addresses, helping evaluate security and isolation between users. Includes real scan mode, demo simulation, and log-saving for analysis.
Follow these steps to run the Python-based Wi-Fi scanner and segmentation testing tool:

✅ 1. Install Python (if not installed)
Download from https://www.python.org/downloads/

During installation, check the box: "Add Python to PATH"

✅ 2. Install Required Library
Install the scapy library, which the tool uses to scan the network:
pip install scapy

✅ 3. Download or Clone the Project

git clone https://github.com/yourusername/wifi-network-scanner.git
cd wifi-network-scanner/tool/source_code
Or just download the .zip file and extract it.

✅ 4. Run the Program
🔹 On Windows (run Command Prompt as Administrator):

python wifi_segmentation_scan.py
🔹 On Linux/Mac (use sudo for permission):
sudo python3 wifi_segmentation_scan.py

✅ 5. Understand the Output
The script runs in two parts:

Demo Mode – Shows example devices connected to a simulated network.

Real Scan Mode – Scans your actual network and prints a list of connected devices with their IP and MAC addresses.

📁 6. Check Saved Results
The tool saves scan logs as .txt files in the same folder.

Example:

network_scan_20250511_152030.txt
network_scan_demo.txt


