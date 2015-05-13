#!/usr/bin/env bash
# PyCam lubuntu LTS 14.04 VirtualBox installer based on lubuntu-14.04.2-desktop-i386

sudo su -
apt-get install gedit
apt-get install vim
apt-get install git
apt-get install python-pip
apt-get install python-zmq
apt-get install python-matplotlib
apt-get install python-biopython
apt-get install ncbi-blast+

# Install VirtualBox Additions
# From the VirtualBox menu of lubuntu go to Devices > Insert Guest Additions CD image... and do
cd /media/training/VBOXADDITIONS_4.3.26_98988
sudo ./VBoxLinuxAdditions.run

pip install ipython[notebook]

apt-get autoremove
apt-get clean
exit

git clone https://github.com/pycam/python-intro.git course

# Add ipython at startup from lubuntu menu do to...
# Preferences > Default applications for LXSession then tab Autostart and add:
# /usr/local/bin/ipython notebook --no-browser --port=8888 --ip=127.0.0.1 /home/training/course/