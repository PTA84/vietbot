import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
# import os.path
from os import path
import requests, json, uuid, urllib, datetime, base64
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
    if p['name'] == 'tts_gg_cloud':        
        token = p['token']
        voice_name = p['voice_name']
        speed = p['speed']

for p in config_data['volume']:
    if p['type'] == 'speak':
        speak_volume= p['value']
        
def speak(text):
    # mixer.init(44100, -16, 1, 1024)
    print(colored('[BOT-TTS-GOOGLE-CLOUD]: '+text,'green'))
    import time            
    #HTTP Request
    url = 'https://texttospeech.googleapis.com/v1/text:synthesize?key='+ token
        #Header Parameters
    headers = {'Content-type': 'application/json'}
    # Body Parameters
    data = { "audioConfig": { "audioEncoding": "MP3", "pitch": pitch, "speakingRate": speed },  "input": { "text": text }, "voice": { "languageCode": 'vi-VN', "name": voice_name }}
    #Get response from Server  
    response = requests.post(url, data = json.dumps(data), headers = headers)
    # Cut audio string from response
    audio_string = response.text.split('"')
    # Convert audio string to audio byte
    audio_byte = base64.b64decode(audio_string[3])                        
    file_name = '/tmp/tts_ggcloud' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'                    
    audio_file= open(file_name, 'wb')
    audio_file.write(audio_byte)
    audio_file.close()
    mixer.music.load(file_name)
    mixer.music.set_volume(speak_volume)            
    mixer.music.play()                                    
    audio = MP3(file_name)
    t = float (audio.info.length)
    # print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)

def short_speak(text):
    import time
    # mixer.init(44100, -16, 1, 1024)
    print(colored('[BOT-TTS-GOOGLE-CLOUD]: '+text,'green'))
    file_name='tts_saved/ggcloud_'+text[:60]+'.mp3'
    me = path.exists(file_name)
    if me ==True:
        mixer.music.load(file_name)
        mixer.music.set_volume(speak_volume)            
        mixer.music.play()                                        
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+str(t))
        time.sleep(round(t)+1)
    else:                                  
        import time            
        #HTTP Request
        url = 'https://texttospeech.googleapis.com/v1/text:synthesize?key='+ token
            #Header Parameters
        headers = {'Content-type': 'application/json'}
        # Body Parameters
        data = { "audioConfig": { "audioEncoding": "MP3", "pitch": pitch, "speakingRate": speed },  "input": { "text": text }, "voice": { "languageCode": 'vi-VN', "name": voice_name }}
        #Get response from Server  
        response = requests.post(url, data = json.dumps(data), headers = headers)
        # Cut audio string from response
        audio_string = response.text.split('"')
        # Convert audio string to audio byte
        audio_byte = base64.b64decode(audio_string[3])                        
        file_name = '/tmp/tts_ggcloud' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'                    
        audio_file= open(file_name, 'wb')
        audio_file.write(audio_byte)
        audio_file.close()
        mixer.music.load(file_name)
        mixer.music.set_volume(speak_volume)            
        mixer.music.play()                                        
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)
