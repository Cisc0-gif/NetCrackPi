#! /bin/bash
read -p "*RUN AS ROOT*" root
echo "[*]Writing File Permissions..."
sudo chmod -R 777 *
echo "[*]Done!"
echo "[*]Updating and Upgrading Packages..."
sudo apt-get update && sudo apt-get upgrade
echo "[*]Done!"
echo "[*]Making sure pip and pip3 are installed..."
sudo apt-get install python-pip python3-pip
echo "[*]Done!"
echo "[*]Running lib installer..."
sudo ./lib_install.py
echo "[+]Done!"
echo "[*]Moving NetCrackPi directory to /opt..."
sudo mkdir /opt
cd ..
sudo mv NetCrackPi /opt
echo "[+]Done!"
echo "[*]Writing network_crack.py to alias..."
sudo echo "alias NetCrack='sudo python3 /opt/NetCrackPi/network_crack.py'" >> /home/pi/.bashrc
echo "[+]Done!"
echo "[+]NetCrackPi Setup Complete!"
