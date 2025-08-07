## OWASP Juice Shop Attacks

---

### 🎯 Objective
Identify and exploit security vulnerabilities in the OWASP Juice Shop application.  
The lab covers **First Attacks** (beginner-level) and **Advanced Attacks** to simulate real-world web exploitation.

---

### 🛠 Lab Setup
1. Run Juice Shop in Docker:
   ```bash
   sudo docker run -d -p 3000:3000 -e NODE_ENV=unsafe bkimminich/juice-shop
   ```
2. Open in browser:  
   [http://localhost:3000](http://localhost:3000)
3. Use Firefox Developer Tools or Burp Suite Community Edition for interception and request tampering.

---

## ## Part 1 – First Attacks

### ### 1. Scoreboard Discovery
- Search for the string `score` in `main.js` using browser DevTools.
- Visit the hidden scoreboard path to view all challenge statuses.

---

### ### 2. XSS Injection & Bonus Payload
- Inject JavaScript into the search box:
  ```html
  <iframe src="javascript:alert('xss')">
  ```
- Trigger a “bonus payload” by embedding a SoundCloud player iframe.
- Use coding challenge view to find vulnerable code — note lack of proper sanitization.

---

### ### 3. Short Password Bypass
- Create a user in the registration form.
- Intercept the POST request in DevTools → **Edit & Resend**.
- Change the password field to a 1-character value to bypass password policy.

---

### ### 4. Chatbot Coupon Abuse
- Converse with the chatbot until it sends a coupon code.
- Decode coupon (Z85 format).
- Modify value and re-encode to forge a high-discount coupon (e.g., 90% off).

---

### ### 5. Sensitive File Disclosure
- Browse to `/ftp` endpoint.
- Download available confidential documents (e.g., complaints, contracts).

---

### ### 6. Metrics Exposure
- Access `/metrics` endpoint.
- Observe server performance and operational metrics.

---

### ### 7. Error Handling Abuse
- Send malformed requests or SQLi payloads to trigger unhandled exceptions.
- Capture stack traces or debug output revealing backend details.

---

### ### 8. Privacy Policy Review
- Locate and open the site’s privacy policy page.
- Note any missing or insecure data handling clauses.

---

### ### 9. Zero-Star Feedback Injection
- Submit feedback normally.
- Intercept POST request and change `rating` value to `0` before resending.

---

## ## Part 2 – Advanced Attacks

### ### 1. SQL Injection – Admin Login
- Use SQLi payload in email field:
  ```sql
  ' OR 1=1 --
  ```
- Bypasses authentication by forcing the WHERE clause to always be true.

---

### ### 2. SQL Injection – Targeted User Login
- Modify payload to target a specific account:
  ```sql
  ' OR email LIKE 'bender%' --
  ```

---

### ### 3. Hidden Admin Section & Feedback Deletion
- Search `admin` in `main.js` to locate admin route.
- As admin, delete a 5-star review.
- Log out to complete the challenge.

---

### ### 4. Password Guessing from Social Clues
- From the “Protect Ya’ Passwordz” hint:  
  - Password = pet name  
  - Includes a space  
  - Vowels replaced with zeros (`o` → `0`)
- Log in with guessed password.

---

### ### 5. JWT Token Analysis
- Copy JWT from cookies.
- Decode via [jwt.io](https://jwt.io) or CLI tools.
- Identify overexposed sensitive data (e.g., email, password hash).

---

### ### 6. Insecure Direct Object Reference (IDOR)
- While logged in, intercept basket API request.
- Modify basket ID in URL or payload to view another user’s cart.

---

### ### 7. SQL Injection via Search API
- Request:
  ```bash
  curl "http://localhost:3000/rest/products/search?q=orange"
  ```
- Inject:
  ```text
  orange')) OR 1=1; --
  ```
- Use `UNION SELECT` with correct column count to extract `username,password` from `users`.

---

### ### 8. Password Hash Cracking
- Extract MD5 hashes from SQLi output.
- Crack using:
  ```bash
  hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
  ```
  or:
  ```bash
  john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
  ```

---

### ### 9. Admin Privilege on Registration
- Intercept registration POST request.
- Add:
  ```json
  "role":"admin"
  ```
- Resend request to create an admin-level account.

---

## 📌 Take-Aways
- Juice Shop demonstrates multiple OWASP Top 10 vulnerabilities.
- Combining DevTools/Burp interception with knowledge of web security can uncover critical flaws quickly.
- Proper input validation, access control, and secure coding practices are essential to mitigate these issues.
