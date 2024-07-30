import requests
from colorama import Fore, Style
import time
import os
from datetime import datetime
import sys

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://ranch.kuroro.com',
    'Pragma': 'no-cache',
    'Referer': 'https://ranch.kuroro.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.165 Mobile'
}

def print_welcome_message():
    print(r"""      

&&&&&&&&&&&&&&&&&&&@@@@@@%#############%%%#%%#####################%&%%%%%%%%%%%%
&@@@&&&&&&&&&&&&&&@@@@@@@%%######%%%%%%%%###%%%&%##################%%%%%%%%%%%%&
@@@@&&&&&&&&&&&&&&&@@@@@@%###%%&%%%%%%%%%%##%%%%%&&&&###%###########%&%%%%%%%%%&
&&&&&&&&&&&&&&&&&@@@@@@@@%#%&%&%%%%%%%%%%%#%%%&&&&&&&&&%############%%%%%%%%%%%&
&&&&&&&&&&&&&&&&&@@@@@@@@%&&&&&&%%%&&&%%%%#%%&&&&&&&&&&&&############%%%%%%%%%%&
&&&&&&&&&&&&&&&&&&@@@@@@@&&&&&&&&&&&&&&&%%%%&&&&&&&&&&&&&&%%##########%#%%%%%%%%
@@&&&&&&&&&&&&&&&&@@@@@@@&&&&&&&&&&&&&&&%%%%&&&&&&&&&&&&&&&@@@@&@@@@@&&&&&%%%%%%
&&&&@&&&&&&&&&&&&&&@@@@@&&&&&&&&&&&&&&&&%%%%%&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@&
&&&&&&&&&&&&&&&&@%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&@@@@@@@@@@@@@@@@@@@@&
&&&&&&&&&&&&&&&&%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@&
&&&&&&&&&&&&&&&%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@
&&&&&&&&&&&&&&%%@@@@@@@@&&@@&&@@@@@@@@@@@@@@&@@&%@@@@@@@@@%%&@@@@@@@@@@@@@@@@@@@
&&&&&&&&&&&&&&%#&@@@*         &&& .(&@@&,          (##/@@@&%%@@@@@@@@@@@@@@@@@@@
&&&&&&&&&&&&&&%#%&@@.         ,,,    (@*           #%&  .@%%%@@@@&&&&&&&&&&&&&&&
&%%&@&&&&&&&&&%%#%&&@               .@&@                @&%%&@@@@&&&&&@@@&&&%&&@
@@&&&@&&&&&%&&&%%#&&&&%           .@@@@&&/            *@&(%&@@@@&&&&&@&@@&&&&&&&
&&@@&&&&&&&&&&&&&%#(%%%&%&#/,,/#&@@@@@@@@@@&%*.  .,#@&&(&%&@@@@@&&&&@@@&&&&&&&&&
&@@&&&%&&&%&&&&&&@&&%%&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&@@@@&&&@@@@&&&&&&&&&&
&&@@&&&&@@&&&@@&&&&@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&@@@@&&&@@@@@@&&&&&&&&
@&&&&%&&@&&&&&&&&&@@@@@@&%%&&&&&&&&&&&&&&&&&&&&&&@@&&&&&&&&@@@&&&&&@&&&&&@&&&&&&
@@@&@@@@@@&&&&&&&&&@@@@@#(%%###%###%%%%&%%%%%%&%%%%%%%%#*&&@@@&@@@@@@@@@@&&@@@@&
@@&&@@@@@@@@&&@&&@@@@@@@/**&###%%######%###%#%&%#%%#%%%%,/&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@&&@&@@@@@@@@@*.     .       .      .         .,&@@@@@@@@@@@@@@@@@@@@@
%%%%&&&&%%%%%#%%%%%%%%%%/,     .                        .*&@@@@@@@@@@@@@@@@@@@@@
##########%%%%&&&&%%###%(#%%%%##*,.   ..     .*..,,(&%%%*#&&&&&%#%@@@@@@@@@@@@@@
##################%#%%%%%%&%%%#&#%%#%%%##%%%%#%%%%%%%%&%(&%#%%#%%@@@@@&%#(%@@@@@
########################&&%%&&%&&%%%%%&%%%%%%%&%%&&&&%%&&&%&%%%%&@%&@%%%%%%%%%##
#####################%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%&&@%##%%########
#################%#%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%&&&&&&
################%&&&&&&&&&@@@&&&&&&&&&&&%%&&&&&&&@@@@@@@@&%%####################
############(#%%%%%%%&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@&&##%#####################
############################%%%%%%%%%%%%%%%%%%%%%#%%%####(######################
          """)
    print(Fore.GREEN + Style.BRIGHT + "Kuroro BOT")

def update_upgrade(bearer_token, upgrade_id):
    url = 'https://ranch-api.kuroro.com/api/Upgrades/BuyUpgrade'
    headers['Authorization'] = bearer_token
    payload = {
        "upgradeId": upgrade_id
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(Fore.GREEN + f"Upgrade {upgrade_id} successful.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Upgrade {upgrade_id} failed.")
        return None

def perform_action(url, action_name, payload, bearer_token):
    try:
        headers['Authorization'] = bearer_token
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(Fore.GREEN + f"{action_name} successful!")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to {action_name}: {e}")

def query_upgrades(file_path):
    upgrades = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                upgrade_id = line.strip()
                if upgrade_id:
                    upgrades.append(upgrade_id)
    except FileNotFoundError:
        print(Fore.RED + f"File {file_path} not found.")
    return upgrades

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkin(bearer_token):
    url = "https://ranch-api.kuroro.com/api/DailyStreak/ClaimDailyBonus"
    headers['Authorization'] = bearer_token
    
    current_date = datetime.now().strftime("%Y-%m-%d")

    payload = {
        "date": current_date
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(Fore.GREEN + f"Daily bonus claimed successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to claim daily bonus: {e}")

def read_bearer_tokens(file_path):
    tokens = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                token = line.strip()
                if token:
                    tokens.append(token)
    except FileNotFoundError:
        print(Fore.RED + f"File {file_path} not found.")
    return tokens

def animate_loading():
    chars = ["|", "/", "-", "\\"]
    for _ in range(20):
        sys.stdout.write("\r" + chars[_ % len(chars)] + " Please wait...")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 15 + "\r")

def waiting_message_lagged():
    message = Fore.CYAN + Style.BRIGHT + """
@@%%%%@@@@#%####*#%%#*****#####
@@%%%%@@@@%%%%%##%%%%%******###
@@@%%%%@@%%%%%%##%%%%%%@@@@@@@%
%%%%%%#%@@@%%%%%%%%###%@@@@@@@%
%%%%%%@@@@@%@@@@@@@@@@#@@@@@@@@
%%%%%#%@...=%.@.....@#%%@@@@@@@
#%%%%#*%......@:.....:*@@%%@%#%
%@%%@%#*%%..@@@@%...%+#@@%@%%%%
%@%@%@@%@%%%%%%%%%%%%%%@%@@@%%%
@%@%%%@@@*##########%+%@%%%%@%%
@@@@%%@@@:..-=##***:-.%@@@@@@@@
#####*###=:.........::%#@@@@@@@
********##%#*#######%*%##%%@#*@
********#%%%%%%%%%%%%%###@#*#**
******%%%%@@%%%#%%%@@@#********
***********#########***********
   30 𝑚𝑖𝑛𝑠 𝐿𝑎𝑔𝑔𝑒𝑑 𝑟𝑛
    
    """ + Style.RESET_ALL
    sys.stdout.write(message)
    sys.stdout.flush()


def main():
    print_welcome_message()
    
    while True:
        tokens = read_bearer_tokens('bearer.txt')
        
        if not tokens:
            print(Fore.RED + "No bearer tokens found.")
            break
        
        upgrades_file = 'upgrades.txt'
        upgrades = query_upgrades(upgrades_file)
        
        if not upgrades:
            print(Fore.RED + f"No upgrades found in {upgrades_file}.")
            break
        
        for i, bearer_token in enumerate(tokens, start=1):
            print(f"### Processing Account {i} ###")
            
            for upgrade_id in upgrades:
                result = update_upgrade(bearer_token, upgrade_id)
                if not result:
                    continue
                time.sleep(2)
                clear_screen()
                print_welcome_message()
            
            perform_action("https://ranch-api.kuroro.com/api/Clicks/MiningAndFeeding", "Mining", {"mineAmount": 100, "feedAmount": 0}, bearer_token)
            perform_action("https://ranch-api.kuroro.com/api/Clicks/MiningAndFeeding", "Feeding", {"mineAmount": 0, "feedAmount": 10}, bearer_token)
            print(Fore.YELLOW + "Mining and Feeding completed.")
            
            checkin(bearer_token)
            
            print(Fore.BLUE + f"Account {i} completed, moving to the next account")
            animate_loading()
            
            time.sleep(5)
        
        print(Fore.BLUE + "All processes completed.")
        waiting_message_lagged()
        time.sleep(1800)  # Sleep for 30 minutes before starting the loop again

if __name__ == "__main__":
    main()
