Installation:
NBHXSS is a Python-based XSS hunting framework.  
Make sure you have **Python 3.9+** installed.

Clone the Repository:
git clone https://github.com/YOUR_USERNAME/nbhxss.git
cd nbhxss

If you downloaded ZIP, just extract and enter the folder.

Install Dependencies:
pip install -r requirements.txt

Optional – for headless browser support:
playwright install


Usage:

Scan a Single URL
python nbhxss.py -u "https://target.com/page.php?id=1"

NBHXSS will automatically:
Detect parameters
Check reflection
Identify context
Select correct payload
Try WAF bypass
Verify XSS via headless browser (if enabled)

Scan Multiple Parameters from a File:
python nbhxss.py -l params.txt

Example params.txt:
https://target.com/page.php?id=1
https://target.com/search?q=test

Skip Static Files:
python nbhxss.py -u "https://target.com/" --skip-static

Skips:
.js .css .jpg .png .svg .woff


Payload System
NBHXSS uses built-in payloads located at:
core/payloads/

Payloads are:
Context-aware
Auto-selected
Mutated for WAF bypass
Safe for bug bounty testing

You do NOT need to manually provide payloads.


Docker Usage (Optional):
docker build -t nbhxss .
docker run --rm nbhxss -u https://target.com/page.php?id=1

Disclaimer:
This tool is intended ONLY for:
Educational purposes
Authorized security testing
Bug bounty programs with permission

Do NOT use against targets without explicit authorization.

Author:
**Author:** NHB-BD  
**Version:** 2.1.0

Bug Bounty & Security Research
NBHXSS – Advanced XSS Hunting Framework

Advanced XSS hunting tool for bug bounty and authorized testing only.
