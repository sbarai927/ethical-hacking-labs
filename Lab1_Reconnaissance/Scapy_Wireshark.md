## Packet Crafting & Analysis

---

### 🎯 Objective
Use Scapy to craft packets and Wireshark to capture/analyze traffic.

---

### 🧪 Craft ICMP Packet
```python
from scapy.all import *
pkt = IP(src="10.6.6.99", dst="10.6.6.23")/ICMP()
send(pkt)
```

---

### 🧪 TCP SYN Probe
```python
sr1(IP(dst="10.6.6.23")/TCP(dport=445,flags="S"))
```

---

### 🧪 Sniff FTP Login
```python
pkts = sniff(filter="tcp and port 21", count=10)
wrpcap("ftp_login.pcap", pkts)
```

---

### 📌 Take-Aways
Scapy allows packet-level testing; Wireshark provides deep packet inspection.
