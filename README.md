# Shuriken 🥷

**Shuriken** is an all-in-one directory enumeration tool that automates web path discovery using multiple popular scanners in one run. It is designed to help security researchers and penetration testers quickly identify hidden files and directories on a target website.

---

## Features

* Combines multiple tools for comprehensive enumeration:

  * `ffuf`
  * `gobuster`
  * `katana`
  * `shortscan`
  * `dirsearch`
    
* Automatic dependency checking and installation
* Random User-Agent rotation to bypass basic protections
* Organized output structure per target
* Safe handling of interruptions (CTRL+C)
* Sequential execution for streamlined scanning

---

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd Shuriken
```

2. Ensure the system has:

* **Go** installed
* **Python 3** installed

Dependencies for Python (used by Dirsearch) will be installed automatically.

---

## Usage

Basic scan:

```bash
python3 shuriken.py -u http://example.com
```

With a custom wordlist:

```bash
python3 shuriken.py -u http://example.com -w path/to/wordlist.txt
```

Skip specific tools:

```bash
python3 shuriken.py -u http://example.com -s gobuster,katana
```

---

## Output

All results are saved in:

```
output/<YYYY-MM-DD>_<target-domain>/
```

Each tool generates its own result file:

* `ffuf-result.txt` 
* `gobuster-result.txt`
* `katana-result.txt`
* `shortscan-result.txt`
* `dirsearch-result.txt`

---

## Notes

* The script using a default wordlist, for better result use a custome wordlist.
* The script automatically checks and installs missing dependencies if needed.
* Tools are executed sequentially, but you can skip tools using `-s`.
* Make sure you have permission to scan the target systems.
* Random User-Agent headers are used to avoid simple blocking mechanisms.

---

## Disclaimer

This tool is intended **only** for educational purposes and authorized security testing. Do **not** use it on systems without proper permission.
