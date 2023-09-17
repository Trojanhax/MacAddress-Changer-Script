import subprocess
import time
import random

# Network interface name (e.g., "Ethernet" or "Wi-Fi")
interface_name = "Wi-Fi"

while True:
    try:
        # Generate a random MAC address (for demonstration purposes)
        new_mac = "02"
        for _ in range(5):
            new_mac += f":{random.randint(0, 255):02X}"
        
        # Change the MAC address using netsh
        subprocess.run(["netsh", "interface", "set", "interface", interface_name, "admin=disable"])
        subprocess.run(["netsh", "interface", "set", "interface", interface_name, "newmac=" + new_mac])
        subprocess.run(["netsh", "interface", "set", "interface", interface_name, "admin=enable"])
        
        print(f"Changed MAC address to {new_mac}")
        
        # Sleep for 5 seconds before changing again
        time.sleep(5)
    
    except KeyboardInterrupt:
        # Stop the script if Ctrl+C is pressed
        break
