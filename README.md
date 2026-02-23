# Shuriken

Shuriken is an all-in-one web directory enumeration tool designed for security researchers and penetration testers. It automates multiple industry-standard scanners within a single workflow and organizes results efficiently.

## Overview

Shuriken eliminates the need to manually configure and execute multiple directory discovery tools. It runs them sequentially within one command and stores outputs in a structured format.

## Integrated Tools

* Katana
* FFUF
* Gobuster
* Shortscan
* Dirsearch

## Features

* Multi-tool execution in a single workflow
* Automatic dependency detection and installation
* User-Agent rotation to reduce basic filtering
* Timestamped output directories per target
* Safe interruption handling (CTRL+C)

## Requirements

Linux-based operating system such as:

* Kali Linux
* Ubuntu

Go (Golang)
Python 3

## Installation

### Install Go

```bash
sudo snap install go --classic
```

Or manual installation:

```bash
wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

### Setup Python Virtual Environment

```bash
sudo apt update
sudo apt install python3-venv -y

python3 -m venv venv
source venv/bin/activate
```

## Usage

```bash
python3 shuriken.py --url <TARGET_URL> --wordlist <PATH_TO_LIST>
```

### Arguments

| Argument   | Description                                  | Required | Default               |
| ---------- | -------------------------------------------- | -------- | --------------------- |
| --url      | Target website (include http:// or https://) | Yes      | N/A                   |
| --wordlist | Custom directory wordlist path               | No       | wordlist/wordlist.txt |

## Output Structure

Results are stored in:

```
output/YYYY-MM-DD_domain.com/
```

Files generated:

* katana-result.txt
* ffuf-result.txt
* gobuster-result.txt
* shortscan-result.txt
* dirsearch-result.txt

## Legal Disclaimer

This tool is intended for educational purposes and authorized security testing only. Do not use it against any system without explicit written permission. The author and Rasad Security Group assume no liability for misuse.

## Author

Ali Shahsavar
Rasad Security Group
