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

# Install Brunnhilde GUI
cd /home/bcadmin
echo "Installing Brunnhilde GUI..."
git clone https://github.com/timothyryanwalsh/brunnhilde-gui
cd /home/bcadmin/brunnhilde-gui
sudo chmod u+x install.sh
sudo ./install.sh

# Download and install CCA Disk Image Processor
cd /home/bcadmin
git clone https://github.com/timothyryanwalsh/cca-diskimageprocessor
cd /home/bcadmin/cca-diskimageprocessor
sudo chmod u+x install.sh
sudo ./install.sh

# Download and install CCA Folder Processor
cd /home/bcadmin
git clone https://github.com/timothyryanwalsh/cca-folderprocessor
cd /home/bcadmin/cca-folderprocessor
sudo chmod u+x install.sh
sudo ./install.sh

# Download and install DFXML Reader
cd /home/bcadmin
git clone https://github.com/timothyryanwalsh/dfxml-reader
cd /home/bcadmin/dfxml-reader
sudo chmod u+x install.sh
sudo ./install.sh

# Create /mnt/diskid/ directory for processing UDF and HFS disks with Disk Image Processor
sudo mkdir /mnt/diskid

# Cleanup folders
echo "Cleaning up folders..."
sudo rm -rf /home/bcadmin/brunnhilde-gui
sudo rm -rf /home/bcadmin/cca-diskimageprocessor
sudo rm -rf /home/bcadmin/cca-folderprocessor
sudo rm -rf /home/bcadmin/dfxml-reader

# Remind user to update unhfs
echo "Finished. ONE TASK REMAINING: YOU MUST STILL UPDATE HFSEXPLORER! Use this version: https://sourceforge.net/projects/catacombae/files/HFSExplorer/0.23.1%20%28snapshot%202016-09-02%29/"
