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

cd /home/bcadmin

# Install Brunnhilde
echo "Installing Brunnhilde..."
git clone https://github.com/timothyryanwalsh/brunnhilde
sudo mv brunnhilde/ /usr/share/

# Install Brunnhilde GUI
echo "Installing Brunnhilde GUI..."
git clone https://github.com/timothyryanwalsh/brunnhilde-gui
cd /home/bcadmin/brunnhilde-gui
sudo bash install.sh

# Install CCA Tools
cd /home/bcadmin
echo "Installing CCA Tools..."
git clone https://github.com/timothyryanwalsh/cca-tools
cd cca-tools
sudo bash install.sh

# Remind user to update unhfs
echo "Finished. ONE TASK REMAINING: YOU MUST STILL UPDATE HFSEXPLORER! Use this version: https://sourceforge.net/projects/catacombae/files/HFSExplorer/0.23.1%20%28snapshot%202016-09-02%29/"
