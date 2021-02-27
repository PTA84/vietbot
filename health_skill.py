#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import spot

from speaking import short_speak
import random
import gih

from termcolor import colored
response_health=gih.get_response('response_health')

def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH HỎI THĂM: '+data)
    short_speak(random.choice(response_health))                     

if __name__ == '__main__':
    main()

