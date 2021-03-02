# Cài thêm 
# pip install bing_tr requests fuzzywuzzy pytest jmespath coloredlogs ratelimit
from speaking import speak, short_speak
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from underthesea import pos_tag
import googlemaps
from datetime import datetime


from termcolor import colored
import requests
from requests import get
import datetime
import random
from datetime import timedelta
import gih
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
latlong=gih.get_config('toado')
list_day= gih.get_request('request_day')         
request_day= gih.get_request('request_day')         
response_day=gih.get_response('response_day')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')
your_darksky_api=gih.get_config('api_darksky')

google_api=gih.get_config('google_api')
gmaps = googlemaps.Client(key=google_api)
g_ip = 0    # Global Variable of IP Address
g_lat = latlong[0]   # Global Variable of Latitude
g_lon = latlong[1]   # Global Variable of Longnitude
x = datetime.datetime.now()
data ='TỪ HÀ NỘI ĐI HỒ CHÍ MINH BAO XA'
def main(data):
    pos_tag(data)
    print(str(pos_tag))
    # print('[BOT]: XỬ LÝ CÂU LỆNH ĐO KHOẢNG CÁCH: '+data)
    
    # print('Bạn đang ở quốc gia: '+ ip_finder()[0]+' mã số điện thoại là +'+ip_finder()[1]+ ' nói tiếng '+ip_finder()[2]+' thủ đô là '+ip_finder()[3])
    # print('Bạn đang ở tỉnh thành '+ip_finder()[5]+ ' và khu vực '+ip_finder()[5])
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
def ip_finder():
    global g_ip  # Global Variable of IP Address
    global g_lat # Global Variable of Latitude
    global g_lon # Global Variable of Longnitude
    if(g_ip==0):
        ip = get('https://api.ipify.org')  # Fetching Current Device Public IP address
        if ip.status_code != 200:
            raise ApiError('GET /tasks/ {}'.format(ip.status_code))
        else:
            ip = ip.text
            g_ip = ip
    yourapi = '128979ae3de728602f249354a85ac508' # Your API key
    ip_url = 'http://api.ipstack.com/'+g_ip+'?access_key='+yourapi
    jsn_ip = requests.get(ip_url)
    if jsn_ip.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(jsn_ip.status_code))
    else:
        ip_result = jsn_ip.json()        
        g_lat = ip_result['latitude']      # Set the Latitude
        g_lon = ip_result['longitude']     # Set the Longitude
        location_country=ip_result['country_name']
        location_calling_code=ip_result['location']['calling_code']
        location_capital=ip_result['location']['capital']        
        location_region=ip_result['region_name']        
        location_city=ip_result['city']
        location_language=str(ip_result['location']['languages'][0]['native'])
    return location_country,location_calling_code,location_language,location_capital,location_region,location_city,
    
def weather_json(mode,arr):
    global g_ip  # Global Variable of IP Address
    global g_lat # Global Variable of Latitude
    global g_lon # Global Variable of Longnitude
    if (mode=='ip' or mode=='IP'):
        if(arr==0):
            if(g_ip==0):
                ip_finder()  # For Collecting IP,Lat,Lon
            else:
                g_ip = arr
                ip_finder()  # For Collecing the Lat Lon
        else:
                g_ip = arr
                ip_finder()  # For Collecing the Lat Lon
    elif (mode=='LATLON' or mode=='latlon'):
        if(arr[0]!=0 and arr[1]!=0  ):
            g_lat = arr[0]
            g_lon = arr[1]
        else:
            g_ip = 0
            g_lat = latlong[0]
            g_lon = latlong[1]
            ip_finder()
    else:
        g_lat = latlong[0]
        g_lon = latlong[1]
        ip_finder()
    if(g_lat==0 or g_lon==0):
        return('Error Input')
    else:

        #url = 'https://api.darksky.net/forecast/'+your_darksky_api+'/'+str(g_lat)+','+str(g_lon)+'?lang=vi'
        url = 'https://api.darksky.net/forecast/'+your_darksky_api+'/'+str(g_lat)+','+str(g_lon)+'?lang=vi'
        jsn = requests.get(url)
        if jsn.status_code != 200:
            raise ApiError('GET /tasks/ {}'.format(jsn.status_code))
        else:
            result = jsn.json()
            return(result)
def current(mod,arr):
    result = weather_json(mod,arr)
    dic={} # Result Dictionary
    fer = result['currently']['temperature']
    cel = (fer-32)*(5/9) # Fahrenheit to Celsius conversion 
    hum = int(result['currently']['humidity'] * 100) # Humidity on percentage
    dic["overal"]=result['currently']['summary']
    dic["temp"]="%.1f" % cel
#    dic["Current Temperature in F"]="%.1f" %fer
    dic["hum"]=hum
    dic["wind"]=result['currently']['windSpeed']
#    dic["Current Wind Pressure"]=result['currently']['pressure']
    return(dic)
def hourly(mod,arr):
    result = weather_json(mod,arr)
    dic={'today':{"%.1f"%i:{} for i in range(25)},'tomorrow':{"%.1f"%i:{} for i in range(25)}}
    for i in range (1,49):
        fer = result['hourly']['data'][i]['temperature']
        cel = (fer-32)*(5/9)                 # Fahrenheit to Celsius conversion 
        hum = int(result['hourly']['data'][i]['humidity'] * 100)  # Humidity on percentage
        if(i<=24):
            dic['today']["%.1f" %i]["overal"]= result['hourly']['data'][i]['summary']
            dic['today']["%.1f" %i]["temp"]="%.1f" % cel
#            dic['today']["%.1f" %i]["Temperature in F"]="%.1f" %fer
            dic['today']["%.1f" %i]["hum"]=hum
            dic['today']["%.1f" %i]["wind"]=result['hourly']['data'][i]['windSpeed']
#            dic['today']["%.1f" %i]["Wind Pressure"]=result['hourly']['data'][i]['pressure']
        else:
            tm  = i - 24
            dic['tomorrow']["%.1f" %tm]["overal"]= result['hourly']['data'][i]['summary']
            dic['tomorrow']["%.1f" %tm]["temp"]="%.1f" % cel
#            dic['tomorrow']["%.1f" %tm]["Temperature in F"]="%.1f" %fer
            dic['tomorrow']["%.1f" %tm]["hum"]=hum
            dic['tomorrow']["%.1f" %tm]["wind"]=result['hourly']['data'][i]['windSpeed']
#            dic['tomorrow']["%.1f"%tm]["Wind Pressure"]=result['hourly']['data'][i]['pressure']
    return(dic)
def weekly(mod,arr):
    result = weather_json(mod,arr)
    dic = {}
    for i in range (1,7):
        r_date = x+datetime.timedelta(i)
        dic[r_date.strftime("%d")]={}
    for i in range (1,7):
        r_date = x+datetime.timedelta(i)
        s = []
        mfer = result['daily']['data'][i]['temperatureMax']
        mcel = (mfer-32)*(5/9)                # Fahrenheit to Celsius conversion
        Mfer = result['daily']['data'][i]['temperatureMin']
        Mcel = (Mfer-32)*(5/9)              # Fahrenheit to Celsius conversion
        hum = int(result['daily']['data'][i]['humidity'] * 100) # Humidity on percentage
        dic[r_date.strftime("%d")]["overal"]=result['daily']['data'][i]['summary']
        dic[r_date.strftime("%d")]["mintemp"]="%.1f" % Mcel
#        dic[r_date.strftime("%d")]["Max Temperature in F"]="%.1f" %Mfer
        dic[r_date.strftime("%d")]["maxtemp"]= "%.1f" % mcel
#        dic[r_date.strftime("%d")]["Min Temperature in F"]="%.1f" %mfer
        dic[r_date.strftime("%d")]["hum"]=hum
        dic[r_date.strftime("%d")]["wind"]=result['daily']['data'][i]['windSpeed']
#        dic[r_date.strftime("%d")]["Wind Pressure"]=result['daily']['data'][i]['pressure']
    return(dic)

def check_last_day():
    y = x-datetime.timedelta(1)
    day = '0'+str(y.day)   
    tt = weekly('latlon',latlong)
    speakct=str('Hôm qua '+tt[day]['overal']+', Nhiệt độ thấp nhất '+replace_point(str(tt[day]['mintemp'])) +' độ C, Nhiệt độ cao nhất '+replace_point(str(tt[day]['maxtemp'])) +' độ C,  độ ẩm là ' + replace_point(str(tt[day]['hum'])) + ' phần trăm, tốc độ gió trung bình ' + replace_point(str(tt[day]['wind'])) + ' ki lô mét trên giờ.')
    speak(speakct)
    
def check_to_day():
    tt = current('latlon',latlong)
    speakct=str('Hôm nay '+tt['overal']+', Nhiệt độ là '+replace_point(str(tt['temp'])) +' độ C,  độ ẩm là ' + replace_point(str(tt['hum'])) + ' phần trăm, tốc độ gió trung bình ' + replace_point(str(tt['wind'])) + ' ki lô mét trên giờ.')
    speak(speakct)
    
def check_tomorrow():
    y = x + datetime.timedelta(1)
    if len(str(y.day))==1:
        day = '0'+str(y.day)    
        # print(day)
    elif len(str(y.day))==2:
        day = str(y.day)    
        # print(day)        
    tt = weekly('latlon',latlong)        
    # print(str(tt))
    speakct=str('Ngày mai '+tt[day]['overal']+', Nhiệt độ thấp nhất '+replace_point(str(tt[day]['mintemp'])) +' độ C, Nhiệt độ cao nhất '+replace_point(str(tt[day]['maxtemp'])) +' độ C,  độ ẩm là ' + replace_point(str(tt[day]['hum'])) + ' phần trăm, tốc độ gió trung bình ' + replace_point(str(tt[day]['wind'])) + ' ki lô mét trên giờ.')
    speak(speakct)
    
def check_next_day():
    y = x + datetime.timedelta(2)
    if len(str(y.day))==1:
        day = '0'+str(y.day)    
        # print(day)
    elif len(str(y.day))==2:
        day = str(y.day)    
        # print(day)                
    tt = weekly('latlon',latlong)        
    speakct=str('Ngày kia '+tt[day]['overal']+', Nhiệt độ thấp nhất '+replace_point(str(tt[day]['mintemp'])) +' độ C, Nhiệt độ cao nhất '+replace_point(str(tt[day]['maxtemp'])) +' độ C,  độ ẩm là ' + replace_point(str(tt[day]['hum'])) + ' phần trăm, tốc độ gió trung bình ' + replace_point(str(tt[day]['wind'])) + ' ki lô mét trên giờ.')
    speak(speakct)

def replace_point(data):
    data = data.replace('.',',')
    return data


if __name__ == '__main__':
    main(data)        