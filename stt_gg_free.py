#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import gih
# import chsv
# import process
# import hass_onoff
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

def main():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio, language = "vi-VN")
        print('BOT nghe được: '+ data)
    except sr.UnknownValueError:    
        print('Sao bạn không nói gì')
        data ='ĐƯỢC RỒI'
        pass
    except sr.RequestError as e:
        print('èo èo'+ e)
        pass
    return data


# [END speech_transcribe_streaming_mic]
