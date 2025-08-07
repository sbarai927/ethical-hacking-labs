## Nmap Enumeration

---

### 🎯 Objective
Perform active scanning to identify open ports, services, and potential vulnerabilities.

---

### 🧪 TCP Scan
```bash
sudo nmap -sT -T4 10.6.6.23 -oN scans/top1k_tcp.txt
```

---

### 🧪 Service & OS Detection
```bash
sudo nmap -sV -sC -O 10.6.6.23 -oN scans/service_os.txt
```
* FTP: vsftpd 2.3.4 (CVE-2011-2523)
* SMB: Samba 3.0.20 (EternalBlue vulnerable)

---

### 🧪 SMB NSE Scripts
```bash
sudo nmap --script smb-enum-shares,smb-enum-users -p139,445 10.6.6.23
```

---

### 📌 Take-Aways
Nmap with NSE scripts can uncover detailed service information and possible exploit paths.
