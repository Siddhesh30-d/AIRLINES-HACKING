from scapy.all import ARP, Ether, srp
from datetime import datetime

def scan_network(ip_range, log_to_file=False):
    print(f"\n[REAL SCAN] Scanning network: {ip_range}")

    # Create ARP request
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send and receive packets
    result = srp(packet, timeout=3, verbose=0)[0]

    # Extract devices
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    if not devices:
        print("[!] No devices found. Network might be segmented properly.")
    else:
        print("\n[+] Devices detected on the same network:")
        print(" IP Address\t\tMAC Address")
        print(" ---------------------------------------------")
        for device in devices:
            print(f" {device['ip']}\t\t{device['mac']}")

        # Save to file if needed
        if log_to_file:
            filename = f"network_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as file:
                file.write("IP Address\tMAC Address\n")
                for device in devices:
                    file.write(f"{device['ip']}\t{device['mac']}\n")
            print(f"\n[+] Log saved to {filename}")

def demo_example_output():
    print("\n[DEMO EXAMPLE] Scanning network: 192.168.0.1/24")
    print("\n[+] Devices detected on the same network:")
    print(" IP Address\t\tMAC Address")
    print(" ---------------------------------------------")
    print(" 192.168.0.1\t\tAA:BB:CC:DD:EE:01  (Wi-Fi Router)")
    print(" 192.168.0.23\t\t12:34:56:78:90:AB  (Passenger's Laptop)")
    print(" 192.168.0.42\t\tAB:CD:EF:12:34:56  (Crew Tablet)")
    print(" 192.168.0.88\t\t11:22:33:44:55:66  (Another Passenger's Phone)")
    print("\n[+] Log saved to network_scan_demo.txt")
    with open("network_scan_demo.txt", "w") as file:
        file.write("IP Address\t\tMAC Address\n")
        file.write("192.168.0.1\t\tAA:BB:CC:DD:EE:01\n")
        file.write("192.168.0.23\t\t12:34:56:78:90:AB\n")
        file.write("192.168.0.42\t\tAB:CD:EF:12:34:56\n")
        file.write("192.168.0.88\t\t11:22:33:44:55:66\n")
# Run both modes automatically
if __name__ == "__main__":
    demo_example_output()                   # Run the demo first
    scan_network("192.168.0.1/24", True)    # Run real scan with default range