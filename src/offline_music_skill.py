#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-


import os
from os import listdir
from os import path
import sys
import random
import time

import datetime

from termcolor import colored
#STT Engine

import threading

#Play Audio và đọc file MP3
import pygame
from pygame import mixer
from mutagen.mp3 import MP3
mixer.init()

#Gọi Hotword
import pyaudio
import struct
import pvporcupine

import importlib

import json


with open('config.json') as config_json:
    config_data = json.load(config_json)
with open('request.json') as request_json:
    request_data = json.load(request_json)
with open('response.json') as response_json:
    response_data = json.load(response_json)
led_off_mode=None
led_off_color=None
led_wakeup_mode=None
led_wakeup_color=None

for p in config_data['mic']:
    if p['type'] == 'ReSpeaker 2/4-Mics Pi HAT':
        if p['is_active'] == True:
            import pixels
        else:
            pass
    elif p['type'] == 'ReSpeaker Mic Array v2.0':
        if p['is_active'] == True:
            import respeaker_usb_led as led_control
            led_off_mode=p['led_off_mode']
            led_off_color=p['led_off_color']
            led_wakeup_mode=p['led_wakeup_mode']
            led_wakeup_color=p['led_wakeup_color']            
        else:
            pass
    elif p['type'] == 'ReSpeaker Core v2.0':
        if p['is_active'] == True:
            from pixel_ring import pixel_ring
    else:
        pass

    event_volume=0.5
    speak_volume=0.5
    playback_volume=0.5    
    for p in config_data['volume']:
        # print('Loại Mic: ' + p['type'])
        if p['type'] == 'event':
            event_volume= p['value']
        if p['type'] == 'speak':
            speak_volume= p['value']
        if p['type'] == 'playback':
            playback_volume= p['value']    

    for p in config_data['tts_engine']:
        # print('Loại Mic: ' + p['type'])
        if p['is_active'] == True:
            tts_engine=importlib.import_module(p['name'])
            if p['name'] == 'tts_gg_cloud':
                ggcre = p['token_file']
                os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre

    stt_engine= None

    ggcre =''
    for p in config_data['stt_engine']:
        # print('Loại Mic: ' + p['type'])
        if p['is_active'] == True:
            stt_engine=importlib.import_module(p['name'])
            if p['name'] == 'stt_gg_cloud':
                ggcre = p['token_file']
                os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre

keyword_paths =[]
sensitivities =[]

for p in config_data['hotword']:
    if p['is_active']:
        keyword_paths.append(p['keyword_path'])
        sensitivities.append(p['sensitive'])

def offline_music_skill_led_off():
    for p in config_data['mic']:
        if p['type'] == 'ReSpeaker 2/4-Mics Pi HAT':
            if p['is_active'] == True:
                pixels.pixels.off()
            else:
                pass
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            if p['is_active'] == True:
                if led_off_mode==1:
                    led_control.find().off(None)
                elif led_off_mode==2:
                    led_control.find().off(led_off_color)
                    # led_control.find().mono()
            else:
                pass
        elif p['type'] == 'ReSpeaker Core v2.0':
            if p['is_active'] == True:
                pixel_ring.off()
        else:
            pass                

def offline_music_skill_led_wakeup():
    for p in config_data['mic']:
        if p['type'] == 'ReSpeaker 2/4-Mics Pi HAT':    
            if p['is_active'] == True:
                pixels.pixels.wakeup()
            else:
                pass
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            if p['is_active'] == True:
                if led_wakeup_mode==1:            
                    led_control.find().wakeup(None)
                elif led_wakeup_mode==2:
                    led_control.find().wakeup(led_wakeup_color)
                    # led_control.find().mono(led_wakeup_color)                    
            else:
                pass
        elif p['type'] == 'ReSpeaker Core v2.0':
            if p['is_active'] == True:
                pixel_ring.wakeup()
        else:
            pass        

def offline_music_skill_led_think():
    for p in config_data['mic']:
        if p['type'] == 'ReSpeaker 2/4-Mics Pi HAT':    
            if p['is_active'] == True:
                pixels.pixels.think()
            else:
                pass
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            if p['is_active'] == True:
                led_control.find().think()
            else:
                pass
        elif p['type'] == 'ReSpeaker Core v2.0':
            if p['is_active'] == True:
                pixel_ring.think()
        else:
            pass        

def offline_music_skill_led_speak():
    for p in config_data['mic']:
        if p['type'] == 'ReSpeaker 2/4-Mics Pi HAT':    
            if p['is_active'] == True:
                pixels.pixels.speak()
            else:
                pass
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            if p['is_active'] == True:
                led_control.find().speak()
            else:
                pass
        elif p['type'] == 'ReSpeaker Core v2.0':
            if p['is_active'] == True:
                pixel_ring.speak()
        else:
            pass            

request_incrase_volume =[]
request_decrase_volume =[]
request_reply =[]
request_pause =[]
request_continue =[]
request_exit=[]

for p in request_data['incrase_volume']:
    if p['is_active']:
        request_incrase_volume.append(p['content'])
for p in request_data['decrase_volume']:
    if p['is_active']:
        request_decrase_volume.append(p['content'])
for p in request_data['reply']:
    if p['is_active']:
        request_reply.append(p['content'])
for p in request_data['pause']:
    if p['is_active']:
        request_pause.append(p['content'])
for p in request_data['continue']:
    if p['is_active']:
        request_continue.append(p['content'])
for p in request_data['exit']:
    if p['is_active']:
        request_exit.append(p['content'])

# def newest(path):
    # files = os.listdir(path)
    # paths = [os.path.join(path, basename) for basename in files]
    # return max(paths, key=os.path.getctime)

def offline_music_skill(data):

    offline_music_skill_run_thread(offline_music_skill_playback,data)
    time.sleep(1)
    offline_music_skill_loop()
    
def offline_music_skill_playback(data):    

    global player
    player = mixer.music
    player.load('mp3/'+data)
    player.set_volume(playback_volume)            
    offline_music_skill_led_speak()
    player.play()
    audio = MP3('mp3/'+data)
    t = float (audio.info.length)
    print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)                                
    offline_music_skill_led_off()
    deamon = False
    return player
def offline_music_skill_loop():    
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
    while str(player.get_busy()) =='1':      
        # pcm = audio_stream.read(512)
        pcm = audio_stream.read(512,exception_on_overflow=False)                
        exception_on_overflow = False
        pcm = struct.unpack_from("h" * 512, pcm)
        keyword_index = porcupine.process(pcm)
        # print(str(keyword_index))
        if keyword_index >= 0:
            offline_music_skill_led_wakeup()
            # play_ding()
            # print('[BOT]: Phát hiện khẩu lệnh đúng '+ keywords[keyword_index] +'xin mời ra lệnh')
            porcupine.delete()
            pa.terminate()
            audio_stream.close()
            offline_music_skill_control()
            break
    else: 
        offline_music_skill_led_speak()
        tts_engine.short_speak('Đã phát nhạc xong')        
        offline_music_skill_led_off()
        daemon = False
        pass            
def offline_music_skill_control():           
    current_volume = player.get_volume()
    player.pause()                
    data = None
    for p in config_data['stt_engine']:
        # print('Loại Mic: ' + p['type'])
        if p['is_active'] == True:
            if p['name'] == 'stt_gg_cloud':
                data = stt_engine.stt_viettel()
            elif p['name'] == 'stt_viettel':
                data = stt_engine.stt_viettel()                
            elif p['name'] == 'stt_fpt':
                data = stt_engine.stt_fpt()                   
            elif p['name'] == 'stt_gg_ass':
                data = stt_engine.stt_gg_ass()                   
            elif p['name'] == 'stt_gg_free':
                data = stt_engine.main()                   
    if data is not None:
        data = data.lower()        
        if any(item in data for item in request_incrase_volume):         
            if player.get_volume() <0.7:
                new_volume = player.get_volume()+0.3
                player.set_volume(new_volume)                
                #run_thread(speak,'Giá trị âm lượng hiện tại là: '+str(player.get_volume()))                        
                player.unpause()
                offline_music_skill_callback
                pass
            else:
                player.set_volume(1.0)                
                player.unpause()                    
                #run_thread(speak,'Giá trị âm lượng hiện tại là: '+str(player.get_volume()))                                                
                offline_music_skill_callback
                pass
        elif any(item in data for item in request_decrase_volume):         
            if player.get_volume() >0.3:
                new_volume = player.get_volume()-0.3
                player.set_volume(new_volume)                
                player.unpause()                    
                #run_thread(speak,'Giá trị âm lượng hiện tại là: '+str(player.get_volume()))                                                
                offline_music_skill_callback
                pass                        
            else:
                player.set_volume(0.1)                
                player.unpause()                    
                #run_thread(speak,'Giá trị âm lượng hiện tại là: '+str(player.get_volume()))                                                
                offline_music_skill_callback
                pass                        
        elif any(item in data for item in request_reply): 
            player.rewind()                
            offline_music_skill_callback                
            pass                
        elif any(item in data for item in request_pause): 
            player.pause()
            offline_music_skill_callback
            pass                                
        elif any(item in data for item in request_continue): 
            player.unpause()
            offline_music_skill_callback
            pass                                
        elif any(item in data for item in request_exit): 
            player.stop()
            daemon = False                                
            pass                                
        else:
            player.set_volume(current_volume)            
            player.unpause()
            offline_music_skill_callback
            pass                
    else:
        player.set_volume(current_volume)
        player.unpause()
        offline_music_skill_callback
        pass


def offline_music_skill_callback():
    offline_music_skill_dong()
    offline_music_skill_led_off()
    offline_music_skill_loop()
def offline_music_skill_ding():
    mixer.music.load('resources/ding.wav')
    mixer.music.set_volume(event_volume)
    mixer.music.play()
    # sound = AudioSegment.from_mp3('resources/ding.wav')
    # play(sound)
def offline_music_skill_dong():
    mixer.music.load('resources/dong.wav')
    mixer.music.set_volume(event_volume)
    mixer.music.play()


def offline_music_skill_run_thread(func,data):
    t = threading.Thread(target = func, args = (data,), daemon = True) 
    t.start()
    # t.join()


# if __name__ == '__main__':
    # offline_music_skill(data)
