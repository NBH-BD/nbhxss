# NBHXSS

**Advanced XSS Hunting Framework for Bug Bounty & Authorized Security Testing**

---


## 🔧 Installation

NBHXSS is a Python-based XSS hunting framework.  
Make sure you have **Python 3.9+** installed.

---


### 📥 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/nbhxss.git
cd nbhxss

---

📦 Install Dependencies
pip install -r requirements.txt

---

🌐 Optional – Headless Browser Support
playwright install

---

🚀 Usage
🔹 Scan a Single URL
python nbhxss.py -u "https://target.com/page.php?id=1"

---

NBHXSS will automatically:

Detect parameters

Check reflection

Identify injection context

Select correct payload

Attempt WAF bypass

Verify XSS via headless browser (if enabled)

---


🔹 Scan Multiple URLs from a File
python nbhxss.py -l params.txt


Example params.txt:

https://target.com/page.php?id=1
https://target.com/search?q=test

---

🔹 Skip Static Files
python nbhxss.py -u "https://target.com/" --skip-static


Skipped file types:

.js .css .jpg .png .svg .woff

---

🧪 Payload System

NBHXSS uses built-in payloads located at:
core/payloads/


Payload features:

Context-aware payload selection

Automatic payload mutation

WAF bypass techniques

Safe for bug bounty testing

✅ You do NOT need to manually provide payloads.

---

🐳 Docker Usage (Optional)
docker build -t nbhxss .
docker run --rm nbhxss -u https://target.com/page.php?id=1

---

⚠️ Disclaimer

This tool is intended ONLY for:

Educational purposes

Authorized security testing

Bug bounty programs with explicit permission

🚫 Do NOT use this tool against targets without authorization.

---

👤 Author

Author: NHB-BD

Version: 2.1.0

---

🛡️ About

NBHXSS is an advanced XSS hunting framework designed for
bug bounty hunters and security researchers.

Happy Hunting 🕵️‍♂️

