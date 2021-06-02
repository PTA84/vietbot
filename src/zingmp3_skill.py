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
from fuzzywuzzy import fuzz
from termcolor import colored
import numpy as np
import json
# data ='thôi đừng chiêm bao'

def zingmp3_skill(data):
    result=None
    # print("Tìm bài hát: "+data+"...")
    if 'của' in data.lower():
        song = re.split(r"\ của", data.lower())[0]
        artist = re.split(r"\ của", data.lower())[1]
    else: 
        song = data
        artist=''
    try:
        resp = requests.get('http://ac.mp3.zing.vn/complete?type=artist,song,key,code&num=500&query='+urllib.parse.quote(song+" "+artist))
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        song_id=[]
        if len(obj['data']) > 0:
            songs = obj['data'][0]['song']
            for i in range (0,len(songs)):
                if str(songs[i]['name']).lower()==str(song).lower() and str(songs[i]['artist']).lower()==str(artist).lower():
                    song_id.append(songs[i]['id'])      
                elif str(songs[i]['name']).lower()==str(song).lower():
                    song_id.append(songs[i]['id'])
                else:
                    song_id.append(songs[i]['id'])
        else:
            new_song=[]
            lst = data.split()
            for start, end in combinations(range(len(lst)), 2):
                new=lst[start:end+1]
                newlist=' '.join(new)
                new_song.append(newlist)
            try:     
                for i in range (0,len(new_song)): 
                    song = new_song[i]
                    resp = requests.get('http://ac.mp3.zing.vn/complete?type=artist,song,key,code&num=500&query='+urllib.parse.quote(song))
                    resultJson = json.dumps(resp.json())
                    obj = json.loads(resultJson)
                    if len(obj['data']) > 0:
                        songs = obj['data'][0]['song']
                        for i in range (0,len(songs)):
                            if fuzz.ratio(str(songs[i]['name']).lower(),song.lower()) > 70: 
                                song_id.append(songs[i]['id'])
            except (IndexError, ValueError):
                pass
        songID =  np.random.choice(song_id)
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
        print(realURL)
        result=file_name            
    except (IndexError, ValueError):
        pass        
    return result
if __name__ == '__main__':
    zingmp3_skill(data)
