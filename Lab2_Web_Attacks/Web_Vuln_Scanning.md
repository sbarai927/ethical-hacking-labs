## Web Vulnerability Scanning

---

### 🎯 Objective
Use **Nikto** and **GVM (Greenbone Vulnerability Manager)** to identify vulnerabilities, misconfigurations, and outdated software in web servers.

---

### 🛠 Nikto – Basic Scan
```bash
nikto -h http://<target-ip> -output nikto_results.txt
```

**Example (Lab):**
```bash
nikto -h http://10.6.6.23 -output scans/nikto_lab2.txt
```

**Lab Observations:**
- Apache version banners exposed
- Outdated modules linked to known CVEs:
  - CVE-1999-0678: Apache default configuration exposes `/usr/doc`
  - CVE-2003-1418: Information disclosure via MIME boundary

**Mitigations:**
- Apply vendor patches/upgrades
- Disable unnecessary HTTP headers
- Restrict file/directory access

---

### 📂 Multiple Targets Scan
```bash
nikto -h targets.txt -output scans/nikto_multi.txt
```
`targets.txt` example:
```
http://10.6.6.23
http://10.6.6.24
```

---

### 🛠 GVM/OpenVAS – Vulnerability Scanning

#### Steps
1. Run `gvm-start`
2. Access web UI: `https://127.0.0.1:9392/`
3. Create a **Target** → set host IP (e.g., `10.6.6.23`)
4. Create a **Task** linked to that target
5. Start the scan

**Key Lab Findings:**
- TWiki vulnerable (pre-4.2.4) → upgrade required
- rexec service enabled → disable & replace with SSH
- Outdated software with multiple CVEs

**Example Exploitation Path:**
- Escalate to root
- Copy `/etc/passwd` and `/etc/shadow`
- Use `unshadow` and `john` to crack

---

### 📌 Take-Aways
- Nikto is fast for surface-level checks
- GVM/OpenVAS gives deeper analysis with CVE links
- Manual verification is essential to avoid false positives
- Prioritise patches by CVSS score
