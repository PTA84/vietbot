#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-

import os
from os import listdir
from os import path
import sys
import random
import time
import requests
import json
import urllib
import re
import random
import datetime
from urllib.request import urlretrieve

from termcolor import colored

import json
# data ='thôi đừng chiêm bao'

def zingmp3_skill(data):
    result=None
    # print("Tìm bài hát: "+data+"...")
    try:
        resp = requests.get('http://ac.mp3.zing.vn/complete/desktop?type=song&query='+urllib.parse.quote(data))
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        songID = obj["data"][1]['song'][0]['id']
        songUrl= "https://mp3.zing.vn/bai-hat/"+songID+".html"
        # print(songUrl)
        resp = requests.get(songUrl)
        # print(resp.text)
        key = re.findall('data-xml="\/media\/get-source\?type=audio&key=([a-zA-Z0-9]{20,35})', resp.text)
        # key = re.findall('data-xml="\/media\/get-source\?type=video&key=([a-zA-Z0-9]{20,35})', resp.text)
        songApiUrl = "https://mp3.zing.vn/xhr/media/get-source?type=audio&key="+key[0]
        resp = requests.get(songApiUrl)
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        # print(str(obj))
        mp3Source = "https:"+obj["data"]["source"]["128"]
        realURLdata = requests.get(mp3Source,allow_redirects=False)
        # print(realURLdata)
        realURL = realURLdata.headers['Location']
        file_name, headers = urlretrieve(realURL)
        # print(realURL)
        result=file_name            
    except (IndexError, ValueError):
        pass        

    return result
if __name__ == '__main__':
    zingmp3_skill(data)
