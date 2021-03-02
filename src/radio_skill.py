#import news
import feedparser
from speaking import speak, short_speak
import random
import gih
import re
import os
import requests
from termcolor import colored
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
import vlc
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
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
request_radio=gih.get_request('request_radio')
request_radio_station_link=gih.get_request('request_radio_station_link')
request_radio_station_name=gih.get_request('request_radio_station_name')
response_news=gih.get_response('response_news')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')
prefix_url = 'https://5a6872aace0ce.streamlock.net/'

data = 'VOV 1'

def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH NGHE RADIO: '+data)
    if any(item in data for item in request_radio_station_name):    
        if request_radio_station_name[0] in data:
            play_radio(0,0)
        elif request_radio_station_name[1] in data:
            play_radio(1,1)
        elif request_radio_station_name[2] in data:
            play_radio(2,2)    
        elif request_radio_station_name[3] in data:
            play_radio(3,3)    
        elif request_radio_station_name[4] in data:
            play_radio(4,4)    
    else:
        short_speak(random.choice(response_news))     
        more_data=getText()    
        if more_data is not None:
            more_data=more_data.upper()    
            if any(item in more_data for item in request_radio_station_name):    
                if request_radio_station_name[0] in more_data:
                    play_radio(0,0)
                elif request_radio_station_name[1] in more_data:
                    play_radio(1,1)
                elif request_radio_station_name[2] in more_data:
                    play_radio(2,2)    
                elif request_radio_station_name[3] in more_data:
                    play_radio(3,3) 
                elif request_radio_station_name[4] in more_data:
                    play_radio(4,4)                     
            else:
                short_speak(random.choice(response_choose_lose))
                pass
        else:
            short_speak(random.choice(response_say_nothing))
            pass
            
def getText():
    #time.sleep(1)
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
#   Dùng STT VTCC
    elif stt_engine == 3:
        print(colored('---------------DÙNG STT VIETTEL-------------','blue'))        
        data = stt_viettel.main()        
    elif stt_engine == 4:
        print(colored('---------------DÙNG STT VIETTEL-------------','blue'))        
        data = stt_viettel_test.main()
#   Dùng STT FPT
    elif stt_engine == 5:
        print(colored('---------------DÙNG STT FPT-------------','yellow'))
        data = stt_fpt.py.main()
#   Sử dụng text input
    return data                           

def play_radio(data1,data2):    
    url_file = prefix_url + request_radio_station_link[data1]
    print(str(url_file))
    p = vlc.MediaPlayer('https://5a6872aace0ce.streamlock.net/nghevov1/vov1.stream_aac/chunklist.m3u8')
    p.play()
    # Open audio file                                       
    if re_speaker == 1:
        pixels.pixels.speak() 
    elif re_speaker ==2:
        led_control.find().speak()
    elif re_speaker ==3:    
        pixel_ring.speak()                                
# def play_radio(data1,data2):

    # newsFeed = feedparser.parse(request_radio_station_link[data1])   
    # i =1
    # while i < 6: 
        # entry = newsFeed.entries[i]
        # print (entry.published)
        # clean = re.compile('<.*?>')
        # clean_content= re.sub(clean, '', entry.summary)
        # speak('Tin mới thứ '+ str(i)+ ' từ '+ request_radio_station_name[data2] +" "+clean_content)        
        # entry = None
        # clean = None
        # clean_content = None        
        # i += 1

        
if __name__ == '__main__':
    main(data)