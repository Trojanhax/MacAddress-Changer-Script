import subprocess
import time
import random

# Network interface name (e.g., "eth0" or "wlan0")
interface_name = "eth0"

while True:
    try:
        # Generate a random MAC address
        new_mac = ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)])
        
        # Disable the network interface
        subprocess.run(["sudo", "ifconfig", interface_name, "down"])
        
        # Change the MAC address
        subprocess.run(["sudo", "ifconfig", interface_name, "hw", "ether", new_mac])
        
        # Enable the network interface
        subprocess.run(["sudo", "ifconfig", interface_name, "up"])
        
        print(f"Changed MAC address to {new_mac}")
        
        # Sleep for 5 seconds before changing again
        time.sleep(5)
    
    except KeyboardInterrupt:
        # Stop the script if Ctrl+C is pressed
        break
