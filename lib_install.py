#! /usr/bin/env python3
import os
import time

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

print('[*]Starting Library Installation...')
time.sleep(2)
print('[*]Configuring Apt Installation Sources...')

sources = """\
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib
"""
with open('/etc/apt/sources.list', 'w+') as f: #config sources list for full package installation
  f.write(sources)
f.close()

print('[*]Sources Configured!')
time.sleep(2)
print('[*]Updating and Upgrading Packages...')
os.system('sudo apt-get update && sudo apt-get upgrade')
print('[*]Installing Linux Packages...')
os.system('sudo apt-get install figlet netcat hashcat php tshark tcpdump telnet ftp git apache2 ssh arp-scan macchanger hddtemp lm-sensors ettercap-text-only build-essential ntfs-3g cifs.utils mount reaver aircrack-ng curl dhcpd isc-dhcp-server hostapd lighttpd unzip xterm pyrit openssl ufw -y')
os.system('sudo ufw enable')
print('[*]Installing python2 and 3 libraries...')
os.system('sudo pip install -U -I pyusb')
os.system('sudo pip install -U platformio')
os.system('sudo pip install -r requirements2.txt')
os.system('sudo pip3 install -r requirements3.txt')
print('[*]Installing Tools...')
print('[*]Installing and Initializing mousejack...')
os.system('sudo git clone https://github.com/BastilleResearch/mousejack.git')
os.chdir('mousejack')
os.system('sudo git submodule init')
os.system('sudo git submoudle update')
os.chdir('..')
os.system('sudo git clone https://github.com/insecurityofthings/jackit.git')
os.chdir('jackit')
os.system('sudo pip install -r requirements.txt')
os.system('sudo pip install -e .')
os.chdir('..')
print('[*]Installing WiFi-Pumpkin...')
os.system('sudo git clone https://github.com/P0cL4bs/WiFi-Pumpkin')
os.chdir("WiFi-Pumpkin")
os.system('sudo ./installer.sh --install')
os.system('sudo pip install --upgrade pyasn1-modules')
os.chdir('..')
print('[*]Installing Wifite2...')
os.system("git clone https://github.com/derv82/wifite2.git")
os.chdir('wifite2')
os.system('sudo python setup.py install')
os.chdir('..')
print('[*]Installing wifijammer...')
os.system('sudo git clone https://github.com/DanMcInerney/wifijammer')
print('[*]Installing pentbox...')
os.system("sudo git clone https://github.com/H4CK3RT3CH/pentbox-1.8")
print('[*]Installing Airgeddon...')
os.system("sudo git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
print('[*]Installing Fluxion...')
os.system("sudo git clone https://github.com/FluxionNetwork/fluxion")
print('[*]Updating and Upgrading Packages...')
os.system('sudo apt-get update && sudo apt-get upgrade')
os.system('sudo apt autoremove')
print('[+]Library Installation Complete...')
