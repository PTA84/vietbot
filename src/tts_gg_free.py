import gih
# import os
# import time
# import wget
from gtts import gTTS
from pygame import mixer
mixer.init()
# from os import path
# import re
import io
from termcolor import colored
from mutagen.mp3 import MP3
import json

with open('config.json') as config_json:
    config_data = json.load(config_json)

for p in config_data['mic']:
    # print('Loại Mic: ' + p['type'])
    if p['type'] == 'ReSpeaker 2-Mics Pi HAT':
        import pixels
        pixels.pixels.off()
    elif p['type'] == 'ReSpeaker Mic Array v2.0':
        import usb_pixel_ring_v2 as led_control
        led_control.find().off()
    elif p['type'] == 'ReSpeaker Core v2.0':
        from pixel_ring import pixel_ring
        pixel_ring.off()
    else:
        pass        
speak_volume=1.0
for p in config_data['volume']:
    if p['type'] == 'speak':
        speak_volume= p['value']
        
def speak(text):
    import time
    print(colored('[BOT-TTS-Google Free]: '+text,'green'))
    # mixer.init(54000, -16, 1, 4096)
    tts = gTTS(text,lang = 'vi')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    t = mp3_fp.truncate()/5000
    t = float(t)
    print ('Time delay: '+str(t))
    for p in config_data['mic']:
        # print('Loại Mic: ' + p['type'])
        if p['type'] == 'ReSpeaker 2-Mics Pi HAT':
            pixels.pixels.speak()
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            led_control.find().speak()
        elif p['type'] == 'ReSpeaker Core v2.0':
            pixel_ring.speak()
        else:
            pass        
    mixer.music.load(mp3_fp)
    mixer.music.set_volume(speak_volume)            
    mixer.music.play()
    time.sleep(round(t)+1)
    mp3_fp.flush()
    mp3_fp.seek(0)        
    for p in config_data['mic']:    
        if p['type'] == 'ReSpeaker 2-Mics Pi HAT':
            pixels.pixels.off()
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            led_control.find().off()
        elif p['type'] == 'ReSpeaker Core v2.0':
            pixel_ring.off()
        else:
            pass                                                    
def short_speak(text):
    import time
    # mixer.init(54000, -16, 1, 4096)
    print(colored('[BOT-TTS-Google Free]: '+text,'green'))
    tts = gTTS(text,lang = 'vi')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    t = mp3_fp.truncate()/5000
    t = float(t)
    print ('Time delay: '+str(t))
    mp3_fp.seek(0)
    for p in config_data['mic']:
        # print('Loại Mic: ' + p['type'])
        if p['type'] == 'ReSpeaker 2-Mics Pi HAT':
            pixels.pixels.speak()
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            led_control.find().speak()
        elif p['type'] == 'ReSpeaker Core v2.0':
            pixel_ring.speak()
        else:
            pass                                        
    mixer.music.load(mp3_fp)
    mixer.music.set_volume(speak_volume)            
    mixer.music.play()             
    audio = MP3(mp3_fp)
    t = float (audio.info.length)
    time.sleep(round(t)+1)                
    mp3_fp.flush()
    mp3_fp.seek(0)        
    for p in config_data['mic']:    
        if p['type'] == 'ReSpeaker 2-Mics Pi HAT':
            pixels.pixels.off()
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            led_control.find().off()
        elif p['type'] == 'ReSpeaker Core v2.0':
            pixel_ring.off()
        else:
            pass                                                    