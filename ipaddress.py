import socket
import platform
import os
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("----------Target Device Information-------------------")
print("Target Hostname: " + hostname)
print("Target IP Address is: " + IPAddr)
print("Name of the OS system: " + platform.system())
print("Version of the operating system: " + platform.release())
print("Name of the operating system: " + os.name)
print("-------------------------------------------------------")
input("Press enter to exit")

