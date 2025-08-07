## Offline Password Cracking

---

### 🎯 Objective
Recover plaintext passwords from hashes using Hashcat, John the Ripper, and RainbowCrack.

---

### 🧪 Hashcat – Dictionary Attack
```bash
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```
- `-m 0` → MD5
- `-a 0` → dictionary mode

---

### 🧪 John the Ripper
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```
Switches to incremental brute-force if dictionary fails.

---

### 🧪 Rainbow Table Attack

#### Create Table
```bash
sudo rtgen md5 loweralpha 1 3 0 1000 1000 0
sudo rtsort .
```

#### Crack Hash
```bash
rcrack . -h 06d80eb0c50b49a509b49f2424e8c805
```
Result: `dog`

---

### 🛡 Mitigation
- Use salted, slow hashes (bcrypt, scrypt, Argon2)
- Enforce strong password policies

---

### 📌 Take-Aways
- Weak hashes + common passwords = instant crack
