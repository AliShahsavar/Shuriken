import subprocess
import time
from datetime import datetime
import argparse
import os
from urllib.parse import urlparse
import random
import json

#Rang ha
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

# Logo e barname (Shuriken)
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
"""
{Color.RESET}

print(header)

# List e abzarhai ke bayad check beshan nasb hastan ya na
check_list = {
  "python":0,
  "go":0,
  "python-req":0,
  "katana":0,
  "ffuf":0,
  "gobuster":0,
  "shortscan":0
}    

# Gereftan e tarikhe emrouz baraye esme folder e khorouji
NOW_DATE = datetime.today().strftime('%Y-%m-%d')
ss
# Gereftan e voroudi ha az karbar (URL va Wordlist)
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Enter URL By Using This Switch", required=True)
parser.add_argument("--wordlist", help="Enter Your Custom Wordlist", default="wordlist/wordlist.txt", required=False)
args = parser.parse_args()

# Joda kardan e domain az URL baraye folder bandi
parsed_domain = urlparse(args.url)
string_domain = str(args.url)
output_path = f"{NOW_DATE}_{parsed_domain.netloc}"

# Hazf kardan e slash akhar e URL age bashe
if args.url.endswith("/"):
  args.url = args.url[:-1]

# Gereftan e ye User-Agent random az file baraye dor zadan e mahdoudiyat ha
def get_user_agent():
  try:
      with open("useragents/user-agents.txt",'r+') as file : 
        USER_AGENT = random.choice(file.readlines())
        return USER_AGENT.strip()
  except FileNotFoundError:
      return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Command haye terminal baraye har abzar
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

# --- Function haye ejraye har abzar ---

def katana_test():
    print("[*] Testing With Katana - Please Wait...")
    try:
        command = f"{dir_enum_shells['katana']} ; echo '[+] Katana finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved; sleep 3", shell=True)

def ffuf_test():
    print("[*] Testing With FFUF - Please Wait...")
    try:
        command = f"{dir_enum_shells['ffuf']} ; echo '[+] FFUF finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        # Age karbar vasat e kar interrupt kard, file json ro be txt tabdil mikone ke rahat beshe khondesh
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
    print("[*] Testing With GoBuster - Please Wait...")
    try:
        command = f"{dir_enum_shells['gobuster']} ; echo '[+] GoBuster finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved ; sleep 3", shell=True)

def shortscan_test():
    print("[*] Testing With Shortscan - Please Wait...")
    try:
        command = f"{dir_enum_shells['shortscan']} ; echo '[+] Shortscan finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved ; sleep 3", shell=True)

def dirsearch_test():
    print("[*] Testing With Dirsearch - Please Wait...")
    try:
        command = f"{dir_enum_shells['dirsearch']} ; echo '[+] Dirsearch finished — closing in 3 seconds...'; sleep 3"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
    except KeyboardInterrupt:
        subprocess.run("\necho [-] CTRL+C Detected - Output Saved ; sleep 3", shell=True)

# Function e asli ke hamechi ro az inja shorou mikonim
def main_function():
    # Sakhtan e folder haye khorouji age vojud nadashte bashan
    if not os.path.exists("output"):
      os.system(f"mkdir output")
    if not os.path.exists(f"output/{output_path}"):
      os.system(f"mkdir output/{output_path}")
      
    print("[~] Start Testing - Please Wait...")
    katana_test()
    print(f"{Color.GREEN}[+] Katana Finished.{Color.RESET}")  
    ffuf_test()
    print(f"{Color.GREEN}[+] FFUF Finished.{Color.RESET}")  
    gobuster_test()
    print(f"{Color.GREEN}[+] GoBuster Finished.{Color.RESET}")  
    shortscan_test()
    print(f"{Color.GREEN}[+] Shortscan Finished.{Color.RESET}")  
    dirsearch_test()
    print(f"{Color.GREEN}[+] dirsearch Finished.{Color.RESET}")  

# --- Ghesmat e Nasb e pish niyaz ha ---

def install_python():
  try : 
    print("[*] Installing Python3...")
    subprocess.run(["sudo","apt","install","python3"])
    print(f"{Color.GREEN}[+] Python3 Installation Successfully.{Color.RESET}")
    check_list["python"] = 1 
  except Exception:
    print(f"{Color.RED}[-] Failed To Download.{Color.RESET}") 
    check_list["python"] = 0

def install_katana():
  if os.path.exists("tools/katana/katana"):
    print("[*] Installing Katana...")
    subprocess.run(["sudo cp tools/katana/katana /usr/local/bin/katana"], shell=True)
    print(f"{Color.GREEN}[+] Katana Installation Successfully.{Color.RESET}")
    check_list["katana"] = 1
  else:
    print(f"{Color.RED}[-] Katana Installation Failed.{Color.RESET}")
    check_list["katana"] = 0

def install_ffuf():
   if os.path.exists("tools/ffuf/ffuf"):
    print("[*] Installing FFUF...")
    subprocess.run(["sudo cp tools/ffuf/ffuf /usr/local/bin/ffuf"], shell=True)
    print(f"{Color.GREEN}[+] FFUF Installation Successfully.{Color.RESET}")
    check_list["ffuf"] = 1
   else:
    print(f"{Color.RED}[-] FFUF Installation Failed.{Color.RESET}")
    check_list["ffuf"] = 0

def install_gobuster():
  if os.path.exists("tools/gobuster/gobuster"):
    print("[*] Installing GoBuster...")
    # Copy kardan e file binary be folder e system ke hame ja dar dastras bashe
    subprocess.run(["sudo cp tools/gobuster/gobuster /usr/local/bin/gobuster"], shell=True)
    print(f"{Color.GREEN}[+] GoBuster Installation Successfully.{Color.RESET}")
    check_list["gobuster"] = 1
  else:
    print(f"{Color.RED}[-] GoBuster Installation Failed.{Color.RESET}")
    check_list["gobuster"] = 0

def install_shortscan():
  if os.path.exists("tools/shortscan/main"):
    print("[*] Installing Shortscan...")
    subprocess.run(["sudo cp tools/shortscan/main /usr/local/bin/main"], shell=True)
    print(f"{Color.GREEN}[+] Shortscan Installation Successfully.{Color.RESET}")
    check_list["shortscan"] = 1
  else:
    print(f"{Color.RED}[-] Shortscan Installation Failed.{Color.RESET}")
    check_list["shortscan"] = 0

# Check kardan e inke aya abzar ha nasban ya na
def checking_dependencies():
  print(f"{Color.YELLOW}[#] Make Sure The Latest Version Of Go Is Installed.{Color.RESET}")  
  print("[*] Start Checking Dependencies...")
  time.sleep(1)
  
  # Check kardan e Go (chon kheili az abzarha ba Go neveshte shodan)
  try:
      go_version = subprocess.run(["go", "version"], capture_output=True, text=True, check=True)
      output = go_version.stdout.strip()
      print(f"{Color.GREEN}[+] Go Installed: {output}{Color.RESET}")
      check_list["go"] = 1
  except (FileNotFoundError, subprocess.CalledProcessError):
      check_list["go"] = 0 

  if check_list["go"] == 1: 
    # Check kardan e Python
    try:
        py_result = subprocess.run(["python3","--version"], capture_output=True, text=True, check=True)
        output = py_result.stdout.strip()
        print(f"{Color.GREEN}[+] Python3 Installed: {output}{Color.RESET}")
        check_list["python"] = 1
    except FileNotFoundError:
        print(f"{Color.RED}[!] Python3 Is Not installed.{Color.RESET}")
        install_python()

    # Nasb e library haye Python baraye dirsearch
    try:
        print("[*] Checking Python Requirements...")
        subprocess.run(["pip3 install -r tools/dirsearch/requirements.txt"], shell=True, check=True)
        check_list["python-req"] = 1
    except:
        print(f"{Color.RED}[-] Failed to install Python Req.{Color.RESET}")
        check_list["python-req"] = 0

    # Check kardan e tak tak e abzar ha dar path e system
    # Katana
    if os.path.exists("/usr/local/bin/katana"):
        print(f"{Color.GREEN}[+] Katana Already Installed.{Color.RESET}")
        check_list["katana"] = 1
    else: install_katana()

    # FFUF
    if os.path.exists("/usr/local/bin/ffuf"):
        print(f"{Color.GREEN}[+] FFUF Already Installed.{Color.RESET}")
        check_list["ffuf"] = 1
    else: install_ffuf()
    
    # GoBuster
    if os.path.exists("/usr/local/bin/gobuster"):
        print(f"{Color.GREEN}[+] GoBuster Already Installed.{Color.RESET}")
        check_list["gobuster"] = 1
    else: install_gobuster()

    # Shortscan
    if os.path.exists("/usr/local/bin/main"):
        print(f"{Color.GREEN}[+] Shortscan Already Installed.{Color.RESET}")
        check_list["shortscan"] = 1
    else: install_shortscan()

    # Age aksar e abzar ha ok budan, barname shorou mishe
    if sum(check_list.values()) >= 6: 
      print(f"\n{Color.PURPLE}~ Welcome To Shuriken =){Color.RESET}")
      main_function()
    else:
      print(f"{Color.RED}\n[!] Failed to run Shuriken - Check missing tools.{Color.RESET}")
      
  else:
    print(f"{Color.RED}[!] Go is Not installed, Shutting down...{Color.RESET}")

# Ghabl az shorou, check mikonim URL dorost vared shode bashe
if parsed_domain.scheme not in ["https", "http"]:
  raise argparse.ArgumentTypeError("URL should start with http:// or https://")
else:
  checking_dependencies()
