import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
# import os.path
from os import path
import requests, json, uuid, urllib, datetime
from termcolor import colored
from mutagen.mp3 import MP3
mixer.init()
with open('config.json') as config_json:
    config_data = json.load(config_json)

token=''
speak_volume=1.0
voice_name=''
speed=1.0
pitch=0

for p in config_data['tts_engine']:
    if p['name'] == 'tts_viettel':        
        token = p['token']
        voice_name = p['voice_name']
        speed = p['speed']

for p in config_data['volume']:
    if p['type'] == 'speak':
        speak_volume= p['value']
        
def speak(text):
#TTS Viettel    
    # mixer.init(44100, -16, 1, 1024)
    print(colored('[BOT-TTS-VIETTEL]: '+text,'green'))
    import time            
    #HTTP Request
    url = 'https://viettelgroup.ai/voice/api/tts/v1/rest/syn'
    #Header Parameters
    #hn-quynhanh2, hcm-diemmy2
    headers = {'Content-type': 'application/json', 'token': token}
    # Body Parameters                        
    data = {'text': text, "voice": voice_name, "id": "2", "without_filter": False, "speed": speed, "tts_return_option": 3}
    #Get response from Server  
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    # Open audio file                             
    uniq_filename = '/tmp/tts_vtcc' + str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'
    audio_file= open(uniq_filename, 'wb')
    audio_file.write(response.content)
    audio_file.close()
    mixer.music.load(uniq_filename)
    mixer.music.set_volume(speak_volume)            
    mixer.music.play()                                    
    audio = MP3(uniq_filename)
    t = float (audio.info.length)
    # print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)
def short_speak(text):
#TTS Viettel    
    import time
    # mixer.init(44100, -16, 1, 1024)
    print(colored('[BOT-TTS-Viettel]: '+text,'green'))
    file_name='tts_saved/vtcc_'+text[:60]+'.mp3'
    me = path.exists(file_name)
    if me ==True:
        mixer.music.load(file_name)
        mixer.music.set_volume(speak_volume)            
        mixer.music.play()                                        
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+str(t))
        time.sleep(t)
    else:                                  
        # print(colored('[BOT-TTS-Viettel]: '+text,'green'))
        import time            
        #HTTP Request
        url = 'https://viettelgroup.ai/voice/api/tts/v1/rest/syn'
        headers = {'Content-type': 'application/json', 'token': token}
        # Body Parameters                        
        data = {'text': text, "voice": voice_name, "id": "2", "without_filter": False, "speed": speed, "tts_return_option": 3}            
        #Get respounse from Server  
        response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
        # Open audio file                             
        audio_file= open(file_name, 'wb')
        audio_file.write(response.content)
        mixer.music.load(file_name)
        mixer.music.set_volume(speak_volume)            
        mixer.music.play()                                        
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)

