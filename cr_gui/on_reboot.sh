#!/bin/bash

#echo "cazzofiga"
source /home/pi/.profile
#source /home/pi/.bashrc
/home/pi/.virtualenvs/cv/bin/activate
cd /home/pi/MiniVanControlsGUI/cr_gui
/home/pi/.virtualenvs/cv/bin/python gui.py > /home/pi/MiniVanControlsGUI/cr_gui/logs/logs 2>&1

deactivate
cd /home/pi
