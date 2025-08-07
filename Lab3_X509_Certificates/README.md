# Lab 3 – Web Application & TLS Security

---
## 📌 Overview
Lab 3 consists of **two independent tracks**:

1. **Option A – OWASP Juice Shop**  
   Perform reconnaissance, exploitation, and vulnerability analysis on a deliberately insecure web application.
   
2. **Optional Lab – X.509 Certificates & TLS**  
   Set up your own Certificate Authority, issue server certificates, and configure TLS on both OpenSSL and Apache2.

## ## Optional Lab: X.509 Certificates & TLS

### ### 1. Setup Certification Authority (CA)
1. Create directories and index files:
   ```bash
   mkdir lab3 certs newcerts private crl
   touch index.txt
   echo 01 > serial
   echo 01 > crlnumber
   ```
2. Generate CA private key:
   ```bash
   openssl genrsa -out private/cakey.pem 2048
   ```
3. Create self-signed root certificate:
   ```bash
   openssl req -new -x509 -days 1000 -key private/cakey.pem -out certs/cacert.pem
   ```

---

### ### 2. Issue a Server Certificate
1. Generate EC private key:
   ```bash
   openssl ecparam -genkey -name prime256v1 -out private/serverkeyYYY.pem
   ```
2. Create CSR for `localhost`:
   ```bash
   openssl req -new -out certs/serverreqYYY.pem -key private/serverkeyYYY.pem
   ```
3. Sign CSR with CA:
   ```bash
   openssl ca -in certs/serverreqYYY.pem -out certs/servercertYYY.pem \
     -keyfile private/cakey.pem -CAfile certs/cacert.pem -config openssl.cnf
   ```

---

### ### 3. Test TLS with OpenSSL Server
1. Start TLS server:
   ```bash
   openssl s_server -accept 11111 -cert certs/servercertYYY.pem \
     -key private/serverkeyYYY.pem -CAfile certs/cacert.pem -www
   ```
2. Import CA cert into Firefox to remove warning.

---

### ### 4. Configure Apache2 with TLS
1. Copy server key and cert to:
   - `/etc/ssl/private`
   - `/etc/ssl/certs`
2. Duplicate default SSL config:
   ```bash
   cp /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/YYY-ssl.conf
   ```
3. Enable and restart:
   ```bash
   a2enmod ssl
   a2ensite YYY-ssl
   systemctl restart apache2
   ```

---

## 📂 Deliverables
- Writeups for each exploited vulnerability.
- Screenshots of successful exploits.
- Commands/config files for certificate setup.
- Any code or payloads used during testing.

---

## 📖 References
- [OWASP Juice Shop Documentation](https://pwning.owasp-juice.shop)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OpenSSL Documentation](https://www.openssl.org/docs/)