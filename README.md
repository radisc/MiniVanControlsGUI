# MiniVanControlsGUI
graphical gui to control AC, door and lights in a minivan

Configuration
1) Configure "cv" python virtual environment in home folder with the required python libraries 

To autostart at Rpi boot, add to "/home/pi/.config/lxsession/LXDE-pi/autostart" the line

@bash -c /home/pi/MiniVanControlsGUI/cr_gui/on_reboot.sh
