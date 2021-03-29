#!/usr/bin/env python
# -- coding: utf-8 --

import ipaddress
import socket  # for making a successful connection to the host
import sys  # for getting arguments input by the user.
from datetime import datetime


def scan_ports(remoteServerIP):
    for port in range(1, 1024):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("\tPort {}: Open".format(port))
            sock.close()
        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()
        except socket.gaierror:
            print('{} Hostname could not be resolved. Exiting'.format(remoteServerIP))
        except socket.error:
            print("{} Couldn't connect to server".format(remoteServerIP))


# validate arguments
if len(sys.argv) < 2:
    print('Not enoght arguments')
    sys.exit(1)
# check what time the scan started
t1 = datetime.now()
if '0/' in sys.argv[1]:
    # handle CIDR
    for ip in [str(ip) for ip in ipaddress.IPv4Network(sys.argv[1])]:
        print('Scanning: {}'.format(ip))
        scan_ports(ip)
else:
    # handle ip/host
    # pass
    remoteServerIP = socket.gethostbyname(sys.argv[1])
    print('Scanning: {}'.format(remoteServerIP))
    scan_ports(remoteServerIP)

t2 = datetime.now()
# calculates the difference of time, to see how long it took to run the script
total = t2 - t1
# printing the information to screen
print('scanning completed in: ', total)
