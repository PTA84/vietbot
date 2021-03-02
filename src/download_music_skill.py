#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-

#Tạo thư mục mp3 trong thư mục vietbot

import os
from os import listdir
from os import path
import sys
import random
import yaml
import gih
import time
import re
import urllib
import re
import urllib.request
import urllib.parse
import datetime

import youtube_dl
from urllib.request import urlopen
import datetime



#So sánh gần giống 2 chuỗi
from fuzzywuzzy import fuzz

from speaking import speak, short_speak 
from termcolor import colored
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel

import threading

from mutagen.mp3 import MP3


re_speaker= gih.get_config('re_speaker')
volume=gih.get_config('volume')
if re_speaker == 1:
    import pixels
#Điều khiển led-------------
    led_xanh = gih.get_config('led_xanh')
    led_do = gih.get_config('led_do')
    try:
        gpio.init()
        gpio.setcfg(led_xanh, 1)
        gpio.setcfg(led_do, 1)
        pixels.pixels.off()     
    except:
        pass
elif re_speaker == 2:  
    import usb_pixel_ring_v2 as led_control  
    led_control.find().off()
elif re_speaker == 3:
    from pixel_ring import pixel_ring
    pixel_ring.off()

request_download_music=gih.get_request('request_download_music')
mp3_list_files =os.listdir('mp3/')
compare_percent=gih.get_config('compare_percent')
# data ='Anh đừng đi china' 


def main(data):
    run_thread(download_process,data)
def download_process(data):    
    print('[BOT]: XỬ LÝ CÂU LỆNH DOWNLOAD: '+data)    
    if re_speaker == 1:
        pixels.pixels.off() 
    elif re_speaker ==2:
        led_control.find().off()       
    elif re_speaker ==3:    
        pixel_ring.off()                                    
    if data is None:
        pass
    elif data is not None:
        a = 0
        download_command = str([s for s in request_download_music if s in data])
        download_command = download_command.replace("['", "")
        download_command = download_command.replace("']", "") 
        data = data.replace(download_command,'')        
        data = data.upper()
        if len(data) >0:
            for i in mp3_list_files:
                song_title=i.replace('_','')
                song_title=song_title.replace('-','')
                song_title=song_title.replace('-','')                
                song_title=song_title.replace('.mp3','')                
                song_title=song_title.upper()
                match_ratio=fuzz.token_sort_ratio(data, song_title)
                # print(data)
                # print(song_title)
                # print(str(match_ratio))
                if match_ratio > compare_percent:                    
                    a=i
                    break
            if a ==0:
                print('Download nhạc '+data+' xuống thư mục')
                short_speak('Download nhạc '+data+' xuống thư mục')
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
            else:
                print('Nhạc cần download '+data+' có sẵn trong thư mục, quay lại')
                short_speak('Nhạc cần download '+data+' có sẵn trong thư mục, quay lại')
                pass
        else:
            print('Không có tên bài nhạc, quay lại')
            short_speak('Không có tên bài nhạc, quay lại')
            pass        

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



def run_thread(func,data=None):
    if data is not None:
        t = threading.Thread(target = func, args = (data,))
        t.start()
    else:
        t = threading.Thread(target = func, args = ())
        t.start()

def back_to_loop():
    if re_speaker == 1:
        pixels.pixels.off() 
    elif re_speaker ==2:
        led_control.find().off()       
    elif re_speaker ==3:    
        pixel_ring.off()                                    
    loop()

if __name__ == '__main__':
    main(data)