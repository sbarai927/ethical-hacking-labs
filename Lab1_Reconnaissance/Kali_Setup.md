## Kali Linux Setup

---

### 🎯 Objective
Set up and configure the Kali Linux environment for Lab 1 tasks (1.3.6 & 1.3.7).

---

### 🛠 Steps
```bash
sudo apt update && sudo apt full-upgrade -y
sudo apt install nmap spiderfoot recon-ng wireshark scapy enum4linux \
                 set net-tools ettercap-text-only
```

1. Configure keyboard layout (e.g., **German** if required).
2. Confirm network configuration with:
   ```bash
   ip a
   ```
3. Verify tool availability:
   ```bash
   which nmap spiderfoot recon-ng
   ```

---

### 💡 Notes
* In UTM (Mac M2), boot via:
  ```
  fs0:\efi\kali\grubaa64.efi
  ```
* VM connected to **lab network** for scanning.

---

### 📌 Take-Aways
A reproducible Kali setup ensures tool compatibility and consistent results.
