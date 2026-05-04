Got it — you don’t want a rewrite, you want your **same README style**, just updated to reflect your new code. Here’s a clean version that stays very close to yours but matches what your script actually does now:

---

## Shuriken: Automated Web Directory Scanner

Shuriken is a fast tool for security testing. It runs several popular scanners at the same time and puts all the results in one place. This saves time for researchers and security professionals.

### Main Features

* **Runs Multiple Tools:** Uses Katana, FFUF, Gobuster, Shortscan, and Dirsearch together.
* **Auto Dependency Check:** Automatically checks and installs required tools and dependencies.
* **Smart Scanning:** Uses random User-Agents to mimic real browsers and avoid basic blocking.
* **Organized Output:** Saves results in folders named by date and target domain.
* **Interrupt Safe:** Saves results even if the scan is stopped (CTRL+C supported).

### Requirements

* **System:** Linux (Kali Linux or Ubuntu recommended)
* **Languages:** Python3 and Go

---

### How to Install

#### 1. Install Go

On **Ubuntu**, install Go using Snap:

```bash
sudo snap install go --classic
```

Or download manually from:
[https://go.dev/dl/](https://go.dev/dl/)

#### 2. Prepare Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Python Requirements

```bash
pip install -r tools/dirsearch/requirements.txt
```

---

### Project Structure (Important)

Make sure required tools exist in the correct paths:

```
tools/
├── katana/
├── ffuf/
├── gobuster/
├── shortscan/
├── dirsearch/
```

---

### How to Use

**Run a scan:**

```bash
python3 shuriken.py --url <TARGET_URL>
```

**With custom wordlist:**

```bash
python3 shuriken.py --url <TARGET_URL> --wordlist <PATH_TO_LIST>
```

---

### Options

| Option             | Purpose              | Required | Default                 |
| :----------------- | :------------------- | :------- | :---------------------- |
| `-u`, `--url`      | Target website URL   | Yes      | None                    |
| `-w`, `--wordlist` | Custom wordlist path | No       | `wordlist/wordlist.txt` |

---

### Output

All results are stored in the `output/` directory.

**Example:**

```
output/2026-05-04_example.com/
```

**Files include:**

* `ffuf-result.json / txt`
* `gobuster-result.txt`
* `katana-result.txt`
* `shortscan-result.txt`
* `dirsearch-result.txt`

---

### Notes

* Automatically removes trailing `/` from URLs
* Uses random User-Agent from:

```
useragents/user-agents.txt
```

* Falls back to a default User-Agent if file is missing

---

### Rules & Safety

Only use this tool on websites you own or have permission to test.
Unauthorized scanning is illegal.

The author is not responsible for misuse of this tool.

---

**Author:** Ali Shahsavar
**Group:** Rasad Security Group
