#!/usr/bin/env python
# Created by EMLGaming
#make a loading bar and a nice welcome
from threading import Thread
import socket
import sys, time
from datetime import datetime
host = input('[?] Enter targets host address: ')
print("[!] Default portrange is 1-5000")
try:
        bPORT = input('[?] Start scanning from port: ')
        bePORT = int(bPORT)
except ValueError:
    if len(bPORT)==0:
        bePORT = 1
try:
        ePORT = input('[?] To port: ')
        endPORT = int(ePORT)
except ValueError:
    if len(ePORT)==0:
        endPORT = 5000
print("[*] Scanning started at %s" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()
counting_open = []
counting_close = []
threads = []
def scan(port):
	s = socket.socket()
	result = s.connect_ex((host,port))
	if result == 0:
		counting_open.append(port)
		s.close()
	else:
		counting_close.append(port)
		s.close()
for i in range(int(bePORT), int(endPORT)):
	t = Thread(target=scan, args=(i,))
	threads.append(t)
	t.start()
[x.join() for x in threads]
hostip = socket.gethostbyname(host)
print()
print("-"*60)
print("[*] Host: %s IP: %s" % (host, hostip))
print('[*] Open ports: %s' % (counting_open))
print("-"*60)
stop_time = datetime.now()
timeduration = stop_time - start_time
print("\n[*] Scanning Finished at %s " % (time.strftime("%H:%M:%S")))
print("[*] Scanning duration: %s " % (timeduration))
import socket
pubip = (socket.getaddrinfo("ident.me", 80, proto=socket.IPPROTO_TCP))
cut1 = (str(pubip))
cut2 = cut1.split(',')
cut3 = cut2[4].split("(")
cut4 = cut3[1].replace("'", "")
from socket import *
ip = gethostbyname(gethostname())
print("\nExtra info:\n[*] Your IP: %s" % (cut4))
print("[*] Your local IP: %s" % (ip))
print("\n[!] Thanks for using my portscanner, EMLGaming")
