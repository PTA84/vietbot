# !/usr/bin/python
# coding=utf-8

import pdb
try:
    from pyA20.gpio import gpio
    from pyA20.gpio import port
except:
    pass
#--------------------------
# CÁC MODULE SẴN CÓ
# import logging
import datetime
from datetime import datetime
from datetime import date
from datetime import time
import time
import re
# os.environ["DISPLAY"] = ":0"
import sys
import json
import os
import yaml
# import snowboydecoder
import signal
# import vlc
import datefinder
global ok
# import speech_recognition as sr
# import feedparser
#import numpy as np
import re
import pyaudio
from mutagen.mp3 import MP3
# from underthesea import sent_tokenize as sent
# import wave
import gih
# import numpy as np
import threading
import struct
import pvporcupine
import random
from termcolor import colored
#Play Audio lib
# import pyaudio
from pygame import mixer
# from pydub import AudioSegment                
# from pydub.playback import play
#Read config
import gih
import requests
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
#TTS Engine
import speaking
from speaking import speak, short_speak

#Other Skill
import greeting_skill
import health_skill
import weather_skill
import news_skill
import wikipedia_skill
import lunar_calendar_skill
import name_day_skill
import time_skill
# import camera_skill
import holiday_skill
import lottery_skill
import youtube_skill
import translate_word_skill
import translate_sentense_skill
import random_number_skill
import exchange_rate_skill
import gold_rate_skill
import speedtest_skill
import wikipedia_skill
import google_answer_skill
import simsim_skill
import wishes_skill
import music_offline_skill
import download_music_skill
import funny_story_skill
import spotify_skill
import google_ass_skill
re_speaker= gih.get_config('re_speaker')
mixer.init()
if re_speaker == 1:
    import RPi.GPIO as GPIO

    # Popen(['amixer', 'set', 'Speaker', "30"])
    # from gpiozero import Button
    # from signal import pause    


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
#Read config
domain = gih.get_config('hass_url')
longlivedtoken = gih.get_config('hass_token')
volume=gih.get_config('volume')
reminder = gih.get_config('reminder')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
stt_engine= gih.get_config('stt_engine')
# wakeup_engine =gih.get_config('wakeup_engine')
# keywords =gih.get_config('keywords')
sensitivities =gih.get_config('sensitivities')
keyword_paths=gih.get_config('keyword_paths')
# hotword=gih.get_config('hotword')
# model = gih.get_config('model')
# sensitivity = gih.get_config('sensitivity')
voice = gih.get_config('voice')
music_source= gih.get_config('music_source')
use_hass = gih.get_config('use_hass')
use_external_answer = gih.get_config('use_external_answer')
#Spotify
# if music_source == 1:
    # import spotify_skill
    # spotify_username = gih.get_config('spotify_username')
    # spotify_client_id = gih.get_config('spotify_client_id')
    # spotify_client_secret = gih.get_config('spotify_client_secret')
    # spotify_redirect_url = gih.get_config('spotify_redirect_url')
    # spotipy=spotify_skill.assign()
hass_online = False
if use_hass == 1:
    print(colored('[BOT]: KẾT NỐI - trung tâm điều khiển nhà tại địa chỉ: '+ domain,'yellow'))
    con1 = gih.data_init()
    con_command = gih.data_command_init()
    r=''
    url = domain+ '/api/states'
    headers = {'Authorization': 'Bearer '+ longlivedtoken,'content-type': 'application/json',}
    time.sleep(0.1)
    try:
        r = requests.get(url,headers = headers)
    except:
        hass_online = False
        mixer.music.load('resources/dong.wav')
        mixer.music.set_volume(volume)                
        mixer.music.play()    
        print(colored('[BOT LỖI]: Không kết nối trung tâm điều khiển nhà tại địa chỉ '+ domain,'red'))
        short_speak("Không kết nối được trung tâm điều khiển nhà")    
        print(colored('[BOT BỎ QUA] Hoạt động ở chế độ không điều khiển nhà thông minh','orange'))
        pass
    if str(r)=='<Response [200]>':
        hass_online = True
        mixer.music.load('resources/ding.wav')
        mixer.music.set_volume(volume)                
        mixer.music.play()    
        print(colored('[BOT THÀNH CÔNG] Kết nối trung tâm điều khiển nhà.','green'))
        short_speak('Kết nối thành công trung tâm điều khiển nhà')            
        r = r.json()
        i = 0
        while i < len(r)-1 :
            i += 1
            x = r[i]
            y = x['entity_id']
            y = y.split('.')
            entity_id_ex = y[1]
            domain_ex = y[0]
            y = x['attributes']
            try:
                friendly_name_ex = y['friendly_name'].strip()
            except:
                friendly_name_ex =""
                pass
            if domain_ex == 'script' or domain_ex == 'light' or domain_ex == 'switch' or domain_ex=='sensor' or domain_ex =='binary_sensor' or domain_ex =='media_player' or domain_ex =='cover' or domain_ex =='input_select' or domain_ex =='alarm_control_panel' or domain_ex =='climate' or domain_ex =='device_tracker' or domain_ex == 'automation' or domain_ex == 'scene' :
                pre_write_data = (entity_id_ex, domain_ex, friendly_name_ex)
                
                with con1:
                    cur = con1.cursor()
                    cur.execute("INSERT INTO HASSINFO VALUES(?,?,?)",pre_write_data)
        time.sleep(0.5)

        import hass_skill
        request_on = gih.get_request('request_on')
        request_off= gih.get_request('request_off')    
        request_all = gih.get_request('request_all')    
        request_check= gih.get_request('request_check')    
        request_setup= gih.get_request('request_setup')        
        # request_play= gih.get_request('request_play')    
        request_schedule= gih.get_request('request_schedule')    
        request_input= gih.get_request('request_input')        
        request_light = gih.get_request('request_light')
        request_switch = gih.get_request('request_switch')
        request_socket = gih.get_request('request_socket')
        request_fan = gih.get_request('request_fan')
        request_curtain = gih.get_request('request_curtain')
        # request_television = gih.get_request('request_television')    
        request_temperature = gih.get_request('request_temperature')        
        request_humidity = gih.get_request('request_humidity')         
        request_input = gih.get_request('request_input')             
        request_script = gih.get_request('request_script')    
        request_automation = gih.get_request('request_automation')    
        request_scene = gih.get_request('request_scene')            
        response_timeout=gih.get_response('response_timeout')        
    else:
        hass_online = False
        mixer.music.load('resources/dong.wav')
        mixer.music.set_volume(volume)                
        mixer.music.play()    
        print(colored('[BOT LỖI]: Không kết nối trung tâm điều khiển nhà tại địa chỉ '+ domain,'red'))
        short_speak("Không kết nối được trung tâm điều khiển nhà")    
        print(colored('[BOT BỎ QUA] Hoạt động ở chế độ không điều khiển nhà thông minh','orange'))
        pass
    #Hass Skill

request_greeting = gih.get_request('request_greeting')
request_health = gih.get_request('request_health')
request_weather = gih.get_request('request_weather')
request_day = gih.get_request('request_day')            
request_news = gih.get_request('request_news')
request_wikipedia = gih.get_request('request_wikipedia')
request_lunar_calendar = gih.get_request('request_lunar_calendar')
request_name_day = gih.get_request('request_name_day')
request_time = gih.get_request('request_time')
request_camera = gih.get_request('request_camera')
request_holiday = gih.get_request('request_holiday')
request_lottery = gih.get_request('request_lottery')            
request_music = gih.get_request('request_music')            
request_download_music = gih.get_request('request_download_music')            
request_offline = gih.get_request('request_offline')            
request_online = gih.get_request('request_online')            
request_translate_word = gih.get_request('request_translate_word')
request_translate_sentense = gih.get_request('request_translate_sentense')
request_funny_story = gih.get_request('request_funny_story')    
request_random_number = gih.get_request('request_random_number')            
request_exit = gih.get_request('request_exit')                           
request_exchange_rate = gih.get_request('request_exchange_rate')
request_gold_rate = gih.get_request('request_gold_rate')
request_speedtest = gih.get_request('request_speedtest')
request_wishes = gih.get_request('request_wishes')
response_timeout=gih.get_response('response_timeout')        
# spotify = gih.get_config('spotify')
# import spot
   
# spotify_username = gih.get_config('spotify_username')
# spotify_client_id = gih.get_config('spotify_client_id')
# spotify_client_secret = gih.get_config('spotify_client_secret')
# spo=spot.spo(spotify_username,spotify_client_id,spotify_client_secret,'http://localhost:9999/')
# spotipy=spo.assign()

def loop():
    print(colored('[BOT]: CHỜ RA LỆNH...','green'))
    porcupine = None
    pa = None
    audio_stream = None    
    # try:
        # porcupine = pvporcupine.create(keywords=keywords,sensitivities=sensitivities)
    porcupine = pvporcupine.create(keyword_paths=keyword_paths,sensitivities=sensitivities)        
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=512)
    # short_speak(random.choice(list_response_ask_wakeup))           

    while True:      
        # pcm = audio_stream.read(512)
        pcm = audio_stream.read(512,exception_on_overflow=False)                
        exception_on_overflow = False
        pcm = struct.unpack_from("h" * 512, pcm)
        keyword_index = porcupine.process(pcm)
        # print(str(keyword_index))
        if keyword_index >= 0:
            if re_speaker == 1:
                pixels.pixels.wakeup() 
            elif re_speaker ==2:
                led_control.find().wakeup()
            elif re_speaker ==3:    
                pixel_ring.wakeup()                    
            play_ding()
            # print('[BOT]: Phát hiện khẩu lệnh đúng '+ keywords[keyword_index] +'xin mời ra lệnh')
            porcupine.delete()
            pa.terminate()
            audio_stream.close()
            process()
            break
def getText():
    #time.sleep(1)
#   Dùng STT Google Free
    if stt_engine == 0:
        data=input("Nhập lệnh cần thực thi:  ")
    elif stt_engine == 1:
        print(colored('---------------DÙNG STT GOOGLE FREE-----------------------','red'))
        data = stt_gg_free.main() 
#   Dùng STT Google Cloud
    elif stt_engine == 2:
        print(colored('---------------DÙNG STT GOOGLE CLOUD-----------------','green'))
        data = stt_gg_cloud.main()
#   Dùng STT VTCC
    elif stt_engine == 3:
        print(colored('---------------DÙNG STT VIETTEL-------------','blue'))        
        data = stt_viettel.main()        
    elif stt_engine == 4:
        print(colored('---------------DÙNG STT VIETTEL-------------','blue'))        
        data = stt_viettel_test.main()
#   Dùng STT FPT
    elif stt_engine == 5:
        print(colored('---------------DÙNG STT FPT-------------','yellow'))
        data = stt_fpt.py.main()
#   Sử dụng text input

    return data

def process():    
    data = getText()
    if data is None: 
        short_speak(random.choice(response_timeout))     
        back_to_loop()                
        pass
    #elif data == 1: 
        #back_to_loop()                
        #pass
    # print('[BOT] - XỬ LÝ YÊU CẦU')          
    if re_speaker == 1:
        pixels.pixels.think() 
    elif re_speaker ==2:
        led_control.find().think()       
    elif re_speaker ==3:    
        pixel_ring.think()                            
    data = str(data).upper()
    if use_hass ==1 and hass_online == True:
        if any(item in data for item in request_on):
            if any(item in data for item in request_all):
                print('[BOT]:-------------Xử lý câu lệnh mở tất cả thiết bị---------------')                
                if any(item in data for item in request_light):
                    hass_skill.on_off_all_1('light','đèn','on')
                    back_to_loop()            
                elif any(item in data for item in request_switch):
                    hass_skill.on_off_all_1('switch','công tắc','on')
                    back_to_loop()                        
                elif any(item in data for item in request_socket):
                    hass_skill.on_off_all_1('socket','ổ cắm','on')
                    back_to_loop()                        
                elif any(item in data for item in request_fan):
                    hass_skill.on_off_all_1('fan','quạt','on')
                    back_to_loop()                        
                elif any(item in data for item in request_curtain):
                    hass_skill.on_off_all_2('rèm','on')
                    back_to_loop()
                else:
                    short_speak('Yêu cầu không đúng tên thiết bị, yêu cầu lại anh nhé')
                    back_to_loop()                  
            else:
                print('[BOT]:-------------Xử lý câu lệnh mở thiết bị---------------')                
                hass_skill.on_off(data,'on')
                back_to_loop()            
        elif any(item in data for item in request_off):
            if any(item in data for item in request_all):
                print('[BOT]:-------------Xử lý câu lệnh tắt tất cả thiết bị---------------')                
                if any(item in data for item in request_light):
                    hass_skill.on_off_all_1('light','đèn','off')
                    back_to_loop()            
                elif any(item in data for item in request_switch):
                    hass_skill.on_off_all_1('switch','công tắc','off')
                    back_to_loop()                        
                elif any(item in data for item in request_socket):
                    hass_skill.on_off_all_1('socket','ổ cắm','off')
                    back_to_loop()                        
                elif any(item in data for item in request_fan):
                    hass_skill.on_off_all_1('fan','quạt','off')
                    back_to_loop()                        
                elif any(item in data for item in request_curtain):
                    hass_skill.on_off_all_2('rèm','off')
                    back_to_loop()                        
                else:
                    short_speak('Yêu cầu không đúng tên thiết bị, yêu cầu lại anh nhé')
                    back_to_loop()                  
            else:
                print('[BOT]:-------------Xử lý câu lệnh tắt thiết bị---------------')                
                hass_skill.on_off(data,'off')
                back_to_loop()            
        elif any(item in data for item in request_check):
            print('[BOT]:-------------Xử lý câu lệnh kiểm tra một thiết bị---------------')        
            hass_skill.trangthai(data)
            back_to_loop()          
#Skill chào
    if any(item in data for item in request_greeting):
        greeting_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill hỏi thăm
    elif any(item in data for item in request_health):
        health_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill thời tiết
    elif any(item in data for item in request_weather):
        weather_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill tin tức                   
    elif any(item in data for item in request_news):
        news_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill Lịch âm                   
    elif any(item in data for item in request_lunar_calendar):
        lunar_calendar_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill Thứ                   
    elif any(item in data for item in request_name_day):
        name_day_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill Giờ                   
    elif any(item in data for item in request_time):
        time_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill Camera                   
    elif any(item in data for item in request_camera):
        camera_skill.main(data)
        back_to_loop()
        pass                
#Skill Exchange Rate                
    elif any(item in data for item in request_exchange_rate):
        exchange_rate_skill.main(data)
        back_to_loop()
        pass                
#Skill Gold Rate                
    elif any(item in data for item in request_gold_rate):
        gold_rate_skill.main(data)
        back_to_loop()
        pass                        
#Skill Holiday                   
    elif any(item in data for item in request_holiday):
        holiday_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill Lottery                   
    elif any(item in data for item in request_lottery):
        lottery_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill SpeedTest                   
    elif any(item in data for item in request_speedtest):
        speedtest_skill.main(data)
        back_to_loop()
        pass                                                                                
#Skill Download Music  
    elif any(item in data for item in request_download_music):
        download_music_skill.main(data)
        back_to_loop()                            
        pass                                                                                        
#Skill Music  
    elif any(item in data for item in request_music):
        if music_source == 1:
            youtube_skill.main(data)
            back_to_loop()                
        elif music_source == 2:
            spotify_skill.main(data)
            back_to_loop()                
#Skill translate Word
    elif any(item in data for item in request_translate_word):
        translate_word_skill.main(data)
        back_to_loop()
        pass                                                                                    
#Skill translate Word
    elif any(item in data for item in request_translate_sentense):
        translate_sentense_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill Truyện cười  
    elif any(item in data for item in request_funny_story):
        funny_story_skill.main(data)
        back_to_loop()
        pass                                                                        
    elif any(item in data for item in request_exit):
        back_to_loop()
        pass                
#Skill Random Number
    elif any(item in data for item in request_random_number):
        random_number_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill Wikipedia
    elif any(item in data for item in request_wikipedia):
        wikipedia_skill.main(data)
        back_to_loop()
        pass                                                                        
#Skill Wishes
    elif any(item in data for item in request_wishes):
        wishes_skill.main(data)
        back_to_loop()
        pass                                                                                
    elif any(item in data for item in request_exit):
        back_to_loop()
        pass                
    else:
        #Skill Google Ass           
        if use_external_answer == 1:            
            google_ass_skill.google_ass_skill_main(data)            
            back_to_loop()
            pass                 
        if use_external_answer == 2:
        #Skill Google Answer
            google_answer_skill.main(data)
            back_to_loop()
            pass                                                                        
        #Skill SIM SIM            
        elif use_external_answer == 3:            
            simsim_skill.main(data)            
            back_to_loop()
            pass              
        # short_speak('Yêu cầu không đúng vào chủ đề, yêu cầu lại anh nhé')
        # back_to_loop()
        # pass              
def back_to_loop():
    play_dong()
    if re_speaker == 1:
        pixels.pixels.off() 
    elif re_speaker ==2:
        led_control.find().off()       
    elif re_speaker ==3:    
        pixel_ring.off()                                    
    loop()
def play_ding():
    mixer.music.load('resources/ding.wav')
    mixer.music.set_volume(volume)                
    mixer.music.play()    
    # sound = AudioSegment.from_mp3('resources/ding.wav')
    # play(sound)                                
def play_dong():
    mixer.music.load('resources/dong.wav')
    mixer.music.set_volume(volume)                
    mixer.music.play()    
    # sound = AudioSegment.from_mp3('resources/dong.wav')
    # play(sound)         
    


def check_internet(url='http://www.google.com/', timeout=5):
    try:
        t = requests.get(url, timeout=timeout)
    except requests.ConnectionError:
        speaking.short_speak('Không kết nối được với internet')
        pass

def volume_button():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON, GPIO.IN)    
    BUTTON = 17     
    m = alsaaudio.Mixer()    
    m.setvolume(30)    
    while True:
        state = GPIO.input(BUTTON)        
        if state:
            current_vol = m.getvolume()[0]
            if current_vol >= 0 and current_vol < 100:            
                if state:
                    current_vol = current_vol + 20
            elif current_vol == 100:            
                if state:
                    current_vol = current_vol - 20
        else:
            pass
        time.sleep(1)    
        
def main():
    check_internet()
    print('------------------------------------------------------------------------------')
    speaking.short_speak('Xin chào')
    speaking.short_speak('Trợ lý ảo cho nhà thông minh. Sẵn sàng chờ lệnh')
    loop()    
    if re_speaker == 1:
        run_thread(volume_button)    
    
if __name__ == '__main__':
    main()

