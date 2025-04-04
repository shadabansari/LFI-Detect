# LFI Scanner

## Overview
This **Local File Inclusion (LFI) Scanner** is a Python tool designed to detect **LFI vulnerabilities** in web applications by injecting common LFI payloads into a given parameter. The script reads URLs from a file and systematically tests each one for potential LFI exploitation.

## Features
- Tests URLs for **LFI vulnerabilities** using various encoding techniques.
- Supports **randomized User-Agent** headers to evade detection.
- Saves detected **vulnerable URLs** to `lfi_results.txt`.
- Handles **timeouts and connection errors gracefully**.

## Prerequisites
- **Python 3.x**
- **Requests library**

To install dependencies, run:
```bash
pip install requests
```

## Usage
### 1. Prepare a file with target URLs
Ensure you have a file (e.g., `urls.txt`) with a list of target URLs, each on a new line:
```
http://example.com/vuln.php
http://target.com/index.php
```

### 2. Run the LFI Scanner
```bash
python lfi_scanner.py
```
It will prompt for:
- The **file path** containing URLs.
- The **vulnerable parameter** (e.g., `file`, `page`, `include`).

Example:
```
Enter the path to the URL list file (e.g., urls.txt): urls.txt
Enter the vulnerable parameter (e.g., file, page, include): file
```

### 3. Output
- **Vulnerable URLs** are logged to `lfi_results.txt`.
- Console output indicates whether LFI was found or not:
  ```
  [+] LFI Found: http://example.com/vuln.php?file=../../../../../etc/passwd
  [-] No LFI: http://target.com/index.php?file=../../../../../etc/passwd
  ```

## Customization
- Add more **LFI payloads** in the `LFI_PAYLOADS` list.
- Modify **User-Agent randomization** for stealth scanning.

---

## ⚠️ Disclaimer

> **This tool is for educational and authorized testing purposes only.**
> Do **NOT** use this on networks or systems you don't own or have explicit permission to test.
> Unauthorized use of this tool may be illegal and unethical.

---

## 🤝 Contributions Welcome

If you'd like to add more modules, features, or improve functionality — feel free to fork this repo and submit a pull request.

---

## 👤 Author

🔗 LinkedIn: [@xhanix](https://www.linkedin.com/in/xhanix/)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE)


---
📌 **Contributions Welcome!** Feel free to submit issues and pull requests. 🚀

