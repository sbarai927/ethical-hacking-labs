# Lab 3 – Web Application & TLS Security

---

## 📌 Overview
Lab 3 consists of **two independent tracks**:

1. **Option A – OWASP Juice Shop**  
   Perform reconnaissance, exploitation, and vulnerability analysis on a deliberately insecure web application.
   
2. **Optional Lab – X.509 Certificates & TLS**  
   Set up your own Certificate Authority, issue server certificates, and configure TLS on both OpenSSL and Apache2.

---

## ## Option A: OWASP Juice Shop Attacks

### 🛠 Setup
1. Start Juice Shop in your Kali Linux VM:
   ```bash
   sudo docker run -d -p 3000:3000 -e NODE_ENV=unsafe bkimminich/juice-shop
   ```
2. Access the app in your browser: [http://localhost:3000](http://localhost:3000)
3. Use **Firefox Developer Tools** or **Burp Suite Community Edition** for analysis.

---

### ### Part 1 – First Attacks

#### 1️⃣ Find the Scoreboard
- Use **Debugger** in DevTools to search for `score` in `main.js`.
- Identify and visit the scoreboard URL to reveal challenges.

#### 2️⃣ XSS Injection & Bonus Payload
- Inject JavaScript via the search field:
  ```html
  <iframe src="javascript:alert(`xss`)">
  ```
- Trigger the Juice Shop song by embedding a SoundCloud iframe.
- Identify the vulnerable code using the coding challenge interface.

#### 3️⃣ Short Password Bypass
- Create a new account.
- Modify POST request parameters in DevTools to bypass the password policy (e.g., 1-character password).

#### 4️⃣ Chatbot Coupon Abuse
- Harass the chatbot to obtain a coupon.
- Decode using **z85**, then forge a 90% discount coupon.

#### 5️⃣ Sensitive File Disclosure
- Browse `/ftp` directory and download confidential files.

#### 6️⃣ Metrics Exposure
- Access `/metrics` endpoint to view application metrics.

#### 7️⃣ Poor Error Handling
- Trigger unhandled errors through crafted inputs.

#### 8️⃣ Privacy Policy Check
- Locate and review the privacy policy.

#### 9️⃣ Zero-Star Feedback
- Intercept and modify the POST request to submit a **0-star** review.

---

### ### Part 2 – Advanced Attacks

#### 1️⃣ SQL Injection – Admin Login
- Payload:
  ```sql
  ' OR 1=1 --
  ```
- Understand why this bypasses authentication and propose mitigations.

#### 2️⃣ Targeted SQL Injection – User Login
- Modify injection to log in as `bender` using:
  ```sql
  ' OR email LIKE 'bender%' --
  ```

#### 3️⃣ Admin Section Access & Feedback Removal
- Find `/admin` path from `main.js`.
- As admin, remove 5-star feedback.

#### 4️⃣ Password Guessing from Social Clues
- Watch “Protect Ya’ Passwordz” video.
- Craft password with pet name + vowel-to-zero substitutions.

#### 5️⃣ JWT Token Analysis
- Extract JWT from cookies.
- Decode at [jwt.io](https://jwt.io) and identify sensitive data.

#### 6️⃣ Insecure Direct Object Reference (IDOR)
- Modify REST request or Session Storage to view another user’s shopping basket.

#### 7️⃣ SQL Injection via Search API
- Example payload:
  ```text
  orange')) OR 1=1; --
  ```
- Use `UNION SELECT` to extract usernames and password hashes.
- Identify the importance of matching column counts.

#### 8️⃣ Password Hash Cracking
- Crack MD5 hashes using `hashcat` or `john`.

#### 9️⃣ Privilege Escalation on Registration
- Modify registration request to include:
  ```json
  "role":"admin"
  ```

---