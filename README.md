# 🥷 Shuriken – All-In-One Directory Enumeration Tool

Shuriken is a high-performance automation framework built for security researchers and penetration testers. It streamlines web directory enumeration by orchestrating multiple industry-standard tools into a single, efficient workflow.

Instead of manually configuring and running multiple scanners, Shuriken executes them simultaneously and organizes results automatically.

---

## 🚀 Features

* 🔥 **Multi-Tool Integration**
  Runs:

  * Katana
  * FFUF
  * Gobuster
  * Shortscan
  * Dirsearch

* ⚙ **Automatic Dependency Management**
  Detects and installs missing tools and required languages (Go & Python).

* 🕵️ **Smart User-Agent Rotation**
  Mimics authentic browser traffic to bypass basic filtering.

* 📁 **Organized Output Structure**
  Generates timestamped result directories for each target:

  ```
  YYYY-MM-DD_domain.com/
  ```

* 🛑 **Session Resilience**
  Safe interruption support (`CTRL+C`) without losing collected results.

---

## 🖥️ System Requirements

Shuriken requires a Linux-based environment such as:

* Kali Linux
* Ubuntu

---

## 🛠 Installation & Setup

### 1️⃣ Install Go (Golang)

Go is required for several integrated tools.

#### Method A: Snap Installation (Recommended for Ubuntu)

```bash
sudo snap install go --classic
```

#### Method B: Manual Installation

```bash
wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

---

### 2️⃣ Setup Python Virtual Environment (Recommended)

To prevent dependency conflicts:

```bash
sudo apt update
sudo apt install python3-venv -y

python3 -m venv venv
source venv/bin/activate
```

Ensure `(venv)` appears in your terminal before running Shuriken.

---

## 📌 Usage

### Basic Command

```bash
python3 shuriken.py --url <TARGET_URL> --wordlist <PATH_TO_LIST>
```

### Command Line Arguments

| Argument     | Description                                  | Required | Default               |
| ------------ | -------------------------------------------- | -------- | --------------------- |
| `--url`      | Target website (include http:// or https://) | ✅ Yes    | N/A                   |
| `--wordlist` | Custom directory wordlist path               | ❌ No     | wordlist/wordlist.txt |

---

## 📂 Output Structure

All results are stored inside the `output/` directory.

Example:

```
output/
└── 2026-02-23_example.com/
    ├── katana-result.txt
    ├── ffuf-result.txt
    ├── gobuster-result.txt
    ├── shortscan-result.txt
    └── dirsearch-result.txt
```

Each scan generates its own timestamped folder.

---

## ⚠️ Important Notice

> **Legal & Safety Disclaimer**
>
> Shuriken is intended strictly for educational purposes and authorized security testing.
>
> Do **NOT** use this tool against any system without explicit written permission.
>
> The author and Rasad Security Group assume no responsibility for misuse or unauthorized activities.

---

## 👨‍💻 Author

**Ali Shahsavar**
Organization: Rasad Security Group
