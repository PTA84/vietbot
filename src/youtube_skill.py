#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-


import os
from os import listdir
from os import path
import sys
import time
import re
import datetime
import requests
import json
import urllib
import re
import pafy
from termcolor import colored


def main(data):
    file_name=None
    print("Tìm bài hát: "+data+"...")
    data = data.lower()
    query_string = urllib.parse.urlencode({"search_query" : data})
    html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    list_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    url = "http://www.youtube.com/watch?v="+list_results[0]
    info = pafy.new(url)
    title = info.title
    file_name_m4a ='/tmp/'+data+'.m4a'
    file_name_mp3 ='mp3/'+data+'.mp3'            
    audio = info.m4astreams[-1]
    audio = info.getbestaudio(preftype="m4a")
    audio.download(file_name_m4a, quiet=True)
    ouput=None
    try:
        track = AudioSegment.from_file(file_name_m4a,'m4a')
        print('CONVERTING: ' + str(title))
        file_handle = track.export(file_name_mp3, format='mp3')
        file_name = file_name_mp3
    except:
        print("ERROR CONVERTING " + str(file_name_m4a))
    return file_name


# if __name__ == '__youtube_skill__':
    # main(data)
