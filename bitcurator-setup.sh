#!/bin/bash

### Bitcurator setup script
# Tim Walsh - Dec 2017
# Run as sudo

# Install PyQt4
echo "Installing PyQt4..."
sudo apt-get install python-qt4

# Install Siegfried
echo "Installing Siegfried..."
wget -qO - https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
echo "deb http://dl.bintray.com/siegfried/debian wheezy main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update && sudo apt-get install siegfried

# Install Brunnhilde
echo "Installing Brunnhilde..."
sudo pip install brunnhilde

cd /home/bcadmin

# Install Brunnhilde GUI
echo "Installing Brunnhilde GUI..."
git clone https://github.com/timothyryanwalsh/brunnhilde-gui
cd /home/bcadmin/brunnhilde-gui
sudo chmod u+x install.sh
sudo ./install.sh

# Install CCA Tools
sudo mkdir "/home/bcadmin/Desktop/CCA Tools"
# download and install disk image processor
# download and install folder processor
# download and install dfxml reader

# Cleanup folders
echo "Cleaning up folders..."
sudo rm -rf /home/bcadmin/brunnhilde-gui
# add cca tools

# Remind user to update unhfs
echo "Finished. ONE TASK REMAINING: YOU MUST STILL UPDATE HFSEXPLORER! Use this version: https://sourceforge.net/projects/catacombae/files/HFSExplorer/0.23.1%20%28snapshot%202016-09-02%29/"
