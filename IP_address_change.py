import psutil
import subprocess

# Get a list of all network interfaces and their addresses
net_if_list = psutil.net_if_addrs()

# Print a list of available interfaces
print("Available network interfaces:")
for i, interface_name in enumerate(net_if_list.keys()):
    print(f"{i}: {interface_name}")

# Prompt the user to select an interface
interface_idx = int(input("Select an interface: "))

# Get the selected interface name
interface_name = list(net_if_list.keys())[interface_idx]

# Get the current IP address of the selected interface
ip_address = None
for address in net_if_list[interface_name]:
    if address.family == 2:  # Check if the address is an IPv4 address
        ip_address = address.address

print(f"Selected interface: {interface_name} ({ip_address})")

# Prompt the user to enter a new IP address for the interface
new_ip_address = input("Enter a new IP address: ")

# Use the netsh command to set the new IP address
subprocess.run(f"netsh interface ipv4 set address name={interface_name} static {new_ip_address}", shell=True)

print(f"IP address for interface {interface_name} set to {new_ip_address}")

### This script uses the psutil library to retrieve information about network interfaces and their addresses. It then prints a list of available interfaces and prompts the user to select one. 
### It gets the current IP address of the selected interface and prompts the user to enter a new IP address. Finally, it uses the netsh command to set the new IP address for the selected interface.
### Note that this script assumes that you have psutil installed on your system. If you don't have it installed, you can install it using pip install psutil.
