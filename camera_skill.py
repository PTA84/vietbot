#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import spot

import speaking

import os
import random
import yaml
import gih

# from pygame import mixer
# mixer.init()
from termcolor import colored
import main_process
import ptz

def main(data):
    list_movement= gih.get_request('request_movement')         
    print('[BOT]: XỬ LÝ CÂU LỆNH ĐIỀU KHIỂN CAMERA: '+data)
    print('---------')
    a=ptz.control(gih.get_configuration('camera_ip'),gih.get_configuration('username'),gih.get_configuration('password'))
    datapreset=data
    datapreset=datapreset.split()
    data = data.upper()
    iiii=0
    while iiii < len(datapreset):
        if datapreset[iiii].isnumeric() ==True:
            preset_number=datapreset[iiii]
            break
        else:
            iiii+=1
    try:
        a.set_preset(preset_number)
    except:
        pass
    if list_movement[0] in data:
        a.len()
        time.sleep(2)
        return
    elif list_movement[1] in data:
        a.xuong()
        time.sleep(2)
        return
    elif list_movement[2] in data:
        a.trai()
        time.sleep(2)
        return
    elif list_movement[3] in data:
        a.phai()
        time.sleep(2)
        return                    
    else:
        pass


if __name__ == '__main__':
    main()