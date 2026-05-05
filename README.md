##### Shuriken 🥷

**Shuriken** is an all-in-one directory enumeration tool designed to automate web path discovery using multiple popular scanners in one run.

It helps security researchers and pentesters quickly find hidden files and directories on a target website by combining the power of several tools.

## Features

* Combines multiple tools:

  * ffuf
  * gobuster
  * katana
  * shortscan
  * dirsearch
* Automatic dependency checking and setup
* Random User-Agent rotation to help bypass basic protections
* Clean and organized output structure
* Handles interruptions safely (CTRL+C)

## Installation

Clone the repository and make sure required tools are in the `tools/` directory.

```bash
git clone <repo-url>
cd Shuriken
```

Make sure you have:

* Go installed
* Python3 installed

## Usage

Basic usage:

```bash
python3 shuriken.py -u http://example.com
```

With custom wordlist:

```bash
python3 shuriken.py -u http://example.com -w wordlist.txt
```

## Output

All results are saved automatically in:

```
output/<date>_<target-domain>/
```

Each tool generates its own result file for easier analysis.

## Notes

* The script will attempt to install missing dependencies automatically.
* Tools are executed sequentially.
* Make sure you have proper permissions when scanning targets.

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Do not use it on systems without permission.
