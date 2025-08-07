#!/usr/bin/env python3
from scapy.all import *
import sys
if len(sys.argv) < 3:
    print("Usage: ./syn_probe.py <ip> <port>")
    sys.exit(1)
ip, port = sys.argv[1], int(sys.argv[2])
ans = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), timeout=2, verbose=0)
if ans and ans.haslayer(TCP) and ans[TCP].flags & 0x12:  # SYN+ACK
    print(f"[+] {ip}:{port} looks OPEN (SYN/ACK).")
else:
    print(f"[-] {ip}:{port} not responding with SYN/ACK.")
