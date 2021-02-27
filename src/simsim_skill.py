#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import spot

from speaking import short_speak
import random
import gih
import requests, json, os, time, uuid, urllib, datetime   
from termcolor import colored
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH HỎI BẰNG SIMSIM: '+data)
    url = 'https://api.simsimi.net/v1/c3c/?text='+data+'&lang=vi_VN&cf=true&key=API-s2veFgBYjTp7Ww8G-QL2iAVlqUyC3YS9o&author=botname'
    _response = requests.get(url) 
    answer = _response.json()['messages'][0]['response']
    if 'Sim không biết' in answer:
        short_speak('Em không có câu trả lời')
    else:
        short_speak(str(answer))
if __name__ == '__main__':
    main()