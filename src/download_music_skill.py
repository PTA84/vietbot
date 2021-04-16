#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-

#Tạo thư mục mp3 trong thư mục vietbot

import os
from os import listdir
from os import path
import sys
import random
import time
import re
import urllib
# import urllib.request
# import urllib.parse
import datetime
import youtube_dl
from urllib.request import urlopen
import json

def main(data):    
    url = "http://www.youtube.com/watch?v="+get_result(data)
    ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': 'mp3/%(title)s.%(ext)s',
                    'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '128',
                    }],
                }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def get_result(data):

    # data = data.replace(request_music[0],'')
    # data = data.replace(request_music[1],'')
    # data = data.replace(request_music[2],'')   
    data = data.lower()
    query_string = urllib.parse.urlencode({"search_query" : data})
    html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    list_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    # number_songs = len(search_results)
    # random_song=random.randint(0,number_songs)
    # media = search_results[random_song]
    return list_results[0]


# if __name__ == '__main__':
    # main(data)