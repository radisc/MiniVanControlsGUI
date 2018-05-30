#!/bin/bash

#echo "cazzofiga"
source /home/pi/.profile
source /home/pi/.bashrc
#/home/pi/.virtualenvs/cv/bin/activate
workon cv
cd /home/pi/MiniVanControlsGUI/cr_gui
/home/pi/.virtualenvs/cv/bin/python2 gui.py > /home/pi/MiniVanControlsGUI/cr_gui/logs/logs 2>&1

#deactivate
cd /home/pi
