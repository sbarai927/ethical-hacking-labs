## Lab 2 – Web Exploitation & Password Attacks

---

### 📌 Overview
Lab 2 focuses on **identifying and exploiting vulnerabilities** in web applications,  
and performing both **offline** and **online** password cracking.

---

### 📂 Topics Covered

| Topic                                 | Notes File                        |
|---------------------------------------|------------------------------------|
| Web vulnerability scanning            | `Web_Vuln_Scanning.md`            |
| SQL Injection exploitation (DVWA)     | `DVWA_SQL_Injection.md`           |
| Cross-Site Scripting                  | `DVWA_XSS.md`                     |
| Cross-Site Request Forgery            | `DVWA_CSRF.md`                    |
| Offline password cracking             | `Password_Cracking_Offline.md`    |
| Online brute-force attacks (SSH etc.) | `Password_Attacks_Online.md`      |

---

### 🧪 Lab Environment
* **Platform:** Kali Linux (custom university build)
* **Targets:**
  - DVWA (Damn Vulnerable Web App) – local instance in Kali VM
  - Demo web servers for Nikto / OpenVAS scans
  - SSH service in lab network for password brute-forcing
* **Tools:** Nikto, OpenVAS/GVM, DVWA, Hydra, Medusa, Ncrack, Hashcat, John the Ripper, RainbowCrack

---

### 🎯 Objectives
1. Identify vulnerabilities in web servers & web applications.
2. Exploit SQL Injection, XSS, and CSRF flaws in DVWA.
3. Crack password hashes with offline tools.
4. Perform online brute-force attacks against SSH.

---

### 📂 Artifacts
```
Screenshots/   ← screenshots of scans, DVWA exploits, cracked passwords
Scripts/       ← automation scripts, tool output logs
```

---

### ⚠ Ethical Notice
All tests performed on intentionally vulnerable targets within a closed lab environment.
