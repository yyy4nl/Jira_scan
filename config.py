import colorama
colorama.init()


headers = { 'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
            ,'Content-Type': 'application/json'
}

AWS_INSTANCE = "http://169.254.169.254/latest"
AWS_METADATA = "http://169.254.169.254/latest/meta-data/"
AWS_IAM_DATA = "http://169.254.169.254/latest/meta-data/iam/security-credentials/"
AWS_IAM_CRED = "http://169.254.169.254/latest/meta-data/iam/security-credentials/%s" #<rolename


GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
CYAN = colorama.Fore.CYAN
YELLOW = colorama.Fore.YELLOW
DIM=colorama.Style.BRIGHT
DIM_RESET=colorama.Style.RESET_ALL
MAGENTA=colorama.Fore.MAGENTA
RESET2 = colorama.Back.RESET



def banner():
    banner=rf'''{RED}
    
    
    _ _                                 
  (_|_)                               
    _ _ _ __ __ _   ___  ___ __ _ _ __  
   | | | '__/ _\` | / __|/ __/ _\` | '_ \ 
   | | | | | (_| | \__ \ (_| (_| | | | |
   | |_|_|  \__,_| |___/\___\__,_|_| |_|
  _/ |         ______                   
 |__/         |______|         
   '''


    print(banner)
    print(f"{CYAN}\t Jira-Lens : JIRA Security Auditing Tool {RESET} [\n\n")
