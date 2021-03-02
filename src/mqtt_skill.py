#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-

#Tạo thư mục mp3 trong thư mục vietbot

#Xử lý file và thư mục
import os
from os import listdir
from os import path
import sys
import re
#Xử lý thời gian
import time
import datetime
#Xử lý url
import pafy
import requests
import urllib
import re
import urllib.request
import urllib.parse
import datetime
#So sánh gần giống 2 chuỗi
from fuzzywuzzy import fuzz
#TTS Engine
from speaking import speak, short_speak 
from termcolor import colored
import random
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
#Xử lý thread
import threading
#Play Audio và đọc file MP3
import pygame
from pygame import mixer
from mutagen.mp3 import MP3
mixer.init()
from pydub import AudioSegment

#Gọi Hotword
import pyaudio
import struct
import pvporcupine
#Đọc file config
import gih
sensitivities =gih.get_config('sensitivities')
keyword_paths=gih.get_config('keyword_paths')
re_speaker= gih.get_config('re_speaker')
if re_speaker == 1:
    import pixels
#Điều khiển led
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
volume=gih.get_config('volume')
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
broker_address=gih.get_config('broker_address')
broker_port=gih.get_config('broker_port')
broker_username=gih.get_config('broker_username')
broker_password=gih.get_config('broker_password')
request_mqtt_device_name=gih.get_config('request_mqtt_device_name')
request_mqtt_topic=gih.get_config('request_mqtt_topic')

topic=gih.get_device('topic')
request_exit = gih.get_request('request_exit')
payload_light_1_on=gih.get_device('payload_light_1_on')
payload_light_1_off=gih.get_device('payload_light_1_off')
payload_light_2_on=gih.get_device('payload_light_2_on')
payload_light_2_off=gih.get_device('payload_light_2_off')
payload_light_3_on=gih.get_device('payload_light_3_on')
payload_light_3_off=gih.get_device('payload_light_3_off')
payload_light_4_on=gih.get_device('payload_light_4_on')
payload_light_4_off=gih.get_device('payload_light_4_off')
payload_light_5_on=gih.get_device('payload_light_5_on')
payload_light_5_off=gih.get_device('payload_light_5_off')
payload_fan_on=gih.get_device('payload_fan_on')
payload_fan_off=gih.get_device('payload_fan_off')
client_id = f'python-mqtt-{random.randint(0, 1000)}'    
request_on = gih.get_request('request_on')
request_off = gih.get_request('request_off')
request_light_1 = gih.get_request('request_light_1')

request_light_2 = gih.get_request('request_light_2')
request_light_3 = gih.get_request('request_light_3')
request_light_4 = gih.get_request('request_light_4')
request_light_5 = gih.get_request('request_light_5')
request_fan = gih.get_request('request_fan')
response_timeout=gih.get_response('response_timeout')        

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # mqtt.Client.connected_flag=False#create flag in class
    client = mqtt_client.Client(client_id) #create new instance 
    client.username_pw_set(username=username,password=password)    #bind call back function
    client.on_connect = on_connect
    # client.loop_start()  #Start loop 
    print("Connecting to broker ",broker_address)
    client.connect(broker_address, broker_port,15)
    # while not client.connected_flag: #wait in loop
        # print("In wait loop")
        # time.sleep(1)
    print("in Main Loop")
    # client.loop_stop()    #Stop loop 
    # client.disconnect() # disconnect
    return client

def disconnect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # mqtt.Client.connected_flag=False#create flag in class
    client = mqtt_client.Client(client_id) #create new instance 
    client.username_pw_set(username=username,password=password)    #bind call back function
    client.on_connect = on_connect
    # client.loop_start()  #Start loop 
    print("Connecting to broker ",broker_address)
    client.connect(broker_address, broker_port,15)
    # while not client.connected_flag: #wait in loop
        # print("In wait loop")
        # time.sleep(1)
    print("in Main Loop")
    # client.loop_stop()    #Stop loop 
    client.disconnect() # disconnect
    return client


def run_thread(func,data=None):
    if data is not None:
        t = threading.Thread(target = func, args = (data,))
        t.start()
    else:
        t = threading.Thread(target = func, args = ())
        t.start()


def signal_handler(sig, frame):    
        print('BẠN MỚI ẤN CTRL+C PHẢI KHÔNG, BYE BYE NHÉ')        
        sys.exit(0)


def handler(signum, frame):
    print('Ố Ô, THẤY BẠN ẤN CTRL+Z RỒI, NHƯNG MÀ TÔI CHẶN RỒI NHÉ')
                    
        
def play_ding():
    mixer.music.load('resources/ding.wav')
    mixer.music.set_volume(volume)                  
    mixer.music.play()                    


def play_dong():
    mixer.music.load('resources/dong.wav')
    mixer.music.set_volume(volume)              
    mixer.music.play()                    

def back_to_main():
    play_dong()
    if respeaker == 1:
        pixels.pixels.off()
    main()


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def publish(client, topic, message):
    time.sleep(1)
    result = client.publish(topic, message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print('Đã ra lệnh thành công')
        speaking.short_speak('Đã ra lệnh thành công')
    else:
        print('Ra lệnh không thành công')
        speaking.short_speak('Ra lệnh không thành công')



def main():
    
    print(colored('[BOT]: CHỜ RA LỆNH...','green'))
    porcupine = None
    pa = None
    audio_stream = None    
    try:
        # porcupine = pvporcupine.create(keywords=keywords,sensitivities=sensitivities)
        porcupine = pvporcupine.create(keyword_paths=keyword_paths,sensitivities=sensitivities)        
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
                        rate=porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)
        # short_speak(random.choice(list_response_ask_wakeup))           

        while True:      
            pcm = audio_stream.read(porcupine.frame_length)
            # pcm = audio_stream.read(porcupine.frame_length,exception_on_overflow=False)                
            # exception_on_overflow = False
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)
            # print(str(keyword_index))
            if keyword_index >= 0:
                if respeaker == 1:
                    pixels.pixels.wakeup() 
                play_ding()
                # print('[BOT]: Phát hiện khẩu lệnh đúng '+ keywords[keyword_index] +'xin mời ra lệnh')
                porcupine.delete()
                pa.terminate()
                audio_stream.close()
                process()
                break
    finally:
        # if porcupine is not None:
            # porcupine.delete()

        # if audio_stream is not None:
            # audio_stream.close()

        # if pa is not None:
                # pa.terminate()
    # except:
        pass

def getText():
    # time.sleep(1)
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
    return data

def process():
    client = connect_mqtt()
    data = getText()
    if data is None: 
        speaking.short_speak(random.choice(response_timeout))     
        back_to_main()                
        pass
    print('[BOT] - XỬ LÝ YÊU CẦU')
    if respeaker == 1:
        pixels.pixels.think()        
    data = str(data).upper()    

    if any(item in data for item in request_on):
        if  any(item in data for item in request_light_1):
            print('[BOT]:-------------Xử lý câu lệnh bật đèn 1---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh bật đèn thứ nhất')
            publish(client,topic,payload_light_1_on) 
            back_to_main()                                       
        if  any(item in data for item in request_light_2):
            print('[BOT]:-------------Xử lý câu lệnh bật đèn 2---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh bật đèn thứ hai')
            publish(client,topic,payload_light_2_on) 
            back_to_main()                                       
        if  any(item in data for item in request_light_3):
            print('[BOT]:-------------Xử lý câu lệnh bật đèn 3---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh bật đèn thứ ba')
            publish(client,topic,payload_light_3_on) 
            back_to_main()                                       
        if  any(item in data for item in request_light_4):
            print('[BOT]:-------------Xử lý câu lệnh bật đèn 4---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh bật đèn thứ tư')
            publish(client,topic,payload_light_4_on) 
            back_to_main()                                       
        if  any(item in data for item in request_light_5):
            print('[BOT]:-------------Xử lý câu lệnh bật đèn 5---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh bật đèn thứ năm')
            publish(client,topic,payload_light_5_on) 
            back_to_main()                                       
        if  any(item in data for item in request_fan):
            print('[BOT]:-------------Xử lý câu lệnh bật quạt---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh bật quạt')
            publish(client,topic,payload_fan_on) 
            back_to_main()                                                   
    elif any(item in data for item in request_off):
        if  any(item in data for item in request_light_1):
            print('[BOT]:-------------Xử lý câu lệnh tắt đèn 1---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh tắt đèn thứ nhất')            
            publish(client,topic,payload_light_1_off) 
            back_to_main()                                       
        if  any(item in data for item in request_light_2):
            print('[BOT]:-------------Xử lý câu lệnh tắt đèn 2---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh tắt đèn thứ hai')
            publish(client,topic,payload_light_2_off) 
            back_to_main()                                       
        if  any(item in data for item in request_light_3):
            print('[BOT]:-------------Xử lý câu lệnh tắt đèn 3---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh tắt đèn thứ ba')
            publish(client,topic,payload_light_3_off) 
            back_to_main()                                       
        if  any(item in data for item in request_light_4):
            print('[BOT]:-------------Xử lý câu lệnh tắt đèn 4---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh tắt đèn thứ tư')
            publish(client,topic,payload_light_4_off) 
            back_to_main()                                       
        if  any(item in data for item in request_light_5):
            print('[BOT]:-------------Xử lý câu lệnh tắt đèn 5---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh tắt đèn thứ năm')
            publish(client,topic,payload_light_5_off) 
            back_to_main()                                       
        if  any(item in data for item in request_fan):
            print('[BOT]:-------------Xử lý câu lệnh tắt quạt---------------')                 
            speaking.short_speak('Bắt đầu xử lý câu lệnh tắt quạt')
            publish(client,topic,payload_fan_off) 
    elif request_exit == True:                
        if mixer.get_busy == False:
            mixer.stop()
            back_to_main()                                    
            pass
        else:
            back_to_main()                
            pass                
    else:
        speaking.short_speak('Yêu cầu không đúng vào chủ đề, yêu cầu lại nhé')
        back_to_main()
        pass
#Skill 



if __name__ == '__main__':
    main()