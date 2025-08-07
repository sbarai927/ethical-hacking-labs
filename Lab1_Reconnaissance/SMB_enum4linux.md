## SMB Enumeration – enum4linux

---

### 🎯 Objective
Enumerate SMB shares and users.

---

### 🧪 Command
```bash
sudo enum4linux -a 10.6.6.23 | tee smb_full.txt
```

---

### 📌 Findings
- Users: arbiter, masterchief
- Share: public (anonymous RW)

---

### 📌 Take-Aways
Anonymous SMB shares present a serious risk for data theft and malware spread.
