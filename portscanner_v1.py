#!/bin/python3

import socket
from datetime import datetime as dt

open_ports = []

#Ask for remote server
host_input = input("\nEnter a host (IPv4) to scan or type 0 for localhost:  ")
if host_input == "0":
	host_input = "127.0.0.1";

#Ask for port range
port_start = int(input("\nEnter port range START:  "))

port_end = int(input("Enter port range END:  "))

#Take time stamp
time_start = dt.now()

print("\nPlease wait... \nScanning host: " + host_input + " on port range: " + str(port_start) + " - " + str(port_end) +"\n")

#Scan ports in range
for port in range(port_start,(port_end+1)):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex((host_input,port))
	if result == 0:
		print("Port: " + str(port) + "\tOPEN")
		open_ports.append(port)		#Add open ports to list
	else:
		print("Port: " + str(port) + "\t\t\t\t\tCLOSED")

#Calculate scan duration
time_end = dt.now()
time_passed = time_end - time_start

print("\nThe scan was completed in: ", time_passed)

#Return statement if no ports open
if open_ports == []:
	open_ports = "<no open ports>"

#Return list of all open ports
print("\nThese ports are open: ", open_ports)
