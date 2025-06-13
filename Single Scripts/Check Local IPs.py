# Import the necessary modules
import socket
import fcntl
import struct

# Get the list of network interfaces
ifaces = socket.if_nameindex()

# Loop through the interfaces
for iface in ifaces:
  # Get the interface name and index
  name = iface[0]
  idx = iface[1]

  # Use the index to get the IP address
  ip = socket.inet_ntoa(fcntl.ioctl(
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM),
    0x8915,  # SIOCGIFADDR
    struct.pack('256s', bytes(idx, 'utf-8'))
  )[20:24])

  # Print the interface name and IP address
  print(f"{name}: {ip}")
