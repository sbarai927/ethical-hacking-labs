## Certification Authority (CA) Setup

---

### 🎯 Objective
Set up a local **Certification Authority (CA)**, generate a server certificate, and sign it using your CA.  
This will be used later to enable TLS on both an OpenSSL test server and Apache2.

---

### 🛠 Lab Environment
* **OS:** Debian 11 (VM or physical)
* **Packages:** `openssl`, `apache2`
* **Browser:** Firefox (for certificate import and testing)

Install prerequisites:
```bash
sudo apt-get update
sudo apt-get install openssl apache2
```

---

### ### 1. Create CA Directory Structure
```bash
mkdir lab3
cd lab3
mkdir certs newcerts private crl
touch index.txt
echo 01 > serial
echo 01 > crlnumber
```

---

### ### 2. Generate Root CA Private Key
```bash
openssl genrsa -out private/cakey.pem 2048
```
💡 Keep `cakey.pem` **secure** — this is your CA's private key.

---

### ### 3. Create a Self-Signed Root Certificate
```bash
openssl req -new -x509 -days 1000 \
  -key private/cakey.pem \
  -out certs/cacert.pem
```
**Example fields:**
- **Country Name (C):** DE  
- **State or Province Name (ST):** NRW  
- **Locality (L):** Koeln  
- **Organization (O):** TH Koeln  
- **Organizational Unit (OU):** ITS  
- **Common Name (CN):** Lab Trust Center `<Your Name>`  
- **Email Address:** *(leave empty)*

---

### ### 4. View the Root Certificate
```bash
openssl x509 -in certs/cacert.pem -text -noout
```
- Confirm **Issuer** and **Subject** match (self-signed).
- Identify the public key.

---

### ### 5. Generate a Server Key Pair (Elliptic Curve)
```bash
openssl ecparam -genkey -name prime256v1 -out private/serverkeyYYY.pem
```
Replace `YYY` with your 8-digit matriculation number.

---

### ### 6. Create a Certificate Signing Request (CSR)
```bash
openssl req -new \
  -out certs/serverreqYYY.pem \
  -key private/serverkeyYYY.pem
```
- Use the same info as root cert **except**:
  - **Common Name (CN):** `localhost`
  - Leave email blank.

---

### ### 7. Inspect the CSR
```bash
openssl req -in certs/serverreqYYY.pem -text -noout
```

---

### ### 8. Sign the Server Certificate with Your CA
1. Copy `openssl.cnf` locally:
   ```bash
   cp /etc/ssl/openssl.cnf .
   ```
2. Edit and change:
   ```
   HOME = .
   ```
3. Issue the certificate:
   ```bash
   openssl ca -notext \
     -in certs/serverreqYYY.pem \
     -out certs/servercertYYY.pem \
     -keyfile private/cakey.pem \
     -CAfile certs/cacert.pem \
     -config openssl.cnf
   ```

---

### ### 9. Verify the Server Certificate
```bash
openssl x509 -in certs/servercertYYY.pem -text -noout
```
Compare with CSR — note any differences in signature algorithms.

---

### 📌 Take-Aways
- A local CA can issue trusted certificates for lab and testing environments.
- Protect the root CA private key to maintain trust.
