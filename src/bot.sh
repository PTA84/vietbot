#!/bin/bash
sudo chown pi:pi /var/run
#mkdir /var/run/snapclient
cd /home/pi/vietbot
python3 main_process.py
