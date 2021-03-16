import time
import requests, json, uuid, urllib, datetime
from termcolor import colored
from mutagen.mp3 import MP3
from urllib.request import urlretrieve
import vlc

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
token=''
speak_volume=1.0
voice_name=''
speed=1.0
pitch=0
for p in config_data['volume']:
    if p['type'] == 'speak':
        speak_volume= p['value']

for p in config_data['tts_engine']:
    if p['name'] == 'tts_fpt':        
        token = p['token']    
        voice_name = p['voice_name']
        speed = p['speed']
def speak(text):

#TTS FPT    
    # mixer.init(44100, -16, 1, 1024)
    print(colored('[BOT-TTS-FPT]: '+text,'green'))
    file_name='tts_saved/fpt_'+text[:60]+'.mp3'
    # print ('Nội dung: '+text)                
    import time
    #HTTP Request
    url = 'https://api.fpt.ai/hmi/tts/v5'
    #Header Parameters
    #hn-quynhanh2, hcm-diemmy2
    headers = {'api_key': token, 'speed':speed, 'voice': voice_name}
    # Body Parameters                        
    data = text.encode('utf-8')
    #Get response from Server  
    response = requests.post(url, data = data, headers = headers)
    url_file = response.json()['data']['url']
    time.sleep(2)
    p = vlc.MediaPlayer(url_file)
    p.play()
    # Open audio file                                       
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
    file_name, headers = urlretrieve(url_file)
    audio = MP3(file_name)
    t = float (audio.info.length)
    # print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)
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

    # mixer.init(44100, -16, 1, 1024)
    print(colored('[BOT-TTS-FPT]: '+text,'green'))
    file_name='tts_saved/fpt_'+text[:60]+'.mp3'
    # print ('Nội dung: '+text)                
    import time
    #HTTP Request
    url = 'https://api.fpt.ai/hmi/tts/v5'
    #Header Parameters
    #hn-quynhanh2, hcm-diemmy2
    headers = {'api_key': token, 'speed':speed, 'voice': voice_name}
    # Body Parameters                        
    data = text.encode('utf-8')
    #Get response from Server  
    response = requests.post(url, data = data, headers = headers)
    url_file = response.json()['data']['url']
    time.sleep(2)
    p = vlc.MediaPlayer(url_file)
    p.play()
    # Open audio file                                       
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
    file_name, headers = urlretrieve(url_file)
    audio = MP3(file_name)
    t = float (audio.info.length)
    # print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)
    for p in config_data['mic']:    
        if p['type'] == 'ReSpeaker 2-Mics Pi HAT':
            pixels.pixels.off()
        elif p['type'] == 'ReSpeaker Mic Array v2.0':
            led_control.find().off()
        elif p['type'] == 'ReSpeaker Core v2.0':
            pixel_ring.off()
        else:
            pass                                                

