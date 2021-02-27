#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import gih
# import chsv
# import process
# #import hass_onoff
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
# import execute
# import re 
# import radio 
# import weth
# import wk
# import spot
# import weather as wt
# from pygame import mixer
import os
import gih

def main():
    import requests
    from pathlib import Path
    import os.path
    import speech_recognition as sr
    r = sr.Recognizer()
    token = gih.get_config('viettel_token')    
    dirname = os.path.dirname(os.path.abspath('_file_'))
    path = os.path.dirname(os.path.abspath('_file_'))
    url = "https://viettelgroup.ai/voice/api/asr/v1/rest/decode_file"
    headers = {
        'token': token,
        #'sample_rate': 16000,
        #'format':'S16LE',
        #'num_of_channels':1,
        #'asr_model': 'mode
        # l code'
    }
    s = requests.Session()
    cert_path = ('wwwvtccai.crt')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    with open('tmp/vtcc.wav', "wb") as f:
        f.write(audio.get_wav_data())
    try:
        files = {'file': open('tmp/vtcc.wav', 'rb')}
        response = requests.post(url,files=files, headers=headers, verify=cert_path, timeout=None)
        txt = response.json()
        if len(t) > 0:
            t = txt[0]
            text = t['result']
            import json
            for element in text['hypotheses']:
                data = element['transcript']    
                print('BOT nghe được: '+ data)
        else:
            data = 'cảm ơn'
            print('không nghe thấy gì')
    except:
        print('Lỗi Viettel')
        pass
    
    return data
# [END speech_transcribe_streaming_mic]


if __name__ == '__main__':
    main()
#[END speech_transcribe_streaming_mic]
