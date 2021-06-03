import os
#from speaking import #short_speak
from termcolor import colored
import datetime
import json
import requests
import threading
import json
import sys
import time
import tts

# from pydub import AudioSegment                
# from pydub.playback import play
from pygame import mixer
import importlib
with open('config.json') as config_json:
    config_data = json.load(config_json)

event_volume=1.0
for p in config_data['volume']:
    # print('Loại Mic: ' + p['type'])
    if p['type'] == 'event':
        event_volume= p['value']
stt_engine= None
for p in config_data['stt_engine']:
    # print('Loại Mic: ' + p['type'])
    if p['is_active'] == True:
        stt_engine=importlib.import_module(p['name'])
        if p['name'] == 'stt_gg_cloud':
        
            ggcre = p['token_file']
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre        
access_url =''
long_token =''

from fuzzywuzzy import fuzz    

def check_hass():
    import requests
    for p in config_data['hass_skill']:
        if p['is_active'] == True:        
            access_url=p['url']
            long_token=p['long_token']
    print(colored('[BOT]: KẾT NỐI - HomeAssistant tại địa chỉ: '+ access_url,'yellow'))
    r=''
    headers = {'Authorization': 'Bearer '+ long_token,'content-type': 'application/json',}
    time.sleep(0.1)
    for p in config_data['hass_skill']:
        if p['is_active'] == True:        
            access_url=p['url']
            long_token=p['long_token']
    try:
        r = requests.get(access_url+ '/api/states',headers = headers)
        if str(r)=='<Response [200]>':
            return True
        else:
            return False
    except:
        return False

def get_device(data,device_type):
    import requests
    for p in config_data['hass_skill']:
        if p['is_active'] == True:        
            access_url=p['url']
            long_token=p['long_token']
    name_list =[]
    entity_id=[]
    friendlyName=[]
    domain= []  
    state= []  
    # attribute=''
    compare_result=[]       
    r=''
    headers = {'Authorization': 'Bearer '+ long_token,'content-type': 'application/json',}
    time.sleep(0.1)
    try:
        r = requests.get(access_url+ '/api/states',headers = headers)    
        if str(r)=='<Response [200]>':
            dict_result=r.json()
            # print(str(dict_result))
            for i in range (len(dict_result)):        
                if dict_result[i]['entity_id'].split('.')[0] ==device_type:
                    entity_id.append(dict_result[i]['entity_id'])                       
                    domain.append(dict_result[i]['entity_id'].split('.')[0])
                    try:
                        friendlyName.append(dict_result[i]['attributes']['friendly_name'].strip().lower())
                        state.append(dict_result[i]['state'])
                    except:
                        friendlyName.append('')                
                        state.append('')   
            try:
                for i in range (len(friendlyName)):
                    match_ratio=fuzz.ratio(data, friendlyName[i])
                    compare_result.append(match_ratio)
                # print(str(compare_result))
                # print(str(friendlyName))
                index=compare_result.index(max(compare_result))
                # print(index)
                print('Tìm thấy thiết bị phù hợp là '+friendlyName[index])
                # print('Tìm thấy tên thiết bị phù hợp là '+friendlyName[index]+'giá trị so sánh là:'+index )
                return entity_id[index], domain[index],friendlyName[index], state[index]
                # else:
                    # print('Không tìm thấy thiết bị phù hợp với tên ' +data)
            except:
                return None
                print('[BOT]: Không tìm thấy thiết bị có tên phù hợp với ' +data)
                tts.tts_vietnamese(True,'Không tìm thấy thiết bị có tên phù hợp với ' +data)        
        else:
            print('[BOT]: Kiểm tra lại tham số kết nối tới HomeAssistant')
            tts.tts_vietnamese(True,'Kiểm tra lại tham số kết nối tới HomeAssistant')        
            return None        
    except:
        print('[BOT]: Không tạo được kết nối được tới HomeAssistant')
        tts.tts_vietnamese(True,'Không tạo được kết nối tới HomeAssistant')
        return None
   
def on_off_all(device,name,action):
    for p in config_data['hass_skill']:
        if p['is_active'] == True:        
            access_url=p['url']
            long_token=p['long_token']
    headers = {'Authorization': 'Bearer '+ long_token,'content-type': 'application/json',}
    payload = {'entity_id': 'all'}        
    if device=='curtain':
        if action == 'on':
            access_url = access_url+'/api/services/cover/open_cover'        
            r = requests.post(access_url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Mở tất cả '+name+' thành công')
                tts.tts_vietnamese(False,'Mở tất cả '+name+' thành công')
            else:
                print('[BOT]: Mở tất cả '+name+' không thành công')
                tts.tts_vietnamese(False,'Mở tất cả '+name+' không thành công')                                            
        elif action =='off':
            access_url = access_url+'/api/services/cover/close_cover'        
            r = requests.post(access_url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đóng tất cả '+name+' thành công')
                tts.tts_vietnamese(False,'Đóng tất cả '+name+' thành công')
            else:
                print('[BOT]: Đóng tất cả '+name+' không thành công')
                tts.tts_vietnamese(False,'Đóng tất cả '+name+' không thành công')                                                
    else:    
        if action == 'on':
            access_url = access_url+'/api/services/'+device+'/turn_on'
            r = requests.post(access_url, data=json.dumps(payload), headers=headers)
            if str(r)=='<Response [200]>':
                print('[BOT]: Bật tất cả '+name+' thành công')
                tts.tts_vietnamese(False,'Bật tất cả '+name+' thành công')
            else:
                print('[BOT]: Bật tất cả '+name+' không thành công')
                tts.tts_vietnamese(False,'Bật tất cả '+name+' không thành công')                                            
        elif action =='off':
            access_url = access_url+'/api/services/'+device+'/turn_off'
            r = requests.post(access_url, data=json.dumps(payload), headers=headers)
            if str(r)=='<Response [200]>':
                print('[BOT]: Tắt tất cả '+name+' thành công')
                tts.tts_vietnamese(False,'Tắt tất cả '+name+' thành công')
            else:
                print('[BOT]: Tắt tất cả '+name+' không thành công')
                tts.tts_vietnamese(False,'Tắt tất cả '+name+' không thành công')                                            

def on_off(data,action,device_type):
    for p in config_data['hass_skill']:
        if p['is_active'] == True:        
            access_url=p['url']
            long_token=p['long_token']
    headers = {'Authorization': 'Bearer '+ long_token,'content-type': 'application/json',}
    if device_type =='cover':        
        try:
            result_device=get_device(data,'cover')         
            entity_id = result_device[0]
            domain=result_device[1]
            friendlyName=result_device[2]
            state=result_device[3]
            if state=='open' and action =='open':
                print('[BOT]: Rèm '+friendlyName+' đã mở sẵn')
                tts.tts_vietnamese(False,'Rèm '+friendlyName+' đã mở sẵn')                                
            elif state =='close' and action =='close':
                print('[BOT]: Rèm '+friendlyName+' đã đóng sẵn')
                tts.tts_vietnamese(False,'Rèm '+friendlyName+' đã đóng sẵn')                                            
            else:
                access_url = access_url+'/api/services/cover/'+action+'_cover'
                payload = {'entity_id': entity_id}
                r = requests.post(access_url, data=json.dumps(payload), headers=headers)
                if str(r)=='<Response [200]>':
                    if action =='open':
                        print('[BOT]: Đã mở rèm '+friendlyName+' thành công')
                        tts.tts_vietnamese(False,'Đã mở rèm '+friendlyName+' thành công')                
                    elif action =='close':
                        print('[BOT]: Đã đóng rèm'+friendlyName+' thành công')
                        tts.tts_vietnamese(False,'Đã đóng rèm '+friendlyName+' thành công')                
                else:
                    print('[BOT]: Không có phản hồi từ rèm '+friendlyName)
                    tts.tts_vietnamese(True,'Không có phản hồi từ rèm '+friendlyName)                                
        except:
            print('[BOT]: Không tìm thấy rèm có tên là '+data)
            tts.tts_vietnamese(False,'Không tìm thấy rèm có tên là '+data)
    else: 
        try:
            result_device=get_device(data,device_type)        
            entity_id = result_device[0]
            domain=result_device[1]
            friendlyName=result_device[2]
            state=result_device[3]
            if state=='on' and action =='on':
                print('[BOT]: '+friendlyName+' đã bật mở sẵn')
                tts.tts_vietnamese(False,friendlyName+' đã bật mở sẵn')                                
            elif state =='off' and action =='off':
                print('[BOT]: '+friendlyName+' đã tắt ngắt sẵn')
                tts.tts_vietnamese(False,friendlyName+' đã tắt ngắt sẵn')                                
            else:
                access_url = access_url+'/api/services/'+domain+'/turn_'+action
                payload = {'entity_id': entity_id}
                r = requests.post(access_url, data=json.dumps(payload), headers=headers)
                if str(r)=='<Response [200]>':
                    if action =='on':
                        print('[BOT]: Đã bật mở '+friendlyName+' thành công')
                        tts.tts_vietnamese(False,'Đã bật mở '+friendlyName+' thành công')
                    elif action =='off':
                        print('[BOT]: Đã tắt ngắt '+friendlyName+' thành công')
                        tts.tts_vietnamese(False,'Đã tắt ngắt '+friendlyName+' thành công')
                else:
                    print('[BOT]: Không có phản hồi từ '+friendlyName)
                    tts.tts_vietnamese(False,'Không có phản hồi từ '+friendlyName)
        except:
            print('[BOT]: Không thực hiện được với thiết bị có tên là '+data)
            tts.tts_vietnamese(False,'Không thực hiện được với thiết bị có tên là '+data)


def check_state(data,state_type,device_type):
    for p in config_data['hass_skill']:
        if p['is_active'] == True:        
            access_url=p['url']
            long_token=p['long_token']
    try:    
        result_device=get_device(data,device_type)
        entity_id = result_device[0]
        friendlyName=result_device[1]
        state=result_device[2]
        if state == 'off':
            state = 'tắt'
        elif state == 'on':
            state= 'bật'
        elif state == 'open':
            state= 'mở'
        elif state == 'close':
            state= 'đóng'
        else:
            pass
        print('[BOT]: Trạng thái của '+friendlyName+ ' là '+ r)
        tts.tts_vietnamese(False,'Trạng thái của ' +friendlyName+ ' là '+ r)
    except:
        print('[BOT]: Không tìm thấy trạng thái thiết bị có tên là '+data)
        tts.tts_vietnamese(False,'Không tìm thấy trạng thái thiết bị có tên là '+data)


def play_ding():
    mixer.music.load('resources/ding.wav')
    mixer.music.set_volume(event_volume)                
    mixer.music.play()    
    # sound = AudioSegment.from_mp3('resources/ding.wav')
    # play(sound)                                
def play_dong():
    mixer.music.load('resources/dong.wav')
    mixer.music.set_volume(event_volume)                
    mixer.music.play()    
    # sound = AudioSegment.from_mp3('resources/dong.wav')
    # play(sound)         

if __name__ == '__main__':
    print(check_hass())
    print(get_device('công tắc phòng khách','light-switch'))
