import requests
import json
import subprocess as sp
import keyboard
#from colorama import init, Fore, Style
from colorama import init, Fore, Style, Back

init(autoreset=True) ## Colorama
INPUT_STATE = None # for MAIN() loop

API_URL = "https://api.covid19india.org/data.json"
RESPONSE = requests.get(API_URL)
DATA = RESPONSE.text

PARSED = json.loads(DATA)

## All Statee Extraction
## This becomes a list
STATEWISE = PARSED["statewise"]    ##extracting All data of total (0) amd state (1-37)


STATE_NUM = []
for count in STATEWISE:
    STATE_NUM.append({STATEWISE.index(count):STATEWISE[STATEWISE.index(count)]["state"]})  ## example 0:'total' \n 1:'Kerela'
    
sp.call('cls',shell=True)
print(Style.BRIGHT + Fore.GREEN + '''
                                                                                                                                               
                                                                                                                                               
 ██████╗ ██████╗ ██╗   ██╗██╗██████╗        ██╗ █████╗     ███████╗████████╗ █████╗ ████████╗███████╗
██╔════╝██╔═══██╗██║   ██║██║██╔══██╗      ███║██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝
██║     ██║   ██║██║   ██║██║██║  ██║█████╗╚██║╚██████║    ███████╗   ██║   ███████║   ██║   ███████╗
██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║╚════╝ ██║ ╚═══██║    ╚════██║   ██║   ██╔══██║   ██║   ╚════██║
╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝       ██║ █████╔╝    ███████║   ██║   ██║  ██║   ██║   ███████║
 ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝        ╚═╝ ╚════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                                                                                                                                                                                                                    
''')

print("-------- Python Code by Soumik (sh3llc0d3) ----------\n")# + Style.RESET_ALL)
print("-------- Stats API : api.covid19india.org ----------\n")
sp.call('TIMEOUT /T 5 > null',shell=True)

#print("STATE_NUM\n",STATE_NUM)

sp.call('cls',shell=True)

def STATE_LIST():
    print(Fore.BLACK + Back.WHITE + "\n\nList of States")
    print("---------------\n")
    for length_STATE_NUM in STATE_NUM:
        print(str(length_STATE_NUM).strip('{}'))
    print("\n-------------------------------------\n")



## Total(T) data extractopm
def TOTAL():
    #sp.call('cls',shell=True)
    DATA = STATEWISE[0]
    CONFIRMED = DATA["confirmed"]
    ACTIVE = DATA["active"]
    DEATHS = DATA["deaths"]
    DELTA = DATA["delta"]
    RECOVERED = DATA["recovered"]
    LASTUPDTIME = DATA["lastupdatedtime"]
    print(Style.BRIGHT + Fore.WHITE + Back.GREEN + "\n------ COVID-19 TOTAL STATS IN INDIA --------\n")
    print("States: {}\n".format(len(STATEWISE)-2))
    print("Confirmed: {}\nActive: {}\nDeaths: {}\nRecovered: {}\nTime: {}\n".format(CONFIRMED,ACTIVE,DEATHS,RECOVERED,LASTUPDTIME))
    print("---------------------------------------\n\n")
    
## Print List of states and Total
STATE_LIST()
TOTAL()

## Read State Data
def STATE_DATA(num):
    sp.call('cls',shell=True)
    sp.call('TIMEOUT /T 1 > null',shell=True)
    DATA = STATEWISE[num]
    CONFIRMED = DATA["confirmed"]
    ACTIVE = DATA["active"]
    DEATHS = DATA["deaths"]
    DELTA = DATA["delta"]
    RECOVERED = DATA["recovered"]
    LASTUPDTIME = DATA["lastupdatedtime"]
    STATE = DATA["state"]
    print(Style.BRIGHT + Fore.WHITE + Back.GREEN + "\n------ COVID-19 STATS IN {} --------\n".format(STATE))
    print("Confirmed: {}\nActive: {}\nDeaths: {}\nRecovered: {}\nTime: {}\n".format(CONFIRMED,ACTIVE,DEATHS,RECOVERED,LASTUPDTIME))
    print("---------------------------------------\n\n")
        


def MAIN():
    global INPUT_STATE
    while INPUT_STATE == None:        
        try:
            INPUT_STATE = int(input(Fore.YELLOW + "Enter State Number for Data(1-37) or Ctrl+c to quit:" + Style.RESET_ALL + " "))
            if INPUT_STATE > 37 or INPUT_STATE < 0:
                print(Style.BRIGHT + Fore.RED + "\nInvalid State Number..... Retry!")
                INPUT_STATE = None
            elif INPUT_STATE in range(0,38):
                STATE_DATA(INPUT_STATE)
                INPUT_STATE = None
                sp.call('TIMEOUT /T 1 > null',shell=True)
                STATE_LIST()
                               
        except ValueError:           
            print(Style.BRIGHT+ Fore.RED + "\nNot a number, try again")
            

MAIN()
    


