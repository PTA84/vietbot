import gih
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
import wget
from gtts import gTTS
# import pygame
from pygame import mixer
import io
import os.path
from os import path
import re
import requests, json, os, uuid, urllib, datetime, base64
# import pydub
# import mutagen
from termcolor import colored
from mutagen.mp3 import MP3
# from pydub import AudioSegment                
# from pydub.playback import play
from urllib.request import urlretrieve
import vlc
mixer.init()
re_speaker= gih.get_config('re_speaker')
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
tts_engine =gih.get_config('tts_engine')    
volume = gih.get_config('volume')
google_api=gih.get_config('google_api')
tts_google_voice_name = gih.get_config('tts_google_voice_name')
tts_google_speed = gih.get_config('tts_google_speed')
tts_google_pitch = gih.get_config('tts_google_pitch')
viettel_token = gih.get_config('viettel_token')
tts_viettel_voice_name = gih.get_config('tts_viettel_voice_name')
tts_viettel_speed = gih.get_config('tts_viettel_speed')
fpt_api = gih.get_config('fpt_api')        
tts_fpt_voice_name = gih.get_config('tts_fpt_voice_name')
tts_fpt_speed = gih.get_config('tts_fpt_speed')
zalo_api = gih.get_config('zalo_api')        
tts_zalo_voice_id = gih.get_config('tts_zalo_voice_id')
tts_zalo_speed = gih.get_config('tts_zalo_speed')

def speak(text):

# TTS Google
    if tts_engine == 1:
        print(colored('[BOT-TTS-Google Free]: '+text,'green'))
        # mixer.init(54000, -16, 1, 4096)
        text = str(sentence[i])
        print ('Nội dung: '+text)
        tts = gTTS(text,lang = 'vi')
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        t = mp3_fp.truncate()/5000
        t = float(t)
        print ('Time delay: '+str(t))
        if re_speaker == 1:
            pixels.pixels.speak() 
        elif re_speaker ==2:
            led_control.find().speak()
        elif re_speaker ==3:    
            pixel_ring.speak()                
        mixer.music.load(mp3_fp)
        mixer.music.set_volume(volume)            
        mixer.music.play()
        time.sleep(round(t)+1)
        mp3_fp.flush()
        mp3_fp.seek(0)        
        # sound = AudioSegment.from_file(mp3_fp)
        # sound = sound.set_frame_rate(24000)     
        # play(sound)                                                                                     

#TTS Google Cloud    
    elif tts_engine == 2:         
        print(colored('[BOT-TTS-Google Cloud]: '+text,'green'))
        import time            
        #HTTP Request
        url = 'https://texttospeech.googleapis.com/v1/text:synthesize?key='+ google_api
        #Header Parameters
        headers = {'Content-type': 'application/json'}
        # Body Parameters
        data = { "audioConfig": { "audioEncoding": "MP3", "pitch": tts_google_pitch, "speakingRate": tts_google_speed },  "input": { "text": text }, "voice": { "languageCode": 'vi-VN', "name": tts_google_voice_name }}
        #Get respounse from Server  
        response = requests.post(url, data = json.dumps(data), headers = headers)
        # Cut audio string from response
        audio_string = response.text.split('"')
        # Convert audio string to audio byte
        audio_byte = base64.b64decode(audio_string[3])                        
        file_name = '/tmp/tts_ggcloud' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'                    
        audio_file= open(file_name, 'wb')
        audio_file.write(audio_byte)
        audio_file.close()
        if re_speaker == 1:
            pixels.pixels.speak() 
        elif re_speaker ==2:
            led_control.find().speak()
        elif re_speaker ==3:    
            pixel_ring.speak()                                    
        mixer.music.load(file_name)
        mixer.music.set_volume(volume)            
        mixer.music.play()                            
        # sound = AudioSegment.from_file(file_name)
        # sound = sound.set_frame_rate(24000)     
        # play(sound)                                                           
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)
#TTS Viettel    
    elif tts_engine == 3:         
        # mixer.init(44100, -16, 1, 1024)
        print(colored('[BOT-TTS-VIETTEL]: '+text,'green'))
        import time            
        #HTTP Request
        url = 'https://viettelgroup.ai/voice/api/tts/v1/rest/syn'
        #Header Parameters
        #hn-quynhanh2, hcm-diemmy2
        headers = {'Content-type': 'application/json', 'token': viettel_token}
        # Body Parameters                        
        data = {'text': text, "voice": tts_viettel_voice_name, "id": "2", "without_filter": False, "speed": tts_viettel_speed, "tts_return_option": 3}
        #Get response from Server  
        response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
        # Open audio file                             
        uniq_filename = '/tmp/tts_vtcc' + str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'
        audio_file= open(uniq_filename, 'wb')
        audio_file.write(response.content)
        audio_file.close()
        if re_speaker == 1:
            pixels.pixels.speak() 
        elif re_speaker ==2:
            led_control.find().speak()
        elif re_speaker ==3:    
            pixel_ring.speak()                                
        # sound = AudioSegment.from_file(uniq_filename)
        # sound = sound.set_frame_rate(24000)             
        # play(sound)                
        mixer.music.load(uniq_filename)
        mixer.music.set_volume(volume)            
        mixer.music.play()                                    
        audio = MP3(uniq_filename)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)

#TTS Zalo    
    elif tts_engine == 4:         
        # mixer.init(44100, -16, 1, 1024)
        print(colored('[BOT-TTS-ZALO]: '+text,'green'))
        file_name='tts_saved/zalo_'+text[:60]+'.mp3'        
        import time
        #HTTP Request
        url = 'https://api.zalo.ai/v1/tts/synthesize'
        #Header Parameters
        #hn-quynhanh2, hcm-diemmy2
        headers = {'apikey': zalo_api}
        # Body Parameters                        
        data = {'input': text, 'speed': tts_zalo_speed, 'encode_type': 1,'speaker_id': tts_zalo_voice_id}
        #Get response from Server  
        response = requests.post(url, data = data, headers = headers)
        url_file = response.json()['data']['url']
        p = vlc.MediaPlayer(url_file)
        p.play()
        # Open audio file                                       
        if re_speaker == 1:
            pixels.pixels.speak() 
        elif re_speaker ==2:
            led_control.find().speak()
        elif re_speaker ==3:    
            pixel_ring.speak()                                
        # mixer.music.load(file_name)
        # mixer.music.set_volume(volume)            
        # mixer.music.play()                                        
        # sound = AudioSegment.from_file(uniq_filename)
        # sound = sound.set_frame_rate(24000)             
        # play(sound)                
        file_name, headers = urlretrieve(url_file)
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)

#TTS FPT    
    elif tts_engine == 5:         
        # mixer.init(44100, -16, 1, 1024)
        print(colored('[BOT-TTS-FPT]: '+text,'green'))
        file_name='tts_saved/fpt_'+text[:60]+'.mp3'
        print ('Nội dung: '+text)                
        import time
        #HTTP Request
        url = 'https://api.fpt.ai/hmi/tts/v5'
        #Header Parameters
        #hn-quynhanh2, hcm-diemmy2
        headers = {'api_key': fpt_api, 'speed':tts_fpt_speed, 'voice': tts_fpt_voice_name}
        # Body Parameters                        
        data = text.encode('utf-8')
        #Get response from Server  
        response = requests.post(url, data = data, headers = headers)
        url_file = response.json()['data']['url']
        time.sleep(2)
        p = vlc.MediaPlayer(url_file)
        p.play()
        # Open audio file                                       
        if re_speaker == 1:
            pixels.pixels.speak() 
        elif re_speaker ==2:
            led_control.find().speak()
        elif re_speaker ==3:    
            pixel_ring.speak()                                
        # mixer.music.load(file_name)
        # mixer.music.set_volume(volume)            
        # mixer.music.play()                                        
        # sound = AudioSegment.from_file(uniq_filename)
        # sound = sound.set_frame_rate(24000)             
        # play(sound)                
        file_name, headers = urlretrieve(url_file)
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)
        


def short_speak(text):
# TTS Google
    if tts_engine == 1:
        import time
        # mixer.init(54000, -16, 1, 4096)
        print(colored('[BOT-TTS-Google Free]: '+text,'green'))
        print ('Nội dung: '+text)
        tts = gTTS(text,lang = 'vi')
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        t = mp3_fp.truncate()/5000
        t = float(t)
        print ('Time delay: '+str(t))
        mp3_fp.seek(0)
        if re_speaker == 1:
            pixels.pixels.speak() 
        elif re_speaker ==2:
            led_control.find().speak()
        elif re_speaker ==3:    
            pixel_ring.speak()                                
        mixer.music.load(mp3_fp)
        mixer.music.set_volume(volume)            
        mixer.music.play()
        # sound = AudioSegment.from_file(mp3_fp)
        # sound = sound.set_frame_rate(24000)     
        # play(sound)                            
        audio = MP3(mp3_fp)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)                
#TTS Google Cloud    

    elif tts_engine == 2:         
        import time            
        print(colored('[BOT-TTS-Google Cloud]: '+text,'green'))
        file_name= 'tts_saved/ggcloud_'+text[:60]+'.mp3'
        me = path.exists(file_name)
        if me ==True:
            if re_speaker == 1:
                pixels.pixels.speak() 
            elif re_speaker ==2:
                led_control.find().speak()
            elif re_speaker ==3:    
                pixel_ring.speak()                                    
            mixer.music.load(file_name)
            mixer.music.set_volume(volume)                            
            mixer.music.play()
            # sound = AudioSegment.from_file(file_name)
            # sound = sound.set_frame_rate(24000)     
            # play(sound)                                           
            audio = MP3(file_name)
            t = float (audio.info.length)
            # print ('Time delay :'+str(t))
            time.sleep(t)
        else:                                        
            #HTTP Request
            url = 'https://texttospeech.googleapis.com/v1/text:synthesize?key='+ google_api
            #Header Parameters
            headers = {'Content-type': 'application/json'}
            # Body Parameters
            data = { "audioConfig": { "audioEncoding": "MP3", "pitch": tts_google_pitch, "speakingRate": tts_google_speed },  "input": { "text": text }, "voice": { "languageCode": 'vi-VN', "name": tts_google_voice_name }}
            #Get respounse from Server  
            response = requests.post(url, data = json.dumps(data), headers = headers)
            # Cut audio string from response
            audio_string = response.text.split('"')
            # Convert audio string to audio byte
            audio_byte = base64.b64decode(audio_string[3])                        
            audio_file= open(file_name, 'wb')
            audio_file.write(audio_byte)
            audio_file.close()
            if re_speaker == 1:
                pixels.pixels.speak() 
            elif re_speaker ==2:
                led_control.find().speak()
            elif re_speaker ==3:    
                pixel_ring.speak()                                    
            mixer.music.load(file_name)
            mixer.music.set_volume(volume)            
            mixer.music.play()                            
            # sound = AudioSegment.from_file(file_name)
            # sound = sound.set_frame_rate(24000)     
            # play(sound)                                                           
            audio = MP3(file_name)
            t = float (audio.info.length)
            # print ('Time delay :'+ str(t))
            time.sleep(round(t)+1)
                
#TTS Viettel    
    elif tts_engine == 3:         
        import time
        # mixer.init(44100, -16, 1, 1024)
        print(colored('[BOT-TTS-Viettel]: '+text,'green'))
        file_name='tts_saved/vtcc_'+text[:60]+'.mp3'
        me = path.exists(file_name)
        if me ==True:
            if re_speaker == 1:
                pixels.pixels.speak() 
            elif re_speaker ==2:
                led_control.find().speak()
            elif re_speaker ==3:    
                pixel_ring.speak()                                    
            # sound = AudioSegment.from_file(file_name)
            # sound = sound.set_frame_rate(24000)                 
            # play(sound)                
            mixer.music.load(file_name)
            mixer.music.set_volume(volume)            
            mixer.music.play()                                        
            audio = MP3(file_name)
            t = float (audio.info.length)
            # print ('Time delay :'+str(t))
            time.sleep(t)
        else:                                  
            print ('Nội dung: '+text)                
            import time            
            #HTTP Request
            url = 'https://viettelgroup.ai/voice/api/tts/v1/rest/syn'
            #Header Parameters
            #hn-quynhanh2, hcm-diemmy2
            headers = {'Content-type': 'application/json', 'token': viettel_token}
            # Body Parameters                        
            data = {'text': text, "voice": tts_viettel_voice_name, "id": "2", "without_filter": False, "speed": tts_viettel_speed, "tts_return_option": 3}            
            #Get respounse from Server  
            response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
            # Open audio file                             
            audio_file= open(file_name, 'wb')
            audio_file.write(response.content)
            if re_speaker == 1:
                pixels.pixels.speak() 
            elif re_speaker ==2:
                led_control.find().speak()
            elif re_speaker ==3:    
                pixel_ring.speak()                                    
            # sound = AudioSegment.from_file(file_name)
            # sound = sound.set_frame_rate(24000)                 
            # play(sound)                
            mixer.music.load(file_name)
            mixer.music.set_volume(volume)            
            mixer.music.play()                                        
            audio = MP3(file_name)
            t = float (audio.info.length)
            # print ('Time delay :'+ str(t))
            time.sleep(round(t)+1)

#TTS Zalo    
    elif tts_engine == 4:         
        # mixer.init(44100, -16, 1, 1024)
        print(colored('[BOT-TTS-ZALO]: '+text,'green'))
        file_name='tts_saved/zalo_'+text[:60]+'.mp3'
        print ('Nội dung: '+text)                
        import time
        #HTTP Request
        url = 'https://api.zalo.ai/v1/tts/synthesize'
        #Header Parameters
        #hn-quynhanh2, hcm-diemmy2
        headers = {'apikey': zalo_api}
        # Body Parameters                        
        data = {'input': text, 'speed': tts_zalo_speed, 'encode_type': 1,'speaker_id': tts_zalo_voice_id}
        #Get response from Server  
        response = requests.post(url, data = data, headers = headers)
        url_file = response.json()['data']['url']
        p = vlc.MediaPlayer(url_file)
        p.play()
        # Open audio file                                       
        if re_speaker == 1:
            pixels.pixels.speak() 
        elif re_speaker ==2:
            led_control.find().speak()
        elif re_speaker ==3:    
            pixel_ring.speak()                                
        # mixer.music.load(file_name)
        # mixer.music.set_volume(volume)            
        # mixer.music.play()                                        
        # sound = AudioSegment.from_file(uniq_filename)
        # sound = sound.set_frame_rate(24000)             
        # play(sound)                
        file_name, headers = urlretrieve(url_file)
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)
        

#TTS FPT    
    elif tts_engine == 5:         
        # mixer.init(44100, -16, 1, 1024)
        print(colored('[BOT-TTS-FPT]: '+text,'green'))
        file_name='tts_saved/fpt_'+text[:60]+'.mp3'
        print ('Nội dung: '+text)                
        import time
        #HTTP Request
        url = 'https://api.fpt.ai/hmi/tts/v5'
        #Header Parameters
        #hn-quynhanh2, hcm-diemmy2
        headers = {'api_key': fpt_api, 'speed':tts_fpt_speed, 'voice': tts_fpt_voice_name}
        # Body Parameters                        
        data = text.encode('utf-8')
        #Get response from Server  
        response = requests.post(url, data = data, headers = headers)
        url_file = response.json()['data']['url']
        time.sleep(2)
        p = vlc.MediaPlayer(url_file)
        p.play()
        # Open audio file                                       
        if re_speaker == 1:
            pixels.pixels.speak() 
        elif re_speaker ==2:
            led_control.find().speak()
        elif re_speaker ==3:    
            pixel_ring.speak()                                
        # mixer.music.load(file_name)
        # mixer.music.set_volume(volume)            
        # mixer.music.play()                                        
        # sound = AudioSegment.from_file(uniq_filename)
        # sound = sound.set_frame_rate(24000)             
        # play(sound)                
        file_name, headers = urlretrieve(url_file)
        audio = MP3(file_name)
        t = float (audio.info.length)
        # print ('Time delay :'+ str(t))
        time.sleep(round(t)+1)

# Speak English
def speaken(audioString):
    tts = gTTS(audioString,lang = 'en')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    t = mp3_fp.truncate()/5000
    t = float(t)
    print ('Time delay: '+str(t))
    mp3_fp.seek(0)
    if re_speaker == 1:
        pixels.pixels.speak() 
    elif re_speaker ==2:
        led_control.find().speak()
    elif re_speaker ==3:    
        pixel_ring.speak()                        
    mixer.music.load(mp3_fp)
    mixer.music.set_volume(volume)                
    mixer.music.play()
    # sound = AudioSegment.from_file(mp3_fp)
    # sound = sound.set_frame_rate(24000)     
    # play(sound)                                                           
    audio = MP3(mp3_fp)
    t = float (audio.info.length)
    print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)    
# Speak Korean
def speakko(audioString):
    tts = gTTS(audioString,lang = 'ko')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    t = mp3_fp.truncate()/5000
    t = float(t)
    print ('Time delay: '+str(t))
    mp3_fp.seek(0)
    if re_speaker == 1:
        pixels.pixels.speak() 
    elif re_speaker ==2:
        led_control.find().speak()
    elif re_speaker ==3:    
        pixel_ring.speak()                                
    mixer.music.load(mp3_fp)
    mixer.music.set_volume(volume)                
    mixer.music.play()
    # sound = AudioSegment.from_file(mp3_fp)
    # sound = sound.set_frame_rate(24000)     
    # play(sound)                                                                   
    audio = MP3(mp3_fp)
    t = float (audio.info.length)
    print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)            
# Speak Japanese
def speakja(audioString):
    tts = gTTS(audioString,lang = 'ja')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    t = mp3_fp.truncate()/5000
    t = float(t)
    print ('Time delay: '+str(t))
    mp3_fp.seek(0)
    if re_speaker == 1:
        pixels.pixels.speak() 
    elif re_speaker ==2:
        led_control.find().speak()
    elif re_speaker ==3:    
        pixel_ring.speak()                            
    mixer.music.load(mp3_fp)
    mixer.music.set_volume(volume)                
    mixer.music.play()
    # sound = AudioSegment.from_file(mp3_fp)
    # sound = sound.set_frame_rate(24000)     
    # play(sound)                                                           
    audio = MP3(mp3_fp)
    t = float (audio.info.length)
    print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)        
# Speak Chinese
def speakzh(audioString):
    tts = gTTS(audioString,lang = 'zh-cn')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    t = mp3_fp.truncate()/5000
    t = float(t)
    print ('Time delay: '+str(t))
    mp3_fp.seek(0)
    if re_speaker == 1:
        pixels.pixels.speak() 
    elif re_speaker ==2:
        led_control.find().speak()
    elif re_speaker ==3:    
        pixel_ring.speak()                        
    mixer.music.load(mp3_fp)
    mixer.music.set_volume(volume)                
    mixer.music.play()
    # sound = AudioSegment.from_file(mp3_fp)
    # sound = sound.set_frame_rate(24000)     
    # play(sound)                                                           
    audio = MP3(mp3_fp)
    t = float (audio.info.length)
    print ('Time delay :'+ str(t))
    time.sleep(round(t)+1)    

