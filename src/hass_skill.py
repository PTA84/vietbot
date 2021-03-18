import os
import yaml
import chsv    
#from speaking import #short_speak
from termcolor import colored
import datetime
import json
import requests
import threading
import json
import sys
import time
import sqlite3 as lite
# from pydub import AudioSegment                
# from pydub.playback import play
from pygame import mixer
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
import importlib
with open('config.json') as config_json:
    config_data = json.load(config_json)
with open('request.json') as request_json:
    request_data = json.load(request_json)    
with open('response.json') as response_json:
    response_data = json.load(response_json)    


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
domain =''
longlivedtoken =''
for p in config_data['hass_skill']:
    if p['is_active'] == True:        
        domain=p['url']
        longlivedtoken=p['long_token']

def info_user():
    if os.path.exists('usin.db'):
        os.remove('usin.db')
    usin = lite.connect('usin.db',check_same_thread=False)
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS link_music_youtube (
                                            link1 text,
                                            link2 text,
                                            link3 text,
                                            link4 text,
                                            link5 text,
                                            link6 text,
                                            link7 text,
                                            link8 text,
                                            link9 text,
                                            link10 text,
                                            link11 text
                                            ); """
    if usin is not None: 
        cur2 = usin.cursor()
        cur2.execute(sql_create_projects_table)
    return usin
def data_init():
    if os.path.exists('hassdata.db'):
        os.remove('hassdata.db')
    con1 = lite.connect('hassdata.db',check_same_thread=False)
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS HASSINFO (
                                            entity_id_ex text,
                                            domain_ex text,
                                            friendly_name_ex text
                                            ); """
    if con1 is not None: 
        cur = con1.cursor()
        cur.execute(sql_create_projects_table)

    return con1

def data_command_init():

    con2 = lite.connect('command.db',check_same_thread=False)
    sql_command_table = """ CREATE TABLE IF NOT EXISTS customcommand (
                                            Command text,
                                            entity_id text,
                                            service text
                                            ); """
    if con2 is not None: 
        cur = con2.cursor()
        cur.execute(sql_command_table)
    return con2

def check_hass(url,long_token):
    import requests
    import hass_skill
    print(colored('[BOT]: KẾT NỐI - trung tâm điều khiển nhà tại địa chỉ: '+ url,'yellow'))
    con1 = data_init()
    con_command = data_command_init()
    r=''
    headers = {'Authorization': 'Bearer '+ long_token,'content-type': 'application/json',}
    time.sleep(0.1)
    try:
        r = requests.get(url+ '/api/states',headers = headers)
    except:
        return False
    if str(r)=='<Response [200]>':
        r = r.json()
        i = 0
        while i < len(r)-1 :
            i += 1
            x = r[i]
            y = x['entity_id']
            y = y.split('.')
            entity_id_ex = y[1]
            domain_ex = y[0]
            y = x['attributes']
            try:
                friendly_name_ex = y['friendly_name'].strip()
            except:
                friendly_name_ex =""
                pass
            if domain_ex == 'script' or domain_ex == 'light' or domain_ex == 'switch' or domain_ex=='sensor' or domain_ex =='binary_sensor' or domain_ex =='media_player' or domain_ex =='cover' or domain_ex =='input_select' or domain_ex =='alarm_control_panel' or domain_ex =='climate' or domain_ex =='device_tracker' or domain_ex == 'automation' or domain_ex == 'scene' :
                pre_write_data = (entity_id_ex, domain_ex, friendly_name_ex)
                
                with con1:
                    cur = con1.cursor()
                    cur.execute("INSERT INTO HASSINFO VALUES(?,?,?)",pre_write_data)
        time.sleep(0.5)
        return True
    else:
        return False

def find_hass_friendly_name(data):
    print('[BOT] -TÌM TÊN THIẾT BỊ')
    print('')
    friendly_name = chsv.check_fr(data)
    ex,ey = chsv.export_e_d(friendly_name)
    domain_ex = ex
    entity_id_ex = ey
    m = 0
    object = [define(domain_ex,entity_id_ex,domain,longlivedtoken) for x in range(len(domain_ex))]
    while m < len(domain_ex): 
        object[m] = define(domain_ex[m],entity_id_ex[m],domain,longlivedtoken)
        object[m] = object[m].define()
        m += 1
    if len(object)==0:                     
        #short_speak('Không tìm thấy thiết bị trong trung tâm điều khiển nhà')        
        #short_speak("Vui lòng nói lại tên thiết bị")
        play_ding()
        more_data=stt_engine.main()
        print('[BOT] -TÌM LẠI TÊN THIẾT BỊ')
        print('')
        friendly_name = chsv.check_fr(data)
        ex,ey = chsv.export_e_d(friendly_name)
        domain_ex = ex
        entity_id_ex = ey
        n = 0
        object = [define(domain_ex,entity_id_ex,domain,longlivedtoken) for x in range(len(domain_ex))]
        while n < len(domain_ex): 
            object[n] = define(domain_ex[n],entity_id_ex[n],domain,longlivedtoken)
            object[n] = object[n].define()
            n += 1
            
    return object
   
def on_off(data,action):
    friendly_name_hass = find_hass_friendly_name(data)
    p = 0
    while p < len(friendly_name_hass): 
        if action =='on':
            friendly_name_hass[p].turn_on()
        elif action =='off':    
            friendly_name_hass[p].turn_off()                
        # print(colored(str(friendly_name_hass[p])+ ': tắt ngắt','green'))
        p +=1        

def on_off_all_1(device,name,action):

    headers = {'Authorization': 'Bearer '+ longlivedtoken,'content-type': 'application/json',}
    payload = {'entity_id': 'all'}        
    if action == 'on':
        url = domain+'/api/services/'+device+'/turn_on'
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print('')
        if str(r)=='<Response [200]>':
            print('[BOT]: Bật tất cả '+name+' thành công')
            #short_speak('Bật tất cả '+name+' thành công')
        else:
            print('[BOT]: Bật tất cả '+name+' không thành công')
            #short_speak('Bật tất cả '+name+' không thành công')                                            
    elif action =='off':
        url = domain+'/api/services/'+device+'/turn_off'
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print('')
        if str(r)=='<Response [200]>':
            print('[BOT]: Tắt tất cả '+name+' thành công')
            #short_speak('Tắt tất cả '+name+' thành công')
        else:
            print('[BOT]: Tắt tất cả '+name+' không thành công')
            #short_speak('Tắt tất cả '+name+' không thành công')                                            

def on_off_all_2(name,action):
    headers = {'Authorization': 'Bearer '+ longlivedtoken,'content-type': 'application/json',}
    payload = {'entity_id': 'all'}        
    if action == 'on':
        url = domain+'/api/services/cover/open_cover'        
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print('')
        if str(r)=='<Response [200]>':
            print('[BOT]: Mở tất cả '+name+' thành công')
            #short_speak('Mở tất cả '+name+' thành công')
        else:
            print('[BOT]: Mở tất cả '+name+' không thành công')
            #short_speak('Mở tất cả '+name+' không thành công')                                            
    elif action =='off':
        url = domain+'/api/services/cover/close_cover'        
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print('')
        if str(r)=='<Response [200]>':
            print('[BOT]: Đóng tất cả '+name+' thành công')
            #short_speak('Đóng tất cả '+name+' thành công')
        else:
            print('[BOT]: Đóng tất cả '+name+' không thành công')
            #short_speak('Đóng tất cả '+name+' không thành công')                                            


def trangthai(data):
    print('')
    friendly_name = chsv.check_fr(data)
    ex,ey = chsv.export_e_d(friendly_name)
    domain_ex= ex
    entity_id_ex= ey
    i=0
    object = [0 for x in range(len(domain_ex))]
    while i < len(domain_ex):
        object[i] = [friendly_name[i],domain_ex[i],entity_id_ex[i],domain,longlivedtoken]
        i+=1
    # print(str(object))        
    k=0
    while k < len(object):        
        doma =  object[k][1]
        print(doma)
        enti =  object[k][2]
        print(enti)
        t,tt = check_state(doma,enti)
        #short_speak(object[k][0]+ ' đang '+ t)
        k+=1  

def thietlap(friendly_name_hass,sta,data):
    q = 0
    try:
        r=friendly_name_hass[0].domain_extract()
        doma = sta[0][1]
        enti = sta[0][2]
        t,tt = check_state(doma,enti)
        tt = tt['attributes']['options']
    except:
        pass
    
    while q < len(friendly_name_hass):
        r=friendly_name_hass[q].domain_extract()
        if str(r)== 'input_select':
            for x in range(len(tt)):
                if tt[x].upper() in data.upper():
                    try:
                        res=friendly_name_hass[q].set_option(tt[x])
                        if res == 1:
                            #short_speak(' thiết lập thành công ')
                            break
                    except:
                        pass
        q+=1
    
    if 'NHIỆT ĐỘ' in data.upper():
        
        qq=0
        data = data.split()
        x=0
        while x < len(data):
            if data[x].isnumeric() ==True and int(data[x])<32 and int(data[x])>15:
                degree = int(data[x])                
                break
            x+=1

        while qq < len(friendly_name_hass):
            rep=friendly_name_hass[qq].domain_extract()
            
            if str(rep)== 'climate':
                
                res=friendly_name_hass[qq].set_temperature(degree)
                if res ==1:
                    #short_speak('Thiết lập máy lạnh sang '+ str(degree)+ ' độ')
                    break
            qq+=1

def hen_gio(data):
    global t1
    from threading import Timer    
    
    from time import ctime, strftime
    def check_time_in(xi_tin):
        split_lan1 = xi_tin.split()
        
        for m in range(0,len(split_lan1)):
            
            if ":" in split_lan1[m]:
                split_lan2 = split_lan1[m].split(":")
                
                break
            else:
                split_lan2=[]
        return split_lan2

    def more_info_friendly(data,friendly_name):
        continuego=1
        if friendly_name== []:
            qa = 0
            while qa<3:
                qa+=1
                #short_speak('tác vụ cần làm là gì')
                more_data=stt_engine.main()
                if 'HỦY' in more_data.upper():
                    #short_speak('thoát chế độ hẹn giờ')
                    continuego=0
                    break
                else:
                    friendly_name = find_hass_friendly_name(more_data)
                    if friendly_name ==[]:
                        pass
                    else:
                        data=more_data
                        break
        return data, friendly_name, continuego                
    def more_info_time(data,time_in_data):
        continue_go =1
        time_in_data=check_time_in(data)
        if time_in_data ==[]:
            qb = 0
            while qb<3:
                qb+=1
                #short_speak('cung cấp thời điểm thực hiện')
                more_data1=stt_engine.main()
                if 'HỦY' in more_data1.upper():
                    #short_speak('thoát khỏi chế độ hẹn giờ')
                    continue_go = 0                                
                    break

                else:
                    time_in_data=check_time_in(more_data1)
                    if time_in_data ==[]:
                        pass
                    else:
                        break

        return time_in_data, continue_go
    friendly_name = find_hass_friendly_name(data)
    print(friendly_name)
    time_in_data=check_time_in(data)
    print(time_in_data)
    continue_go=1
    if friendly_name == []:
        abc = more_info_friendly(data,friendly_name)
        friendly_name =abc[1]
        data = abc[0]
        continue_go=abc[2]
        
    if continue_go ==1:
        if time_in_data == []:
            abcd = more_info_time(data,time_in_data)
            time_in_data = abcd[0]
            continue_go=abcd[1]
    if continue_go == 1:
        time_set = datetime.timedelta(hours=int(time_in_data[0]), minutes = int(time_in_data[1]),seconds=00)
        print(time_set)
        time_now_hour =strftime("%H")
        time_now_minute =strftime("%M")
        time_now_second =strftime("%S")
        time_now=datetime.timedelta(hours=int(time_now_hour), minutes = int(time_now_minute),seconds = int(time_now_second))
        
        second_delta = time_set-time_now
        
        secondelta=str(second_delta).split(":")
        
        second_delta_final = int(secondelta[0])*3600+int(secondelta[1])*60+int(secondelta[2])
        
    
    if len(friendly_name) !=0 and int(second_delta_final) >1:
        seconds=int(second_delta_final)
        print('[BOT]: OK')
        #short_speak('đã đặt hẹn giờ' )
        if 'HẸN GIỜ' in data:
            data=data.replace("HẸN GIỜ","")
            
        t1 = Timer(seconds,has_xuly,[data])
        t1.start()
    else:
        #short_speak('xin thử lại sau')
        print('dsfsdf')


class switch():

    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
        
    def turn_on(self):
        url = self.domain+'/api/services/switch/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}            
        payload = {'entity_id': 'switch.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã bật mở công tắc thành công')
            #short_speak('Đã bật mở công tắc thành công')                
            r=1
            return r                
        else:
            print('[BOT]: bật mở công tắc không thành công')
            #short_speak('bật mở công tắc không thành công')                                
            r=0
            return r                                
    def turn_off(self):
        url = self.domain+'/api/services/switch/turn_off'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'switch.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã tắt ngắt công tắc thành công')
            #short_speak('Đã tắt ngắt công tắc thành công')                
            r=1
            return r                
        else:
            print('[BOT]: tắt ngắt công tắc không thành công')
            #short_speak('tắt ngắt công tắc không thành công')                                
            r=0
            return r                                
    def domain_extract(self):
        rr='switch'
        return rr

class light():

    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
        
    def turn_on(self):
        url = self.domain+'/api/services/light/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'light.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã bật mở đèn thành công')
            #short_speak('Đã bật mở đèn thành công')                
            r=1
            return r                
        else:
            print('[BOT]: bật mở đèn không thành công')
            #short_speak('bật mở đèn không thành công')                                
            r=0
            return r                                
            
    def turn_off(self):
        url = self.domain+'/api/services/light/turn_off'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}        
        payload = {'entity_id': 'light.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã tắt ngắt đèn thành công')
            #short_speak('Đã tắt ngắt đèn thành công')                
            r=1
            return r                
        else:
            print('[BOT]: tắt ngắt đèn không thành công')
            #short_speak('tắt ngắt đèn không thành công')                                
            r=0
            return r                                            
    def domain_extract(self):
        rr='light'
        return rr

class fan():

    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
        
    def turn_on(self):
        url = self.domain+'/api/services/light/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'light.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã bật mở quạt thành công')
            #short_speak('Đã bật mở quạt thành công')                
            r=1
            return r                
        else:
            print('[BOT]: bật mở quạt không thành công')
            #short_speak('bật mở quạt không thành công')                                
            r=0
            return r                                
            
    def turn_off(self):
        url = self.domain+'/api/services/light/turn_off'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}        
        payload = {'entity_id': 'light.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã tắt ngắt quạt thành công')
            #short_speak('Đã tắt ngắt quạt thành công')                
            r=1
            return r                
        else:
            print('[BOT]: tắt ngắt quạt không thành công')
            #short_speak('tắt ngắt quạt không thành công')                                
            r=0
            return r                                
            
    def domain_extract(self):
        rr='fan'
        return rr

class cover():
    # Implement one of these methods.
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        """Open the cover."""
        url = self.domain+'/api/services/cover/open_cover'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'cover.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã mở thành công')
            #short_speak('Đã mở thành công')                
            r=1
            return r                
        else:
            print('[BOT]: Mở không thành công')
            #short_speak('Mở không thành công')                                
            r=0
            return r                                
    def turn_off(self):
        """Close the cover."""        
        url = self.domain+'/api/services/cover/close_cover'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'cover.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã đóng thành công')
            #short_speak('Đã đóng thành công')                
            r=1
            return r                
        else:
            print('[BOT]: Đóng không thành công')
            #short_speak('Đóng không thành công')                                
            r=0
            return r                                

    def domain_extract(self):
        rr='cover'
        return rr        

class media_player():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        url = self.domain+'/api/services/media_player/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}            
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã bật mở đài phát thành công')
            #short_speak('Đã bật mở đài phát thành công')                
            r=1
            return r                
        else:
            print('[BOT]: bật mở đài phát không thành công')
            #short_speak('bật mở đài phát không thành công')                                
            r=0
            return r                                
    def turn_off(self):
        url = self.domain+'/api/services/media_player/turn_off'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã tắt ngắt đài phát thành công')
            #short_speak('Đã tắt ngắt đài phát thành công')                
            r=1
            return r                
        else:
            print('[BOT]: tắt ngắt đài phát không thành công')
            #short_speak('tắt ngắt đài phát không thành công')                                
            r=0
            return r                                
    def media_play(self):
        url = self.domain+'/api/services/media_player/media_play'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}            
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã phát thành công')
            #short_speak('Đã phát thành công')                
            r=1
            return r                
        else:
            print('[BOT]: Phát không thành công')
            #short_speak('Phát không thành công')                                
            r=0
            return r                                
    def media_pause(self):
        url = self.domain+'/api/services/media_player/media_pause'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}           
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã dừng thành công')
            ##short_speak('Đã dừng thành công')                
            r=1
            return r                
        else:
            print('[BOT]: Dừng không thành công')
            ##short_speak('Dừng không thành công')                                
            r=0
            return r                                
    def domain_extract(self):
        rr='media_player'
        return rr

class script():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        url = self.domain+'/api/services/script/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'script.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã chạy kịch bản thành công')                
            r=1
            return r                
        else:
            print('[BOT]: Chạy kịch bản không thành công')
            ##short_speak('Chạy kịch bản không thành công')                                
            r=0
            return r                                
    def domain_extract(self):
        rr='script'
        return rr

class automation():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        url = self.domain+'/api/services/automation/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}
        payload = {'entity_id': 'automation.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã kích hoạt tự động hóa thành công')
            ##short_speak('Đã kích hoạt tự động hóa thành công')                
            r=1
            return r                
        else:
            print('[BOT]: Kích hoạt tự động hóa không thành công')
            ##short_speak('Kích hoạt tự động hóa không thành công')                                
            r=0
            return r                                
    def turn_off(self):
        url = self.domain+'/api/services/automation/turn_off'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}
        payload = {'entity_id': 'automation.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã vô hiệu tự động hóa thành công')
            ##short_speak('Đã vô hiệu tự động hóa thành công')                
            r=1
            return r                
        else:
            print('[BOT]: Vô hiệu tự động hóa không thành công')
            ##short_speak('Vô hiệu tự động hóa không thành công')                                
            r=0
            return r                                
    def domain_extract(self):
        rr='automation'
        return rr

class scene():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        url = self.domain+'/api/services/scene/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}
        payload = {'entity_id': 'scene.'+self.entity_id_ex}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print('')
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã bật mở ngữ ảnh thành công')
            ##short_speak('Đã bật mở ngữ ảnh thành công')                
            r=1
            return r                
        else:
            print('[BOT]: bật mở ngữ ảnh không thành công')
            ##short_speak('bật mở ngữ ảnh không thành công')                                
            r=0
            return r                                
    def domain_extract(self):
        rr='scene'
        return rr

class input_select():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
        
    def set_option(self,option):
        url = self.domain+'/api/services/input_select/select_option'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}           
        payload = {'entity_id': 'input_select.'+self.entity_id_ex, 'option':option}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if str(r)=='<Response [200]>':
            print('[BOT]: Đã nhập thành công')
            ##short_speak('Đã nhập thành công')                
            r=1
            return r                
        else:
            print('[BOT]: Nhập không thành công')
            ##short_speak('Nhập không thành công')                                
            r=0
            return r                                
    def domain_extract(self):
        rr='input_select'
        return rr
        

class sensor():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def domain_extract(self):
        rr='sensor'
        return rr

class binary_sensor():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def domain_extract(self):
        rr='binary_sensor'
        return rr

class climate():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def domain_extract(self):
        rr='climate'
        return rr
    def set_temperature(self,degree):
        url = self.domain+'/api/services/climate/set_temperature'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}
        payload = {'entity_id': 'climate.'+self.entity_id_ex, 'temperature':degree}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã thiết lập nhiệt độ thành công')
                r=1
                return r
        except:
            r = 0
            return r
            
class define():
    def __init__(self,domain_ex=[], entity_id_ex=[],domain='',longlivedtoken=''):
        self.domain_ex = domain_ex
        self.entity_id_ex= entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def define(self):
        if self.domain_ex == 'switch':
            self.object = switch(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'automation':
            self.object = automation(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'device_tracker':
            self.object = device_tracker(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'alarm_control_panel':
            self.object = alarm_control_panel(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex =='script':
            self.object = script(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex =='scene':
            self.object = scene(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'light':
            self.object = light(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'sensor':
            self.object = sensor(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'binary_sensor':
            self.object = binary_sensor(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'media_player':
            self.object = media_player(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'input_select':
            self.object = input_select(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'climate':
            self.object = climate(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'cover':
            self.object = cover(self.entity_id_ex,self.domain,self.longlivedtoken)            
        return self.object
        
def check_state(domain_ex=[],entity_id_ex=[]):
    url = domain + '/api/states/'+ domain_ex+ '.'+ entity_id_ex
    headers = {'Authorization': 'Bearer '+ longlivedtoken,'content-type': 'application/json',}
    r = requests.get(url, headers=headers)
    # print(str(r))
    r = r.json()
    qq=r
    r = r['state']
    if r == 'off':
        r = 'tắt hoặc đóng'
    elif r == 'on':
        r= 'bật hoặc mở'
    else:
        pass
    return r,qq
    
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