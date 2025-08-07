## Lab 1 – Reconnaissance & Information Gathering

---

### 📌 Overview
Lab 1 focuses on **passive and active reconnaissance** on a target network using a customised Kali Linux VM.  
The tasks cover OSINT, DNS analysis, active scanning, packet crafting, vulnerability research, and social engineering.

---

### 📂 Topics Covered

| Topic                                    | Notes File                       |
|------------------------------------------|-----------------------------------|
| Kali base setup                          | `Kali_Setup.md`                  |
| OSINT tools                              | `OSINT_Tools.md`                 |
| DNS lookups & Shodan                     | `DNS_and_Shodan.md`              |
| Network scanning (Nmap)                  | `Nmap_Enumeration.md`            |
| Packet crafting & analysis               | `Scapy_Wireshark.md`             |
| CVE & CVSS vulnerability research        | `CVE_CVSS.md`                    |
| Social Engineering Toolkit               | `SET_SocialEngineering.md`       |
| SMB enumeration                          | `SMB_enum4linux.md`              |
| MITM with Ettercap                       | `Ettercap_MITM.md`               |

---

### 🧪 Lab Environment
* **Platform:** Kali Linux (custom university build)
* **Tools:** Nmap, SpiderFoot, Recon-ng, Scapy, Wireshark, enum4linux, SET, Ettercap, Shodan CLI
* **Network:** NAT + Host-only (10.x.x.x lab subnet)

---

### 🎯 Objectives
1. Use OSINT to gather information without touching the target.
2. Perform DNS lookups, WHOIS queries, and Shodan searches.
3. Actively scan hosts to enumerate services and vulnerabilities.
4. Capture and analyze packets.
5. Perform SMB enumeration and simulate MITM.

---

### 📂 Artifacts
```
Screenshots/   ← screenshots of scans, OSINT results, packet captures
Scripts/       ← automation scripts, scan outputs, pcap files
```

---

### ⚠ Ethical Notice
All activities conducted in a controlled lab environment on authorised targets.
