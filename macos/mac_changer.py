import subprocess
import time
import random

# Network interface name (e.g., "en0" for Ethernet or "en1" for Wi-Fi)
interface_name = "en0"

while True:
    try:
        # Generate a random MAC address
        new_mac = "02"
        for _ in range(5):
            new_mac += f":{random.randint(0, 255):02X}"
        
        # Disable the network interface
        subprocess.run(["sudo", "ifconfig", interface_name, "down"])
        
        # Change the MAC address
        subprocess.run(["sudo", "ifconfig", interface_name, "lladdr", new_mac])
        
        # Enable the network interface
        subprocess.run(["sudo", "ifconfig", interface_name, "up"])
        
        print(f"Changed MAC address to {new_mac}")
        
        # Sleep for 5 seconds before changing again
        time.sleep(5)
    
    except KeyboardInterrupt:
        # Stop the script if Ctrl+C is pressed
        break
