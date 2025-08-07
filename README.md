# Ethical Hacking Labs

A collection of practical lab exercises completed during an IT Security course, covering reconnaissance, web application exploitation, password attacks, and TLS/PKI configuration.

## Table of Contents

- [Objective](#objective)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Repository Layout](#repository-layout)
- [Quick Start](#quick-start)
- [Lab Summaries](#lab-summaries)
- [Scripts](#scripts)
- [Reproducing Key Results](#reproducing-key-results)
- [Project Road-map](#project-road-map)
- [Disclaimer](#disclaimer)

---

## Objective

This repository documents a series of **Ethical Hacking labs in the framework of Cisco certification** completed as part of IT Security course (WS 2024), lectured by Prof. Heiko Knopse, Technische Hochschule Köln.  
Each lab folder contains:

- Step-by-step **Markdown guides** for individual tasks
- **Helper scripts** for automation
- **Screenshots & documentation** for reproducibility

The labs aim to:

1. Develop hands-on skills in reconnaissance and enumeration
2. Understand and exploit common web application vulnerabilities
3. Perform both online and offline password attacks
4. Explore TLS/PKI setup with X.509 certificates

---
## Prerequisites

- **OS:** Kali Linux (preferred) or any Linux distribution with required tools
- **Python:** 3.8+
- **Virtual Environment:** Recommended (`venv` or `conda`)
- **Networking:** Access to lab VMs and vulnerable targets (e.g., DVWA, Juice Shop)
- **Python Libraries:** Listed in [`requirements.txt`](./requirements.txt)
- **Tools:**  
  - Nmap, Nikto, Hydra, Medusa, John the Ripper, Hashcat
  - OpenSSL, Apache2 (for TLS labs)
  - Scapy, Wireshark
  - Social Engineering Toolkit (SET)

---
## Installation

Clone the repository:
```bash
git clone https://github.com/<your-username>/ethical-hacking-labs.git
cd ethical-hacking-labs
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Install pentesting tools:
```bash
sudo apt update
sudo apt install nmap nikto hydra medusa john hashcat openssl apache2
```

---

## Repository Layout

```
ethical-hacking-labs/
│
├── docs/                         # Lab handouts & instructions
│   ├── Lab 1.pdf
│   ├── Lab 2.pdf
│   └── Lab 3.pdf
│
├── Lab1_Reconnaissance/           # Lab 1 – Recon & Information Gathering
│   ├── README.md
│   ├── Kali_Setup.md
│   ├── OSINT_Tools.md
│   ├── DNS_and_Shodan.md
│   ├── Nmap_Enumeration.md
│   ├── Scapy_Wireshark.md
│   ├── CVE_CVSS.md
│   ├── SET_SocialEngineering.md
│   ├── SMB_enum4linux.md
│   ├── Ettercap_MITM.md
│   └── scripts/
│       ├── recon_quickshot.sh
│       └── syn_probe.py
│
├── Lab2_Web_Attacks/              # Lab 2 – Web Vulns & Password Attacks
│   ├── README.md
│   ├── Web_Vuln_Scanning.md
│   ├── DVWA_SQL_Injection.md
│   ├── DVWA_XSS.md
│   ├── DVWA_CSRF.md
│   ├── Password_Cracking_Offline.md
│   ├── Password_Attacks_Online.md
│   └── lab2_helper.py
│
├── Lab3_JuiceShop/                 # Lab 3 – OWASP Juice Shop Exploitation
│   ├── README.md
│   ├── JuiceShop_Attacks.md
│   └── lab3_helper.py
│
├── Lab3_X509_Certificates/         # Optional – TLS & PKI Lab
│   ├── README.md
│   ├── CA_Setup.md
│   └── TLS_Apache.md
│
├── requirements.txt                # Python dependencies for all scripts
└── README.md                       # This file
```

---

## Quick Start

### Lab 1 – Reconnaissance
```bash
cd Lab1_Reconnaissance/scripts
python3 syn_probe.py
```

### Lab 2 – Web Attacks
```bash
cd Lab2_Web_Attacks
python3 lab2_helper.py nikto targets.txt results/
```

### Lab 3 – Juice Shop
```bash
cd Lab3_JuiceShop
python3 lab3_helper.py http://localhost:3000 --recon --sqli
```

---

## Lab Summaries

### **Lab 1 – Reconnaissance & Information Gathering**
- OSINT tools, DNS enumeration, Shodan
- Nmap scanning, Scapy packet crafting, Wireshark analysis
- Vulnerability scoring with CVE/CVSS
- SMB enumeration, SET, Ettercap MITM

### **Lab 2 – Web Vulnerabilities & Password Attacks**
- Nikto & OpenVAS scans
- DVWA: SQL Injection, XSS, CSRF
- Offline password cracking (John, Hashcat, Rainbow Tables)
- Online brute-force (Hydra, Medusa, Ncrack)

### **Lab 3 – OWASP Juice Shop**
- Recon of hidden endpoints
- Exploiting scoreboard, coupon, privacy leaks, SQLi, XSS
- JWT analysis, IDOR, password cracking

### **Lab 3 (Optional) – TLS & X.509**
- Setting up a local Certificate Authority
- Signing server certificates
- Configuring Apache for HTTPS

---

## Scripts

- **Lab 1:**
  - `recon_quickshot.sh` – Fast network recon
  - `syn_probe.py` – SYN scan with Scapy
- **Lab 2:**
  - `lab2_helper.py` – Automated scans & password attack helper
- **Lab 3:**
  - `lab3_helper.py` – Juice Shop recon + SQLi helper

---

## Reproducing Key Results
To reproduce all lab results from scratch:
1. Follow the setup instructions in each lab’s `README.md`.
2. Run the helper scripts to automate scanning/exploitation.
3. Save all output in the `results/` subdirectories for reporting.
4. Compare with provided screenshots attached in the pdf per lab to confirm success.

---
## Project Road-map
- [x] Document all lab steps in markdown
- [x] Add helper scripts for Lab 1, Lab 2, Lab 3
- [ ] Add Docker-based isolated test environment
- [ ] Automate report generation from results

---

## Disclaimer
All activities in this repository are performed in **controlled lab environments** on intentionally vulnerable systems.  
Do **not** attempt these techniques on any network or system you do not own or have explicit permission to test.
