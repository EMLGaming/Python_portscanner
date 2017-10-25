#!/usr/bin/env python
# Created by EMLGaming

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    if iteration == total:
        print()
from time import sleep
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
print("\n[*] Scanning started at %s" % (time.strftime("%H:%M:%S")))
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
items = list(range(bePORT, endPORT))
l = len(items)
from threading import Thread
printProgressBar(0, l, prefix = 'Scanning:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    t = Thread(target=scan, args=(i,))
    threads.append(t)
    t.start()
    sleep(0.0017)
    printProgressBar(i + 1, l, prefix = 'Scanning:', suffix = 'Complete', length = 50)
[x.join() for x in threads]
hostip = socket.gethostbyname(host)
stop_time = datetime.now()
timeduration = stop_time - start_time
print("[*] Scanning Finished at %s " % (time.strftime("%H:%M:%S")))
print("[*] Scanning duration: %s " % (timeduration))
print()
print("#"*75)
print("[*] Host: %s IP: %s" % (host, hostip))
print('[*] Open ports: %s' % (counting_open))
print("#"*75)
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
