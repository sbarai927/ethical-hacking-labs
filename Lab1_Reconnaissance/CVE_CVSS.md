## Vulnerability Research – CVE & CVSS

---

### 🎯 Objective
Map identified service versions to known vulnerabilities and assess severity.

---

### 🧪 Process
1. Capture banner/version
2. Search CVE databases:
   * [NVD](https://nvd.nist.gov/)
   * [Vulners](https://vulners.com/)
3. Record CVE IDs and CVSS scores

---

### 📌 Example
| Service | Version | CVE          | CVSS  | Notes                   |
|---------|---------|--------------|-------|-------------------------|
| vsftpd  | 2.3.4   | CVE-2011-2523| 9.3   | Backdoored login        |
| Samba   | 3.0.20  | CVE-2017-7494| 8.1   | Remote code execution   |

---

### 📌 Take-Aways
CVE mapping quantifies risk; CVSS helps prioritise patches.
