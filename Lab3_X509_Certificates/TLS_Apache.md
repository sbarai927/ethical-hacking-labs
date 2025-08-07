## TLS Configuration with Apache2

---

### 🎯 Objective
Configure **Apache2** to serve HTTPS using the server certificate issued by your local CA.

---

### 🛠 Prerequisites
* Completed `CA_Setup.md`
* Generated:
  - `serverkeyYYY.pem` (server private key)
  - `servercertYYY.pem` (server certificate signed by CA)
  - `cacert.pem` (root CA certificate)

---

### ### 1. Verify Apache HTTP Service
Open:
```
http://localhost
```
You should see Apache's default page (HTTP).

---

### ### 2. Copy Certificates & Keys to System Paths

#### 2.1 Copy server private key
```bash
sudo cp private/serverkeyYYY.pem /etc/ssl/private/
sudo chown root:root /etc/ssl/private/serverkeyYYY.pem
sudo chmod 600 /etc/ssl/private/serverkeyYYY.pem
```
💡 Correct permissions prevent unauthorized access to private keys.

#### 2.2 Copy certificates
```bash
sudo cp certs/servercertYYY.pem /etc/ssl/certs/
sudo cp certs/cacert.pem /etc/ssl/certs/
```

---

### ### 3. Create Apache SSL Virtual Host
Duplicate the default SSL configuration:
```bash
sudo cp /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/YYY-ssl.conf
```
Edit `YYY-ssl.conf`:
```
SSLCertificateFile      /etc/ssl/certs/servercertYYY.pem
SSLCertificateKeyFile   /etc/ssl/private/serverkeyYYY.pem
SSLCertificateChainFile /etc/ssl/certs/cacert.pem
```

---

### ### 4. Enable SSL/TLS in Apache
```bash
sudo a2enmod ssl
sudo a2ensite YYY-ssl
sudo apache2ctl configtest
sudo systemctl restart apache2
```

---

### ### 5. Test HTTPS in Firefox
1. Import `cacert.pem` into Firefox:
   - `about:preferences` → Privacy & Security → Certificates → View Certificates → Import
   - Trust this CA to identify websites.
2. Visit:
   ```
   https://localhost
   ```
3. Click the padlock to inspect the certificate — it should show as **verified**.

---

### ### 6. Optional: Redirect HTTP to HTTPS
Add to your HTTP site config:
```
<VirtualHost *:80>
    ServerName localhost
    Redirect / https://localhost/
</VirtualHost>
```

---

### 📌 Take-Aways
- Correct certificate/key file placement and permissions are crucial for security.
- Importing the root CA into a browser removes untrusted warnings for lab-issued certs.
