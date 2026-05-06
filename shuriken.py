import subprocess
import time
from datetime import datetime
import argparse
import os
from urllib.parse import urlparse
import random
import json

# Colors
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Program Logo
header = f"""{Color.CYAN} 

                      00                                        
                      00                                        
                     0000                                       
                    010000                                      
                    000000                                      
                   00010000                                     
                     0000                                       
     00001000000     0000    000110000000    
       0000100000  00000100 00000100100        
         0000000100000010000001000000          
           000   000001000000   000            
                   000010010                    
                  00010001001                   
               0100000    0010010                
               000100      010000                
              00100010    00000000               
              001000        000110               
             00000             00000               
             00                   00               
                                                 
    Shuriken By Rasad Security Group ~ V1.0 
        Author : Ali Shahsavar
    ALL-IN-ONE Directory Enumeration Tool
{Color.RESET}"""

print(header)

# List of tools to be checked for installation
check_list = {
  "python":0,
  "go":0,
  "python-req":0,
  "katana":0,
  "ffuf":0,
  "gobuster":0,
  "shortscan":0
}    

# Get current date for output folder naming
NOW_DATE = datetime.today().strftime('%Y-%m-%d')

# --- Argument Parsing ---
parser = argparse.ArgumentParser(description="Shuriken: All-in-One Directory Enumeration Tool")

parser.add_argument("-u", "--url", 
                    help="Target URL (e.g., http://example.com)", 
                    metavar="URL", 
                    required=True)

parser.add_argument("-w", "--wordlist", 
                    help="Path to custom wordlist (default: wordlist/wordlist.txt)", 
                    default="wordlist/wordlist.txt", 
                    metavar="PATH",
                    required=False)

parser.add_argument("-s", "--skip", 
                    help="Tools to skip, separated by commas (e.g., gobuster,katana)", 
                    default="", 
                    required=False)

args = parser.parse_args()

# Process skip list: split by comma, strip whitespace, and lowercase
skip_list = [tool.strip().lower() for tool in args.skip.split(",")] if args.skip else []

# Extract domain from URL for folder organization
parsed_domain = urlparse(args.url)
if parsed_domain.scheme not in ["https", "http"]:
    print(f"{Color.RED}[!] Error: URL must start with http:// or https://{Color.RESET}")
    exit(1)

output_path = f"{NOW_DATE}_{parsed_domain.netloc}"

# Remove trailing slash from URL if present
if args.url.endswith("/"):
  args.url = args.url[:-1]

# Fetch a random User-Agent
def get_user_agent():
  try:
      with open("useragents/user-agents.txt",'r+') as file : 
        USER_AGENT = random.choice(file.readlines())
        return USER_AGENT.strip()
  except FileNotFoundError:
      return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Terminal commands
dir_enum_shells = {
    "ffuf": (
        f"ffuf -u {args.url}/FUZZ -w '{args.wordlist}' "
        f"-H 'User-Agent: {get_user_agent()}' "
        f"-o output/{output_path}/ffuf-result.json -of json"
    ),
    "gobuster": (
        f"gobuster dir -u {args.url} -w '{args.wordlist}' -useragent '{get_user_agent()}' -o output/{output_path}/gobuster-result.txt --exclude-length 0 " 
    ),
    "katana": (
        f"katana -u {args.url} "
        f"-H 'User-Agent: {get_user_agent()}' "
        f"-o output/{output_path}/katana-result.txt"
    ),
    "shortscan": (
        f"main -o human {args.url} "
        f"--header 'User-Agent: {get_user_agent()}' "
        f"> output/{output_path}/shortscan-result.txt"
    ),
    "dirsearch": (
        f"python3 tools/dirsearch/dirsearch.py -u {args.url} "
        f"-w '{args.wordlist}' "
        f"--user-agent '{get_user_agent()}' "
        f"--follow-redirects "
        f"-o output/{output_path}/dirsearch-result.txt"
    )
}

# --- Tool Execution Functions ---

def katana_test():
    print("[*] Testing with Katana - Please wait...")
    try:
        command = f"{dir_enum_shells['katana']} ; echo '[+] Katana finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved; sleep 3", shell=True)

def ffuf_test():
    print("[*] Testing with FFUF - Please wait...")
    try:
        command = f"{dir_enum_shells['ffuf']} ; echo '[+] FFUF finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved; sleep 3", shell=True)
        try:
            with open(f"output/{output_path}/ffuf-result.json", "r") as json_file:
                data = json.load(json_file)
            with open(f"output/{output_path}/ffuf-result.txt", "w") as txt_file:
                for result in data["results"]:
                    txt_file.write(str(result["url"]) + " ---> " + str(result["status"]) + "\n")
            os.system(f"rm -rf output/{output_path}/ffuf-result.json")
        except:
            pass

def gobuster_test():
    print("[*] Testing with GoBuster - Please wait...")
    try:
        command = f"{dir_enum_shells['gobuster']} ; echo '[+] GoBuster finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved ; sleep 3", shell=True)

def shortscan_test():
    print("[*] Testing with Shortscan - Please wait...")
    try:
        command = f"{dir_enum_shells['shortscan']} ; echo '[+] Shortscan finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved ; sleep 3", shell=True)

def dirsearch_test():
    print("[*] Testing with Dirsearch - Please wait...")
    try:
        command = f"{dir_enum_shells['dirsearch']} ; echo '[+] Dirsearch finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved ; sleep 3", shell=True)

# --- Main Entry Point ---
def main_function():
    if not os.path.exists("output"):
      os.system(f"mkdir output")
    if not os.path.exists(f"output/{output_path}"):
      os.system(f"mkdir output/{output_path}")
      
    print("[~] Starting tests - Please wait...")
    
    # Katana
    if "katana" not in skip_list:
        katana_test()
        print(f"{Color.GREEN}[+] Katana Finished.{Color.RESET}")  
    else:
        print(f"{Color.YELLOW}[!] Skipping Katana (User Request).{Color.RESET}")

    # FFUF
    if "ffuf" not in skip_list:
        ffuf_test()
        print(f"{Color.GREEN}[+] FFUF Finished.{Color.RESET}")  
    else:
        print(f"{Color.YELLOW}[!] Skipping FFUF (User Request).{Color.RESET}")

    # GoBuster
    if "gobuster" not in skip_list:
        gobuster_test()
        print(f"{Color.GREEN}[+] GoBuster Finished.{Color.RESET}")  
    else:
        print(f"{Color.YELLOW}[!] Skipping GoBuster (User Request).{Color.RESET}")

    # Shortscan
    if "shortscan" not in skip_list:
        shortscan_test()
        print(f"{Color.GREEN}[+] Shortscan Finished.{Color.RESET}")  
    else:
        print(f"{Color.YELLOW}[!] Skipping Shortscan (User Request).{Color.RESET}")

    # Dirsearch
    if "dirsearch" not in skip_list:
        dirsearch_test()
        print(f"{Color.GREEN}[+] Dirsearch Finished.{Color.RESET}")  
    else:
        print(f"{Color.YELLOW}[!] Skipping Dirsearch (User Request).{Color.RESET}")

# --- Dependency Section ---

def install_python():
  try : 
    print("[*] Installing Python3...")
    subprocess.run(["sudo","apt","install","python3"])
    print(f"{Color.GREEN}[+] Python3 installed successfully.{Color.RESET}")
    check_list["python"] = 1 
  except Exception:
    print(f"{Color.RED}[-] Failed to download Python3.{Color.RESET}") 
    check_list["python"] = 0

def install_katana():
  if os.path.exists("tools/katana/katana"):
    print("[*] Installing Katana...")
    subprocess.run(["sudo cp tools/katana/katana /usr/local/bin/katana"], shell=True)
    print(f"{Color.GREEN}[+] Katana installed successfully.{Color.RESET}")
    check_list["katana"] = 1
  else:
    print(f"{Color.RED}[-] Katana installation failed: Source binary not found.{Color.RESET}")
    check_list["katana"] = 0

def install_ffuf():
   if os.path.exists("tools/ffuf/ffuf"):
    print("[*] Installing FFUF...")
    subprocess.run(["sudo cp tools/ffuf/ffuf /usr/local/bin/ffuf"], shell=True)
    print(f"{Color.GREEN}[+] FFUF installed successfully.{Color.RESET}")
    check_list["ffuf"] = 1
   else:
    print(f"{Color.RED}[-] FFUF installation failed: Source binary not found.{Color.RESET}")
    check_list["ffuf"] = 0

def install_gobuster():
  if os.path.exists("tools/gobuster/gobuster"):
    print("[*] Installing GoBuster...")
    subprocess.run(["sudo cp tools/gobuster/gobuster /usr/local/bin/gobuster"], shell=True)
    print(f"{Color.GREEN}[+] GoBuster installed successfully.{Color.RESET}")
    check_list["gobuster"] = 1
  else:
    print(f"{Color.RED}[-] GoBuster installation failed: Source binary not found.{Color.RESET}")
    check_list["gobuster"] = 0

def install_shortscan():
  if os.path.exists("tools/shortscan/main"):
    print("[*] Installing Shortscan...")
    subprocess.run(["sudo cp tools/shortscan/main /usr/local/bin/main"], shell=True)
    print(f"{Color.GREEN}[+] Shortscan installed successfully.{Color.RESET}")
    check_list["shortscan"] = 1
  else:
    print(f"{Color.RED}[-] Shortscan installation failed: Source binary not found.{Color.RESET}")
    check_list["shortscan"] = 0

def checking_dependencies():
  print(f"{Color.YELLOW}[#] Ensure the latest version of Go is installed.{Color.RESET}")  
  print("[*] Checking dependencies...")
  time.sleep(1)
  
  try:
      go_version = subprocess.run(["go", "version"], capture_output=True, text=True, check=True)
      output = go_version.stdout.strip()
      print(f"{Color.GREEN}[+] Go Found: {output}{Color.RESET}")
      check_list["go"] = 1
  except (FileNotFoundError, subprocess.CalledProcessError):
      check_list["go"] = 0 

  if check_list["go"] == 1: 
    try:
        py_result = subprocess.run(["python3","--version"], capture_output=True, text=True, check=True)
        output = py_result.stdout.strip()
        print(f"{Color.GREEN}[+] Python3 Found: {output}{Color.RESET}")
        check_list["python"] = 1
    except FileNotFoundError:
        print(f"{Color.RED}[!] Python3 is not installed.{Color.RESET}")
        install_python()

    try:
        print("[*] Checking Python requirements...")
        subprocess.run(["pip3 install -r tools/dirsearch/requirements.txt"], shell=True, check=True)
        check_list["python-req"] = 1
    except:
        print(f"{Color.RED}[-] Failed to install Python requirements.{Color.RESET}")
        check_list["python-req"] = 0

    if os.path.exists("/usr/local/bin/katana"):
        print(f"{Color.GREEN}[+] Katana is already installed.{Color.RESET}")
        check_list["katana"] = 1
    else: install_katana()

    if os.path.exists("/usr/local/bin/ffuf"):
        print(f"{Color.GREEN}[+] FFUF is already installed.{Color.RESET}")
        check_list["ffuf"] = 1
    else: install_ffuf()
    
    if os.path.exists("/usr/local/bin/gobuster"):
        print(f"{Color.GREEN}[+] GoBuster is already installed.{Color.RESET}")
        check_list["gobuster"] = 1
    else: install_gobuster()

    if os.path.exists("/usr/local/bin/main"):
        print(f"{Color.GREEN}[+] Shortscan is already installed.{Color.RESET}")
        check_list["shortscan"] = 1
    else: install_shortscan()

    if sum(check_list.values()) == 7 : 
      print(f"\n{Color.PURPLE}~ Welcome to Shuriken =){Color.RESET}")
      main_function()
    else:
      print(f"{Color.RED}\n[!] Failed to run Shuriken - Please check for missing tools.{Color.RESET}")
      
  else:
    print(f"{Color.RED}[!] Go is not installed. Shutting down...{Color.RESET}")

# Start
checking_dependencies()
