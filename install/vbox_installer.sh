#!/usr/bin/env bash
# lubuntu LTS 14.04 VirtualBox installer based on lubuntu-14.04.2-desktop-i386
# computer name: crukci-training-vm; user: training; password: admin123

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

# To increase screen resolution
# Start > Preferences > Additional Drivers: Using x86 virtualization solution... and click Apply Changes
# Then Start > Preferences > Monitor Settings and select 1440x1050 and click Save and Apply

pip install ipython[notebook]

apt-get autoremove
apt-get clean


adduser pycam # password: pycam123

exit

# login as pycam --------------------------------------------------------------

git clone https://github.com/pycam/python-intro.git course

# Add ipython at startup from lubuntu menu do to...
# Preferences > Default applications for LXSession then tab Autostart and add:
# /usr/local/bin/ipython notebook --no-browser --port=8888 --ip=127.0.0.1 /home/pycam/course/

# Add bookmarks into firefox: (1) pycam.github.io (2) 127.0.0.1:8888


