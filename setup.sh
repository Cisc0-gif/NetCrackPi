#! /bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

wait_func() {
  read -p "PRESS ENTER TO CONTINUE" wait
}

printf ${RED}
read -p "*RUN AS ROOT*" root
printf "${BLUE}[*]Writing File Permissions...${NC}\n"
sudo chmod -R 777 *
printf "${GREEN}[+]Done! ${BLUE} \n[*]Updating and Upgrading Packages...${NC}\n"
sudo apt-get update && sudo apt-get upgrade
printf "${GREEN}[+]Done! ${BLUE} \n[*]Making sure pip and pip3 are installed...${NC}\n"
sudo apt-get install python-pip python3-pip
printf "${GREEN}[+]Done! ${BLUE} \n[*]Configuring apt Installation Sources...${NC}\n"
sudo curl https://pastebin.com/raw/fNL6X8gt > /etc/apt/sources.list
sudo apt-get update
printf "${GREEN}[+]Done! ${BLUE} \n[*]Installing Packages, Libraries, and Repos...${NC}\n"
sudo apt-get install figlet netcat hashcat php tshark tcpdump telnet ftp git apache2 ssh arp-scan macchanger hddtemp lm-sensors xterm ettercap-text-only ettercap-graphical build-essential ntfs-3g cifs.utils mount reaver aircrack-ng curl dhcpd isc-dhcp-server hostapd lighttpd unzip xterm pyrit openssl ufw bully pixiewps kismet -y
sudo ufw enable
printf " ${BLUE}[*]Installing Python2 & Python3 Libraries...${NC}\n"
sudo pip install -U -I pyusb
sudo pip install -U platformio
sudo pip install -r requirements2.txt
sudo pip3 install -r requirements3.txt
printf " ${BLUE}[*]Setting Up Snort...${NC}\n"
sudo mkdir snortlogs
sudo apt-get install snort
printf " ${BLUE}[*]Installing and Initializing Mousejack...${NC}\n"
sudo git clone https://github.com/BastilleResearch/mousejack.git
cd mousejack
sudo git submodule init
sudo git submodule update
cd ..
sudo git clone https://github.com/insecurityofthings/jackit.git
cd jackit
sudo pip install -r requirements.txt
sudo pip install -e .
cd ..
printf " ${BLUE}[*]Installing WifiPumpkin3...${NC}\n"
sudo systemctl stop systemd-resolved
sudo curl https://pastebin.com/raw/QEHM8UJb > /etc/systemd/resolved.conf
sudo ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf
sudo systemctl start systemd-resolved
sudo apt-get install python3 libssl-dev libffi-dev build-essential python3-pyqt5 -y
sudo git clone https://github.com/P0cL4bs/wifipumpkin3.git
cd wifipumpkin3
sudo python3 setup.py install
cd ..
printf " ${BLUE}[*]Installing Wifite2...${NC}\n"
sudo git clone https://github.com/derv82/wifite2.git
cd wifite2
sudo python setup.py install
cd ..
printf " ${BLUE}[*]Installing wifijammer...${NC}\n"
sudo git clone https://github.com/DanMcInerney/wifijammer.git
printf " ${BLUE}[*]Installing Pentbox...${NC}\n"
sudo git clone https://github.com/H4CK3RT3CH/pentbox-1.8.git
printf " ${BLUE}[*]Installing Airgeddon...${NC}\n"
sudo git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git
printf " ${BLUE}[*]Installing Fluxion...${NC}\n"
sudo git clone https://github.com/FluxionNetwork/fluxion.git
printf " ${BLUE}[*]Installing PwnStar...${NC}\n"
sudo git clone https://github.com/SilverFoxx/PwnSTAR.git
cd PwnSTAR
sudo chmod 777 installer.sh
sudo ./installer.sh
cd ..
printf " ${BLUE}[*]Installing Linset...${NC}\n"
sudo git clone https://github.com/vk496/linset.git
cd linset
sudo chmod 777 linset
cd ..
printf " ${BLUE}[*]Installing Espionage...${NC}\n"
sudo git clone https://github.com/josh0xA/Espionage
cd Espionage
sudo pip3 install -r requirments.txt
cd ..
sudo apt autoremove
printf " ${BLUE}[*]Installing privoxy...${NC}\n"
sudo apt-get install privoxy
cd /etc/privoxy/
sudo rm config
sudo -u root curl https://pastebin.com/raw/3gyRkyuX > config
sudo service privoxy restart
sudo crontab -l | { cat; echo "@reboot sudo service privoxy start"; } | sudo crontab -
printf " ${GREEN}[+]Privoxy running on port 8118!${NC}\n"
wait_func
printf "${GREEN}[+]Done! ${BLUE} \n[*]Moving NetCrackPi directory to /opt...${NC}\n"
sudo mkdir /opt
cd ..
sudo mv NetCrackPi /opt
printf "${GREEN}[+]Done! ${BLUE} \n[*]Writing network_crack.py to alias...${NC}\n"
sudo echo "alias netcrack='sudo python3 /opt/NetCrackPi/network_crack.py'" >> /home/pi/.bashrc
printf "${GREEN}[+]Done! \n[+]NetCrackPi Setup Complete!${NC}"
