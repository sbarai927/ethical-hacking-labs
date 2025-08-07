## OSINT Tools

---

### 🎯 Objective
Gather open-source intelligence on targets using online frameworks and automated tools.

---

### 🧪 Tools Used

#### 1️⃣ OSINT Framework (Web)
* Visual tree of OSINT resources
* Helps pivot from one piece of info to others

#### 2️⃣ SpiderFoot
```bash
sudo spiderfoot -l 127.0.0.1:5001
```
Access at: `http://127.0.0.1:5001`  
Finds emails, domains, IP ranges, breaches, etc.

#### 3️⃣ Recon-ng
```bash
recon-ng
> marketplace install all
> workspaces create lab1
> modules load recon/domains-hosts/bing_domain_web
> set SOURCE example.com
> run
```

---

### 📌 Take-Aways
OSINT tools can map a target’s footprint without touching their infrastructure.
