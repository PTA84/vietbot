import wikipedia
import speaking
import feedparser
import time
import gih
from speaking import speak, short_speak
import os
import random
import yaml
import gih
import threading
import psutil
from termcolor import colored
import threading
from threading import Thread
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
request_wishes=gih.get_request('request_wishes')
request_person_type=gih.get_request('request_person_type')
request_all=gih.get_request('request_all')
request_single=gih.get_request('request_single')
response_ask_wishes=gih.get_response('response_ask_wishes')

response_new_year=gih.get_response('response_new_year')
response_content_elder=gih.get_response('response_content_elder')
response_content_middle_age=gih.get_response('response_content_middle_age')
response_content_youth=gih.get_response('response_content_youth')
response_content_small_age=gih.get_response('response_content_small_age')
response_content_child=gih.get_response('response_content_child')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')

def main(data):
    print('[BOT]: XỬ LÝ YÊU CẦU CHÚC: '+data)
    data = data.upper()
    wishes = str([s for s in request_wishes if s in data])
    wishes = wishes.replace("['", "")
    wishes = wishes.replace("']", "")     
    data = data.replace(wishes, "") 

    if any(item in data for item in request_person_type):
        person_type = str([s for s in request_person_type if s in data])
        person_type = person_type.replace("['", "")
        person_type = person_type.replace("']", "") 
        if any(item in data for item in request_all):
            best_wishes(person_type,'all')            
        elif any(item in data for item in request_single):
            best_wishes(person_type,'single')                        
        else:
            best_wishes(person_type,'none')
    else:
        short_speak(random.choice(response_ask_wishes))
        more_data=getText()    
        if more_data is not None:
            more_data = more_data.upper()
            wishes = str([s for s in request_wishes if s in more_data])
            wishes = wishes.replace("['", "")
            wishes = wishes.replace("']", "")     
            more_data = more_data.replace(wishes, "")                 
            if any(item in more_data for item in request_person_type):
                person_type = str([s for s in request_person_type if s in more_data])
                person_type = person_type.replace("['", "")
                person_type = person_type.replace("']", "") 
                if any(item in more_data for item in request_all):
                    best_wishes(person_type,'all')            
                elif any(item in more_data for item in request_single):
                    best_wishes(person_type,'single')                        
                else:
                    best_wishes(person_type,'none')
            else:
                short_speak(random.choice(response_choose_lose))            
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
    
def best_wishes(input1, input2):
    if input2 =='none':
        if request_person_type[0] in input1:        
            short_speak('Chúc '+request_person_type[0]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))  
        elif request_person_type[1] in input1:
            short_speak('Chúc '+request_person_type[1]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))    
        elif request_person_type[2] in input1: 
            short_speak('Chúc '+request_person_type[2]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))
        elif request_person_type[3] in input1:
            short_speak('Chúc '+request_person_type[3]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age)) 
        elif request_person_type[4] in input1:
            short_speak('Chúc '+request_person_type[4]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[5] in input1:
            short_speak('Chúc '+request_person_type[5]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[6] in input1:
            short_speak('Chúc '+request_person_type[6]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[7] in input1:
            short_speak('Chúc '+request_person_type[7]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[8] in input1:
            short_speak('Chúc '+request_person_type[8]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[9] in input1:
            short_speak('Chúc '+request_person_type[9]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[10] in input1:
            short_speak('Chúc '+request_person_type[10]+' '+random.choice(response_new_year)+' '+random.choice(response_content_youth))                         
        elif request_person_type[11] in input1:
            short_speak('Chúc '+request_person_type[11]+' '+random.choice(response_new_year)+' '+random.choice(response_content_youth))                         
        elif request_person_type[12] in input1:
            short_speak('Chúc '+request_person_type[12]+' '+random.choice(response_new_year)+' '+random.choice(response_content_small_age))                                 
        elif request_person_type[13] in input1:
            short_speak('Chúc '+request_person_type[13]+' '+random.choice(response_new_year)+' '+random.choice(response_content_child))                                 
    elif input2 =='single':
        if request_person_type[0] in input1:        
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[0]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))  
        elif request_person_type[1] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[1]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))    
        elif request_person_type[2] in input1: 
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[2]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))
        elif request_person_type[3] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[3]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age)) 
        elif request_person_type[4] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[4]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[5] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[5]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[6] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[6]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[7] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[7]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[8] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[8]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[9] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[9]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[10] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[10]+' '+random.choice(response_new_year)+' '+random.choice(response_content_youth))                         
        elif request_person_type[11] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[11]+' '+random.choice(response_new_year)+' '+random.choice(response_content_youth))                         
        elif request_person_type[12] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[12]+' '+random.choice(response_new_year)+' '+random.choice(response_content_small_age))                                 
        elif request_person_type[13] in input1:
            short_speak('Chúc '+random.choice(request_single)+' '+request_person_type[13]+' '+random.choice(response_new_year)+' '+random.choice(response_content_child))                                 
    elif input2 =='all':
        if request_person_type[0] in input1:        
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[0]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))  
        elif request_person_type[1] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[1]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))    
        elif request_person_type[2] in input1: 
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[2]+' '+random.choice(response_new_year)+' '+random.choice(response_content_elder))
        elif request_person_type[3] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[3]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age)) 
        elif request_person_type[4] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[4]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[5] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[5]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[6] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[6]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))         
        elif request_person_type[7] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[7]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[8] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[8]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[9] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[9]+' '+random.choice(response_new_year)+' '+random.choice(response_content_middle_age))                 
        elif request_person_type[10] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[10]+' '+random.choice(response_new_year)+' '+random.choice(response_content_youth))                         
        elif request_person_type[11] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[11]+' '+random.choice(response_new_year)+' '+random.choice(response_content_youth))                         
        elif request_person_type[12] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[12]+' '+random.choice(response_new_year)+' '+random.choice(response_content_small_age))                                 
        elif request_person_type[13] in input1:
            short_speak('Chúc '+random.choice(request_all)+' '+request_person_type[13]+' '+random.choice(response_new_year)+' '+random.choice(response_content_child))    
    pass
    
def run_thread(func,data=None):
    if data is not None:
        t = threading.Thread(target = func, args = (data,))
        t.start()
    else:
        t = threading.Thread(target = func, args = ())
        t.start()
        



if __name__ == '__main__':
    main(data)
