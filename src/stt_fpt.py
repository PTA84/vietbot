#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import gih
# import chsv
# import process
#import hass_onoff
# import random
# import speaking
# import ptz
# import time
# import amlich
# import thu
# import ngayle
# import tintuc
# import loto 
# import fun 
# import hass_execute
# import re 
# import radio 
# import weth
# import wk
# import spot
# import speech_recognition as sr
# import weather as wt
# from pygame import mixer

def main():
#   print ('FPT')
    r = sr.Recognizer()
    import random
#   print ('FPT1')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    with open('tmp/record.wav', "wb") as f:
        f.write(audio.get_wav_data())
    data = ""
    keys = ['Os1MlynwG2W7eNFecfME0EOHZ9hCcobk','hFewll7iiYesYsc5TQO9RyPWogvYGXff','1E9dz9Oyax0WFbqVxIsBQSTuCf04yA6I']
    api_fpt_key = random.choice(keys)
    print (api_fpt_key)
    try:
        import requests
        url = 'https://api.fpt.ai/hmi/asr/general'
        payload = open('tmp/record.wav', 'rb').read()
        headers = {'api-key': api_fpt_key}
        response = requests.post(url=url, data=payload, headers=headers)
        txt = response.json()
#       print (txt)
        import json
        for element in txt['hypotheses']:
            data = element['utterance'] 
#   print(response.json())
#       data = r.recognize_google(audio, language = "vi-VN")
        print('BOT nghe được: '+ data)
    except sr.UnknownValueError:    
        print('Sao bạn không nói gì')
        data ='ĐƯỢC RỒI'
        pass
    except sr.RequestError as e:
        print('èo èo'+ e)
        pass
    return data


if __name__ == '__main__':
    main()
# [END speech_transcribe_streaming_mic]
