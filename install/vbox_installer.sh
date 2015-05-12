#!/usr/bin/env bash
# PyCam ubuntu installer

sudo su -
apt-get install gedit
apt-get install git
apt-get install python-pip
apt-get install python-zmq
apt-get install python-matplotlib
apt-get install python-biopython

apt-get install virtualbox-guest-utils
apt-get install dkms

pip install ipython[notebook]

apt-get autoremove
apt-get clean
exit

git clone https://github.com/pycam/python-intro.git course
