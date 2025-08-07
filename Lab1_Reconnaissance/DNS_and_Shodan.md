## DNS Lookups & Shodan

---

### 🎯 Objective
Use DNS tools and Shodan to gather passive intelligence on targets.

---

### 🧪 DNS Enumeration
```bash
nslookup vpn.example.com 8.8.8.8
dig AXFR @ns1.example.com example.com
dig -x 198.51.100.42 +short
```

---

### 🧪 WHOIS Query
```bash
whois example.com | egrep -i 'Registrar|Expiry'
```

---

### 🧪 Shodan Search
```bash
shodan search --fields ip_str,port,org "org:\"Example Corp\" http.title:\"Welcome\""
```

---

### 📌 Take-Aways
Combining DNS records with Shodan data can reveal hidden or vulnerable services.
