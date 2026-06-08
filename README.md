# 🛡️ Web Application Vulnerability Scanner
* Website link: https://webapplication-vulnerablity-scanner.onrender.com/scan
* A Flask-based cybersecurity tool that analyzes web applications for common security weaknesses and generates detailed vulnerability reports.

## 🚀 Features

* HTTPS Verification
* Security Header Analysis

  * Content-Security-Policy (CSP)
  * Strict-Transport-Security (HSTS)
  * X-Frame-Options
  * X-Content-Type-Options
* Server Information Disclosure Detection
* Common Directory Discovery

  * /admin
  * /backup
  * /uploads
  * /test
* Risk Assessment Engine (Low / Medium / High)
* PDF Report Generation
* TXT Report Generation
* SQLite Scan History
* Flask Web Dashboard
* Downloadable Reports

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Security Analysis

* Requests
* BeautifulSoup

### Reporting

* ReportLab

### Database

* SQLite

### Visualization

* Matplotlib

---

## 🔍 How It Works

1. Enter a website URL.
2. The scanner checks:

   * HTTPS usage
   * Security headers
   * Server information disclosure
   * Common sensitive directories
3. Vulnerabilities are identified.
4. A risk score is calculated.
5. Reports are generated in PDF and TXT formats.
6. Scan history is stored in SQLite.

---

## 📄 Generated Reports

The scanner automatically generates:

```text
reports/
├── report.txt
└── report.pdf
```

Reports include:

* Target URL
* Scan findings
* Risk level
* Security recommendations

---

## 🎯 Learning Outcomes

This project helped in understanding:

* Web Application Security
* Vulnerability Assessment
* Security Header Analysis
* Flask Web Development
* Report Generation
* Risk Assessment Techniques
* Cybersecurity Automation

---
