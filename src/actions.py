#!/usr/bin/env python

#This is different from AIY Kit's actions
#Copying and Pasting AIY Kit's actions commands will not work

# from kodijson import Kodi, PLAYER_VIDEO
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import spotipy.oauth2 as oauth2
from pushbullet import Pushbullet
# from mediaplayer import api
from youtube_search_engine import google_cloud_api_key
from googletrans import Translator
from youtube_search_engine import youtube_search
from youtube_search_engine import youtube_stream_link
from google.cloud import texttospeech
from gtts import gTTS
import requests
import mediaplayer
import os
import os.path
from os import path
import uuid, urllib
try:
    import RPi.GPIO as GPIO
except Exception as e:
    GPIO = None
import time
import re
import subprocess
import aftership
import feedparser
import json
import urllib.request
import pafy
import pychromecast
import spotipy
import pprint
import yaml
import pywemo
import random
import threading
from termcolor import colored
from os import listdir
import urllib
from urllib.request import urlretrieve
ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))


with open('{}/src/config.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    configuration = yaml.load(conf)

with open('{}/src/lang.yaml'.format(ROOT_PATH),'r', encoding='utf8') as lang:
    langlist = yaml.load(lang)

TTSChoice=''
if configuration['TextToSpeech']['Choice']=="Google Cloud":
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""):
        if configuration['TextToSpeech']['Google_Cloud_TTS_Credentials_Path']!="ENTER THE PATH TO YOUR TTS CREDENTIALS FILE HERE":
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = configuration['TextToSpeech']['Google_Cloud_TTS_Credentials_Path']
            TTSChoice='GoogleCloud'
            # Instantiates a client
            client = texttospeech.TextToSpeechClient()
        else:
            print("Set the path to your Google cloud text to speech credentials in the config.yaml file. Using gTTS for now.....")
            TTSChoice='GTTS'
    else:
        TTSChoice='GoogleCloud'
        # Instantiates a client
        client = texttospeech.TextToSpeechClient()
if configuration['TextToSpeech']['Choice']=="VIETTEL":
    TTSChoice='VIETTEL'
else:
    TTSChoice='GTTS'


domoticz_devices=''
Domoticz_Device_Control=False
bright=''
hexcolour=''

keywordfile= '{}/src/keywords_vn.yaml'.format(ROOT_PATH)
with open(keywordfile,'r' , encoding='utf8') as conf:
    custom_action_keyword = yaml.load(conf)


# Get devices list from domoticz server
if configuration['Domoticz']['Domoticz_Control']=='Enabled':
    Domoticz_Device_Control=True
    try:
        domoticz_response = requests.get("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=devices&filter=all&order=Name",verify=False)
        domoticz_devices=json.loads(domoticz_response.text)
        with open('{}/domoticz_device_list.json'.format(USER_PATH), 'w') as devlist:
            json.dump(domoticz_devices, devlist)
    except requests.exceptions.ConnectionError:
        print("Domoticz server not online")
else:
    Domoticz_Device_Control=False

Spotify_credentials=False
Youtube_credentials=False
if configuration['Spotify']['client_id']!= 'ENTER YOUR SPOTIFY CLIENT ID HERE' and configuration['Spotify']['client_secret']!='ENTER YOUR SPOTIFY CLIENT SECRET HERE':
    Spotify_credentials=True
if configuration['Google_cloud_api_key']!='ENTER-YOUR-GOOGLE-CLOUD-API-KEY-HERE':
    Youtube_credentials=True

# Spotify Declarations
# Register with spotify for a developer account to get client-id and client-secret
if Spotify_credentials:
    client_id = configuration['Spotify']['client_id']
    client_secret = configuration['Spotify']['client_secret']
    username=configuration['Spotify']['username']
    credentials = oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify_token = credentials.get_access_token()


#Import VLC player
vlcplayer=mediaplayer.vlcplayer()



#Google Music Declarations
song_ids=[]
track_ids=[]


#Login with default kodi/kodi credentials
#kodi = Kodi("http://localhost:8080/jsonrpc")

#Login with custom credentials
# # Kodi("http://IP-ADDRESS-OF-KODI:8080/jsonrpc", "username", "password")
# kodiurl=("http://"+str(configuration['Kodi']['ip'])+":"+str(configuration['Kodi']['port'])+"/jsonrpc")
# kodi = Kodi(kodiurl, configuration['Kodi']['username'], configuration['Kodi']['password'])
# musicdirectory=configuration['Kodi']['musicdirectory']
# videodirectory=configuration['Kodi']['videodirectory']
# windowcmd=configuration['Kodi']['windowcmd']
# window=configuration['Kodi']['window']

if GPIO!=None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #Number of entities in 'var' and 'PINS' should be the same
    var = configuration['Raspberrypi_GPIO_Control']['lightnames']
    gpio = configuration['Gpios']['picontrol']
    for pin in gpio:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    #Servo pin declaration
    servopin=configuration['Gpios']['servo'][0]
    GPIO.setup(servopin, GPIO.OUT)
    pwm=GPIO.PWM(servopin, 50)
    pwm.start(0)

    #Stopbutton
    stoppushbutton=configuration['Gpios']['stopbutton_music_AIY_pushbutton'][0]
    GPIO.setup(stoppushbutton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIOcontrol=True
else:
    GPIOcontrol=False

#Number of scripts and script names should be the same
scriptname=configuration['Script']['scriptname']
scriptcommand=configuration['Script']['scriptcommand']

#Number of station names and station links should be the same
stnname=configuration['Radio_stations']['stationnames']
stnlink=configuration['Radio_stations']['stationlinks']
stnradio=configuration['Radio_stations']['stationradio']

#IP Address of ESP
ip=configuration['ESP']['IP']

#Declaration of ESP names
devname=configuration['ESP']['devicename']
devid=configuration['ESP']['deviceid']

playshell = None

#Initialize colour list
clrlist=[]
clrlistfullname=[]
clrrgblist=[]
clrhexlist=[]
with open('{}/src/colours.json'.format(ROOT_PATH), 'r') as col:
     colours = json.load(col)
for i in range(0,len(colours)):
    clrname=colours[i]["name"]
    clrnameshort=clrname.replace(" ","",1)
    clrnameshort=clrnameshort.strip()
    clrnameshort=clrnameshort.lower()
    clrlist.append(clrnameshort)
    clrlistfullname.append(clrname)
    clrrgblist.append(colours[i]["rgb"])
    clrhexlist.append(colours[i]["hex"])


#Parcel Tracking declarations
aftership.api_key=configuration['AFTERSHIP']['Key']
aftershiptracking=False
if configuration['AFTERSHIP']['Key']=='ENTER YOUR AFTERSHIP KEY HERE':
    aftershiptracking=False
else:
    aftershiptracking=True
    couriers = configuration['AFTERSHIP']['Parcels']['Courier_Name']
    trackingids = configuration['AFTERSHIP']['Parcels']['Tracking_Code']


#RSS feed URLS
worldnews = "http://feeds.bbci.co.uk/news/world/rss.xml"
technews = "http://feeds.bbci.co.uk/news/technology/rss.xml"
topnews = "http://feeds.bbci.co.uk/news/rss.xml"
sportsnews = "http://feeds.feedburner.com/ndtvsports-latest"
quote = "http://feeds.feedburner.com/brainyquote/QUOTEBR"

##Speech and translator declarations
translator = Translator()
femalettsfilename="/tmp/female-say.mp3"
malettsfilename="/tmp/male-say.wav"
ttsfilename="/tmp/gcloud.mp3"
language=configuration['Language']['Choice']
translanguage=language.split('-')[0]
gender=''
if configuration['TextToSpeech']['Voice_Gender']=='Male':
    gender='Male'
elif configuration['TextToSpeech']['Voice_Gender']=='Female':
    gender='Female'
else:
    gender='Female'

if configuration['Pushbullet']['Pushbullet_API_KEY']!='ENTER YOUR PUSHBULLET KEY HERE':
    pb=Pushbullet(configuration['Pushbullet']['Pushbullet_API_KEY'])
else:
    pb=None

#Function for google KS custom search engine
def kickstrater_search(query):
    service = build("customsearch", "v1",
            developerKey=google_cloud_api_key)
    res = service.cse().list(
        q=query,
        cx = '012926744822728151901:gefufijnci4',
        ).execute()
    return res


#Function for google Gaana custom search engine
def gaana_search(query):
    service = build("customsearch", "v1",
            developerKey=google_cloud_api_key)
    res = service.cse().list(
        q=query,
        cx = '012926744822728151901:jzpzbzih5hi',
        ).execute()
    return res

#gTTS
def gttssay(phrase,saylang,specgender):
    tts = gTTS(text=phrase, lang='vi')
    tts.save(femalettsfilename)
    if specgender=='Male':
        os.system('sox ' + femalettsfilename + ' ' + malettsfilename + ' pitch +450')
        os.remove(femalettsfilename)
        os.system('aplay ' + malettsfilename)
        os.remove(malettsfilename)
    elif specgender=='Female':
        os.system("mpg123 "+femalettsfilename)
        os.remove(femalettsfilename)
#tts Viettel
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# import os.path

#from termcolor import colored
#from mutagen.mp3 import MP3


token='HXddsd-TPRwwS4AqRKwTCh-qlyziwWcBOzmbTSzDW3XgT8yY5J-Gx-2BFfz1sW-C'
#speak_volume=1.0
voice_name='hcm-diemmy2'
speed=1.0
pitch=0
def stt_viettel(phrase):
    text=phrase
    #print(colored('[BOT-TTS-VIETTEL]: '+text,'green'))
    #import time            
    #HTTP Request
    url = 'https://viettelgroup.ai/voice/api/tts/v1/rest/syn'
    #Header Parameters
    #hn-quynhanh2, hcm-diemmy2
    headers = {'Content-type': 'application/json', 'token': token}
    # Body Parameters                        
    data = {'text': text, "voice": voice_name, "id": "2", "without_filter": False, "speed": speed, "tts_return_option": 3}
    #Get response from Server  
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    # Open audio file                             
    uniq_filename = '/tmp/tts_vtcc' + str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'
    audio_file= open(uniq_filename, 'wb')
    audio_file.write(response.content)
    audio_file.close()
    os.system("mpg123 "+uniq_filename)
    os.remove(uniq_filename)
    # mixer.music.load(uniq_filename)
    # mixer.music.set_volume(speak_volume)            
    # mixer.music.play()                                    
    # audio = MP3(uniq_filename)
    # t = float (audio.info.length)
    # # print ('Time delay :'+ str(t))
    # time.sleep(round(t)+1)
#Google Cloud Text to Speech
def gcloudsay(phrase,lang):
    try:
        if gender=='Male':
            gcloudgender=texttospeech.enums.SsmlVoiceGender.MALE
        else:
            gcloudgender=texttospeech.enums.SsmlVoiceGender.FEMALE

        synthesis_input = texttospeech.types.SynthesisInput(text=phrase)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code=lang,
            ssml_gender=gcloudgender)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open(ttsfilename, 'wb') as out:
            out.write(response.audio_content)
        if gender=='Male' and lang=='vi':
            os.system('sox ' + ttsfilename + ' ' + malettsfilename + ' pitch -450')
            os.remove(ttsfilename)
            os.system('aplay ' + malettsfilename)
            os.remove(malettsfilename)
        else:
            os.system("mpg123 "+ttsfilename)
            os.remove(ttsfilename)
    except google.api_core.exceptions.ResourceExhausted:
        print("Google cloud text to speech quota exhausted. Using GTTS. Make sure to change the choice in config.yaml")
        gttssay(phrase,lang)

#Word translator
def trans(words,destlang,srclang):
    transword= translator.translate(words, dest=destlang, src=srclang)
    transword=transword.text
    transword=transword.replace("Text, ",'',1)
    transword=transword.strip()
    print(transword)
    return transword

#Text to speech converter with translation
def say(words,sourcelang=None,destinationlang=None):
    if sourcelang!=None and destinationlang!=None:
        if TTSChoice=='GoogleCloud':
            sayword=trans(words,destinationlang,sourcelang)
            gcloudsay(sayword,language)
        elif TTSChoice=='GTTS':
            sayword=trans(words,destinationlang,sourcelang)
            gttssay(sayword,translanguage,gender)
        elif TTSChoice=='VIETTEL':
            sayword=trans(words,destinationlang,sourcelang)
            stt_viettel(sayword)
    else:
        if sourcelang==None:
            sourcelanguage='vi'
        else:
            sourcelanguage=sourcelang
        if sourcelanguage!=translanguage:
            sayword=trans(words,translanguage,sourcelanguage)
        else:
            sayword=words
        if TTSChoice=='GoogleCloud':
            gcloudsay(sayword,language)
        elif TTSChoice=='GTTS':
            gttssay(sayword,translanguage,gender)
        elif TTSChoice=='VIETTEL':
            stt_viettel(sayword)


#Function to get HEX and RGB values for requested colour
def getcolours(phrase):
    usrclridx=idx=phrase.find(custom_action_keyword['Dict']['To'])
    usrclr=query=phrase[usrclridx:]
    usrclr=usrclr.replace(custom_action_keyword['Dict']['To'],"",1)
    usrclr=usrclr.replace("'","",1)
    usrclr=usrclr.replace("}","",1)
    usrclr=usrclr.strip()
    usrclr=usrclr.replace(" ","",1)
    usrclr=usrclr.lower()
    print(usrclr)
    try:
        for colournum, colourname in enumerate(clrlist):
            if usrclr in colourname:
               RGB=clrrgblist[colournum]
               red,blue,green=re.findall('\d+', RGB)
               hexcode=clrhexlist[colournum]
               cname=clrlistfullname[colournum]
               print(cname)
               break
        return red,blue,green,hexcode,cname
    except UnboundLocalError:
        say("Sorry unable to find a matching colour")


#Function to convert FBG to XY for Hue Lights
def convert_rgb_xy(red,green,blue):
    try:
        red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else red / 12.92
        green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else green / 12.92
        blue = pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else blue / 12.92
        X = red * 0.664511 + green * 0.154324 + blue * 0.162028
        Y = red * 0.283881 + green * 0.668433 + blue * 0.047685
        Z = red * 0.000088 + green * 0.072310 + blue * 0.986039
        x = X / (X + Y + Z)
        y = Y / (X + Y + Z)
        return x,y
    except UnboundLocalError:
        say("No RGB values given")

#Custom text to speak notification
def notify_tts(phrase):
    word=(custom_action_keyword['Keywords']['notify_TTS'][0]).lower()
    voice_notify = phrase.replace(word, "")
    voice_notify.strip()
    say(voice_notify)

#Run scripts
def script(phrase):
    for num, name in enumerate(scriptname):
        if name.lower() in phrase:
            conv=scriptname[num]
            command=scriptcommand[num]
            print (command)
            say("Running " +conv)
            os.system(command)

#Radio Station Streaming
def radio(phrase):
    conv = None
    for num, name in reversed(list(enumerate(stnname))):
        if name.lower() in phrase:
            station=stnlink[num]
            conv=stnradio[num]
            print (station)
            break
    if conv is not None:
        say("Tuning into " + conv)
        vlcplayer.media_manager(station,'Radio')
        vlcplayer.media_player(station)
    else:
        say("Station not found")


#ESP6266 Devcies control
def ESP(phrase):
    for num, name in enumerate(devname):
        if name.lower() in phrase:
            dev=devid[num]
            if custom_action_keyword['Dict']['On'] in phrase:
                ctrl='=ON'
                say("Turning On " + name)
            elif custom_action_keyword['Dict']['Off'] in phrase:
                ctrl='=OFF'
                say("Turning Off " + name)
            rq = requests.head("http://"+ip + dev + ctrl)


#Stepper Motor control
def SetAngle(angle):
    if GPIOcontrol:
        duty = angle/18 + 2
        GPIO.output(servopin, True)
        say("Moving motor by " + str(angle) + " degrees")
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        pwm.ChangeDutyCycle(0)
        GPIO.output(servopin, False)
    else:
        say("GPIO controls, is not supported for your device.")



def stop():
    vlcplayer.stop_vlc()

#Parcel Tracking
def parcel_tracking(*, tracking_id=None, slug=None, tracking_number=None, fields=None):
    try:
        result = aftership.tracking.get_tracking(tracking_id=tracking_id,
                                                 slug=slug,
                                                 tracking_number=tracking_number,
                                                 fields=','.join(fields))
    except aftership.exception.NotFound:
        return None
    return result['tracking']

def track():
    if aftershiptracking==False:
        say("Aftership API key has not been entered in the config file.")
    else:
        if len(couriers) != len(trackingids):
            say("Number of courier names and the tracking ids are not matching. Please check the config file.")
        else:
            for x in range(0,len(couriers)):
                trackinginfo=parcel_tracking(slug=couriers[x],tracking_number=trackingids[x],fields=[])
                if trackinginfo==None:
                    say("Looks like the details have not been added to the Aftership tracking database.")
                else:
                    numcheck=len(trackinginfo['checkpoints'])
                    description = trackinginfo['checkpoints'][numcheck-1]['message']
                    parcelid=trackinginfo['tracking_number']
                    trackinfo= ("Parcel Number " + str(x+1)+ " with tracking id " + parcelid + " has "+ description)
                    say(trackinfo)
                    #time.sleep(5)



#RSS Feed Reader
def feed(phrase):
    if 'world news' in phrase:
        URL=worldnews
    elif 'top news' in phrase:
        URL=topnews
    elif 'sports news' in phrase:
        URL=sportsnews
    elif 'tech news' in phrase:
        URL=technews
    elif (custom_action_keyword['Keywords']['RSS'][1]).lower() in phrase:
        URL=quote
    numfeeds=10
    feed=feedparser.parse(URL)
    feedlength=len(feed['entries'])
    print(feedlength)
    if feedlength<numfeeds:
        numfeeds=feedlength
    title=feed['feed']['title']
    say(title)
    if GPIOcontrol:
        #To stop the feed, press and hold stop button
        while GPIO.input(stoppushbutton):
            for x in range(0,numfeeds):
                content=feed['entries'][x]['title']
                print(content)
                say(content)
                summary=feed['entries'][x]['summary']
                print(summary)
                say(summary)
                if not GPIO.input(stoppushbutton):
                  break
            if x == numfeeds-1:
                break
            else:
                continue
    else:
        print("GPIO controls, is not supported for your device. You need to wait for feeds to automatically stop")


##--------------Start of send clickatell sms----------------------
#Function to send SMS with Clickatell api
recivernum=configuration['Clickatell']['Reciever']
clickatell_api=configuration['Clickatell']['Clickatell_API']

def sendClickatell(number, message):
    response=requests.get('https://platform.clickatell.com/messages/http/send?apiKey=' + clickatell_api + '&to=' + number + '&content=' + message)
    if response.status_code == 202:
        say("SMS message sent")
    else:
        say("Error sending SMS message. Check your settings")

def sendSMS(query):
    if clickatell_api != 'ENTER_YOUR_CLICKATELL_API':
        for num, name in enumerate(configuration['Clickatell']['Name']):
            if name.lower() in query:
                conv=recivernum[num]
                command=(custom_action_keyword['Keywords']['Send_sms_clickatell'][0]).lower()
                msg=query.replace(command, "")
                message=msg.replace(name.lower(), "")
                message=message.strip()
                print(message + " , " + name + " , " + conv)
                say("Sends SMS message " + message + " to " + name)
                sendClickatell(conv, message)
    else:
        say("You need to enter Clickatell API")





#----------Getting urls for YouTube autoplay-----------------------------------
def fetchautoplaylist(url,numvideos):
    videourl=url
    autonum=numvideos
    autoplay_urls=[]
    autoplay_urls.append(videourl)
    for i in range(0,autonum):
        response=urllib.request.urlopen(videourl)
        webContent = response.read()
        webContent = webContent.decode('utf-8')
        idx=webContent.find("Up next")
        getid=webContent[idx:]
        idx=getid.find('<a href="/watch?v=')
        getid=getid[idx:]
        getid=getid.replace('<a href="/watch?v=',"",1)
        getid=getid.strip()
        idx=getid.find('"')
        videoid=getid[:idx]
        videourl=('https://www.youtube.com/watch?v='+videoid)
        if not videourl in autoplay_urls:
            i=i+1
            autoplay_urls.append(videourl)
        else:
            i=i-1
            continue
##    print(autoplay_urls)
    return autoplay_urls






#-----------------Start of Functions for YouTube Streaming---------------------

def YouTube_Autoplay(phrase):
    try:
        urllist=[]
        currenttrackid=0
        track=phrase
        track = track.replace(custom_action_keyword['Keywords']['YouTube_music_stream'][0],'')
        #track = track.replace(custom_action_keyword['Keywords']['Phatmotbai'][1],'')
        track=track.strip()
        #say("Phát danh sách "+track)
        print(track)
        autourls=youtube_search(track,10) # Maximum of 10 URLS
        print(autourls)
        #say("Adding autoplay links to the playlist")
        for i in range(0,len(autourls)):
            audiostream,videostream=youtube_stream_link(autourls[i])
            streamurl=audiostream
            urllist.append(streamurl)
        if not urllist==[]:
                vlcplayer.media_manager(urllist,'YouTube')
                vlcplayer.youtube_player(currenttrackid)
        else:
            say("Unable to find songs matching your request")

    except Exception as e:
        print(e)
        say('Encountered an exception please check the logs.')

def YouTube_No_Autoplay(phrase):
    urllist = []
    currenttrackid = 0
    track = phrase
    result = None
    track = track.replace(custom_action_keyword['Keywords']['YouTube_music_stream'][0],'')
    track = track.replace(custom_action_keyword['Keywords']['Phat_mot_bai'][0],'')
    track = track.replace(custom_action_keyword['Keywords']['Phat_mot_bai'][1],'')
    track = track.replace('zing','')
    track = track.strip()
    print("Tìm bài hát trên zingmp3.vn: "+track+"...")
    say('phát bài hát '+track+'trên zing.vn')
    try:
        resp = requests.get('http://ac.mp3.zing.vn/complete/desktop?type=song&query='+urllib.parse.quote(track))
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        songID = obj["data"][1]['song'][0]['id']
        songUrl= "https://mp3.zing.vn/bai-hat/"+songID+".html"
        print(songUrl)
        resp = requests.get(songUrl)
        #print(resp.text)
        key = re.findall('data-xml="\/media\/get-source\?type=audio&key=([a-zA-Z0-9]{20,35})', resp.text)
        # # key = re.findall('data-xml="\/media\/get-source\?type=video&key=([a-zA-Z0-9]{20,35})', resp.text)
        songApiUrl = "https://mp3.zing.vn/xhr/media/get-source?type=audio&key="+key[0]
        resp = requests.get(songApiUrl)
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        #print(str(obj))
        mp3Source = "https:"+obj["data"]["source"]["128"]
        realURLdata = requests.get(mp3Source,allow_redirects=False)
        #print(realURLdata)
        realURL = realURLdata.headers['Location']
        file_name, headers = urlretrieve(realURL)
        print(realURL)
        result=file_name
        if result is not None:
            #fullurl=result
            vlcplayer.media_manager(result,'zing')
            vlcplayer.media_player(result)
        else:
            say('Không tìm thấy bài hát yêu cầu của bạn trên zing.vn thực hiện phát bài hát trên yotube') 
        #say("Phát bài hát "+track)
            print(track)
            urlid=youtube_search(track)
            if urlid is not None:
                fullurl="https://www.youtube.com/watch?v="+urlid
                audiostream,videostream=youtube_stream_link(fullurl)
                streamurl=audiostream
                urllist.append(streamurl)
                vlcplayer.media_manager(urllist,'YouTube')
                vlcplayer.youtube_player(currenttrackid)
            else:
                say("Unable to find songs matching your request")            
    except (IndexError, ValueError):
        pass        
    return result
   

#-----------------End of Functions for YouTube Streaming---------------------



#--------------Start of Chromecast functions-----------------------------------

def chromecast_play_video(phrase):
    # Chromecast declarations
    # Do not rename/change "TV" its a variable
    TV = pychromecast.Chromecast("192.168.1.13") #Change ip to match the ip-address of your Chromecast
    mc = TV.media_controller
    idx1=phrase.find(custom_action_keyword['Dict']['Play'])
    idx2=phrase.find('on chromecast')
    query=phrase[idx1:idx2]
    query=query.replace(custom_action_keyword['Dict']['Play'],'',1)
    query=query.replace('on chromecast','',1)
    query=query.strip()
    youtubelinks=youtube_search(query)
    youtubeurl=youtubelinks[0]
    streams=youtube_stream_link(youtubeurl)
    videostream=streams[1]
    TV.wait()
    time.sleep(1)
    mc.play_media(videostream,'video/mp4')

def chromecast_control(action):
    # Chromecast declarations
    # Do not rename/change "TV" its a variable
    TV = pychromecast.Chromecast("192.168.1.13") #Change ip to match the ip-address of your Chromecast
    mc = TV.media_controller
    if 'pause'.lower() in str(action).lower():
        TV.wait()
        time.sleep(1)
        mc.pause()
    if 'resume'.lower() in str(action).lower():
        TV.wait()
        time.sleep(1)
        mc.play()
    if 'end'.lower() in str(action).lower():
        TV.wait()
        time.sleep(1)
        mc.stop()
    if 'volume'.lower() in str(action).lower():
        if 'up'.lower() in str(action).lower():
            TV.wait()
            time.sleep(1)
            TV.volume_up(0.2)
        if 'down'.lower() in str(action).lower():
            TV.wait()
            time.sleep(1)
            TV.volume_down(0.2)

#-------------------End of Chromecast Functions---------------------------------

#-------------------Start of Kickstarter Search functions-----------------------
def campaign_page_parser(campaignname):
    page_link=kickstrater_search(campaignname)
    kicktrackurl=page_link['items'][0]['link']
    response=urllib.request.urlopen(kicktrackurl)
    webContent = response.read()
    webContent = webContent.decode('utf-8')
    return webContent

def kickstarter_get_data(page_source,parameter):
    idx=page_source.find(parameter)
    info=page_source[idx:]
    info=info.replace(parameter,"",1)
    idx=info.find('"')
    info=info[:idx]
    info=info.replace('"',"",1)
    info=info.strip()
    result=info
    return result

def get_campaign_title(campaign):
    campaigntitle=campaign
    campaigntitleidx1=campaigntitle.find('<title>')
    campaigntitleidx2=campaigntitle.find('&mdash;')
    campaigntitle=campaigntitle[campaigntitleidx1:campaigntitleidx2]
    campaigntitle=campaigntitle.replace('<title>',"",1)
    campaigntitle=campaigntitle.replace('&mdash;',"",1)
    campaigntitle=campaigntitle.strip()
    return campaigntitle

def get_pledges_offered(campaign):
    pledgesoffered=campaign
    pledgenum=0
    for num in re.finditer('pledge__reward-description pledge__reward-description--expanded',pledgesoffered):
        pledgenum=pledgenum+1
    return pledgenum

def get_funding_period(campaign):
    period=campaign
    periodidx=period.find('Funding period')
    period=period[periodidx:]
    periodidx=period.find('</p>')
    period=period[:periodidx]
    startperiodidx1=period.find('class="invisible-if-js js-adjust-time">')
    startperiodidx2=period.find('</time>')
    startperiod=period[startperiodidx1:startperiodidx2]
    startperiod=startperiod.replace('class="invisible-if-js js-adjust-time">','',1)
    startperiod=startperiod.replace('</time>','',1)
    startperiod=startperiod.strip()
    period2=period[startperiodidx2+5:]
    endperiodidx1=period2.find('class="invisible-if-js js-adjust-time">')
    endperiodidx2=period2.find('</time>')
    endperiod=period2[endperiodidx1:endperiodidx2]
    endperiod=endperiod.replace('class="invisible-if-js js-adjust-time">','',1)
    endperiod=endperiod.replace('</time>','',1)
    endperiod=endperiod.strip()
    duration=period2[endperiodidx2:]
    duration=duration.replace('</time>','',1)
    duration=duration.replace('(','',1)
    duration=duration.replace(')','',1)
    duration=duration.replace('days','day',1)
    duration=duration.strip()
    return startperiod,endperiod,duration

def kickstarter_tracker(phrase):
    idx=phrase.find('of')
    campaign_name=phrase[idx:]
    campaign_name=campaign_name.replace("kickstarter campaign", "",1)
    campaign_name = campaign_name.replace('of','',1)
    campaign_name=campaign_name.strip()
    campaign_source=campaign_page_parser(campaign_name)
    campaign_title=get_campaign_title(campaign_source)
    campaign_num_rewards=get_pledges_offered(campaign_source)
    successidx=campaign_source.find('to help bring this project to life.')
    if str(successidx)==str(-1):
        backers=kickstarter_get_data(campaign_source,'data-backers-count="')
        totalpledged=kickstarter_get_data(campaign_source,'data-pledged="')
        totaltimerem=kickstarter_get_data(campaign_source,'data-hours-remaining="')
        totaldur=kickstarter_get_data(campaign_source,'data-duration="')
        endtime=kickstarter_get_data(campaign_source,'data-end_time="')
        goal=kickstarter_get_data(campaign_source,'data-goal="')
        percentraised=kickstarter_get_data(campaign_source,'data-percent-raised="')
        percentraised=round(float(percentraised),2)
        if int(totaltimerem)>0:
            #print(campaign_title+" is an ongoing campaign with "+str(totaltimerem)+" hours of fundraising still left." )
            say(campaign_title+" is an ongoing campaign with "+str(totaltimerem)+" hours of fundraising still left." )
            #print("Till now, "+str(backers)+ " backers have pledged for "+str(campaign_num_rewards)+" diferent rewards raising $"+str(totalpledged)+" , which is "+str(percentraised)+" times the requested amount of $"+str(goal))
            say("Till now, "+str(backers)+ " backers have pledged for "+str(campaign_num_rewards)+" diferent rewards raising $"+str(totalpledged)+" , which is "+str(percentraised)+" times the requested amount of $"+str(goal))
        if float(percentraised)<1 and int(totaltimerem)<=0:
            #print(campaign_title+" has already ended")
            say(campaign_title+" has already ended")
            #print(str(backers)+ " backers raised $"+str(totalpledged)+" , which was "+str(percentraised)+" times the requested amount of $"+str(goal))
            say(str(backers)+ " backers raised $"+str(totalpledged)+" , which was "+str(percentraised)+" times the requested amount of $"+str(goal))
            #print(campaign_title+" was unseccessful in raising the requested amount of $"+str(goal)+" ." )
            say(campaign_title+" was unseccessful in raising the requested amount of $"+str(goal)+" ." )
        if float(percentraised)>1 and int(totaltimerem)<=0:
            #print(campaign_title+" has already ended")
            say(campaign_title+" has already ended")
            #print(str(backers)+ " backers raised $"+str(totalpledged)+" , which was "+str(percentraised)+" times the requested amount of $"+str(goal))
            say(str(backers)+ " backers raised $"+str(totalpledged)+" , which was "+str(percentraised)+" times the requested amount of $"+str(goal))
            #print("Though the funding goal was reached, due to reasons undisclosed, the campaign was either cancelled by the creator or Kickstarter.")
            say("Though the funding goal was reached, due to reasons undisclosed, the campaign was either cancelled by the creator or Kickstarter.")
    else:
        [start_day,end_day,numdays]=get_funding_period(campaign_source)
        campaigninfo=campaign_source[(successidx-100):(successidx+35)]
        campaignidx=campaigninfo.find('<b>')
        campaigninfo=campaigninfo[campaignidx:]
        campaigninfo=campaigninfo.replace('<b>',"",1)
        campaigninfo=campaigninfo.replace('</b>',"",1)
        campaigninfo=campaigninfo.replace('<span class="money">',"",1)
        campaigninfo=campaigninfo.replace('</span>',"",1)
        campaigninfo=campaigninfo.strip()
        #print(campaign_title+" was a "+str(numdays)+" campaign launched on "+str(start_day))
        #print(campaigninfo)
        say(campaign_title+" was a "+str(numdays)+" campaign launched on "+str(start_day))
        say(campaigninfo)

#------------------------------End of Kickstarter Search functions---------------------------------------


#----------------------------------Start of Push Message function-----------------------------------------
def pushmessage(title,body):
    if pb!=None:
        push = pb.push_note(title,body)
    else:
        say("Pushbullet API key has not been entered.")
#----------------------------------End of Push Message Function-------------------------------------------


#----------------------------------Start of recipe Function----------------------------------------------
def getrecipe(item):
    appid='ENTER-YOUR-APPID-HERE'
    appkey='ENTER-YOUR-APP-KEY-HERE'
    recipeurl = 'https://api.edamam.com/search?q='+item+'&app_id='+appid+'&app_key='+appkey
    print(recipeurl)
    recipedetails = urllib.request.urlopen(recipeurl)
    recipedetails=recipedetails.read()
    recipedetails = recipedetails.decode('utf-8')
    recipedetails=json.loads(recipedetails)
    recipe_ingredients=str(recipedetails['hits'][0]['recipe']['ingredientLines'])
    recipe_url=recipedetails['hits'][0]['recipe']['url']
    recipe_name=recipedetails['hits'][0]['recipe']['label']
    recipe_ingredients=recipe_ingredients.replace('[','',1)
    recipe_ingredients=recipe_ingredients.replace(']','',1)
    recipe_ingredients=recipe_ingredients.replace('"','',1)
    recipe_ingredients=recipe_ingredients.strip()
    print(recipe_name)
    print("")
    print(recipe_url)
    print("")
    print(recipe_ingredients)
    compiled_recipe_info="\nRecipe Source URL:\n"+recipe_url+"\n\nRecipe Ingredients:\n"+recipe_ingredients
    pushmessage(str(recipe_name),str(compiled_recipe_info))

#---------------------------------End of recipe Function------------------------------------------------


#--------------------------------Start of Hue Control Functions------------------------------------------

def hue_control(phrase,lightindex,lightaddress):
    with open('/opt/hue-emulator/config.json', 'r') as config:
         hueconfig = json.load(config)
    currentxval=hueconfig['lights'][lightindex]['state']['xy'][0]
    currentyval=hueconfig['lights'][lightindex]['state']['xy'][1]
    currentbri=hueconfig['lights'][lightindex]['state']['bri']
    currentct=hueconfig['lights'][lightindex]['state']['ct']
    huelightname=str(hueconfig['lights'][lightindex]['name'])
    try:
        if custom_action_keyword['Dict']['On'] in phrase:
            huereq=requests.head("http://"+lightaddress+"/set?light="+lightindex+"&on=true")
            say("Turning on "+huelightname)
        if custom_action_keyword['Dict']['Off'] in phrase:
            huereq=requests.head("http://"+lightaddress+"/set?light="+lightindex+"&on=false")
            say("Turning off "+huelightname)
        if 'çolor' in phrase:
            rcolour,gcolour,bcolour,hexcolour,colour=getcolours(phrase)
            print(str([rcolour,gcolour,bcolour,hexcolour,colour]))
            xval,yval=convert_rgb_xy(int(rcolour),int(gcolour),int(bcolour))
            print(str([xval,yval]))
            huereq=requests.head("http://"+lightaddress+"/set?light="+lightindex+"&x="+str(xval)+"&y="+str(yval)+"&on=true")
            print("http://"+lightaddress+"/set?light="+lightindex+"&x="+str(xval)+"&y="+str(yval)+"&on=true")
            say("Setting "+huelightname+" to "+colour)
        if (custom_action_keyword['Dict']['Brightness']).lower() in phrase:
            if 'hundred'.lower() in phrase or custom_action_keyword['Dict']['Maximum'] in phrase:
                bright=100
            elif 'zero'.lower() in phrase or custom_action_keyword['Dict']['Minimum'] in phrase:
                bright=0
            else:
                bright=re.findall('\d+', phrase)
            brightval= (bright/100)*255
            huereq=requests.head("http://"+lightaddress+"/set?light="+lightindex+"&on=true&bri="+str(brightval))
            say("Changing "+huelightname+" brightness to "+bright+" percent")
    except (requests.exceptions.ConnectionError,TypeError) as errors:
        if str(errors)=="'NoneType' object is not iterable":
            print("Type Error")
        else:
            say("Device not online")

#------------------------------End of Hue Control Functions---------------------------------------------

#------------------------------Start of Spotify Functions-----------------------------------------------

def show_spotify_track_names(tracks):
    spotify_tracks=[]
    for i, item in enumerate(tracks['items']):
        track = item['track']
##        print ("%d %32.32s %s" % (i, track['artists'][0]['name'],track['name']))
        # print ("%s %s" % (track['artists'][0]['name'],track['name']))
        spotify_tracks.append("%s %s" % (track['artists'][0]['name'],track['name']))
    return spotify_tracks

def scan_spotify_playlists():
    if spotify_token:
        i=0
        playlistdetails=[]
        spotify_tracks_list=[]
        sp = spotipy.Spotify(auth=spotify_token)
        # print(sp.user(username))
        # print("")
        # print("")
        playlists = sp.user_playlists(username)
        print(len(playlists['items']))
        num_playlists=len(playlists['items'])
        spotify_playlists={"Playlists":[0]*(len(playlists['items']))}
        # print(spotify_playlists)
        # print("")
        # print("")
        for playlist in playlists['items']:
            # print (playlist['name'])
            playlist_name=playlist['name']
            # print("")
            # print("")
##            print ('  total tracks', playlist['tracks']['total'])
##            print("")
##            print("")
            results = sp.user_playlist(playlist['owner']['id'], playlist['id'],fields="tracks,next")
            tracks = results['tracks']
            spotify_tracks_list=show_spotify_track_names(tracks)
            playlistdetails.append(i)
            playlistdetails.append(playlist_name)
            playlistdetails.append(spotify_tracks_list)
            spotify_playlists['Playlists'][i]=playlistdetails
            playlistdetails=[]
            i=i+1
        # print("")
        # print("")
        # print(spotify_playlists['Playlists'])
        return spotify_playlists, num_playlists
    else:
        say("Can't get token for, " + username)
        print("Can't get token for ", username)

def spotify_playlist_select(phrase):
    trackslist=[]
    currenttrackid=0
    idx1=phrase.find(custom_action_keyword['Dict']['Play'])
    idx2=phrase.find(custom_action_keyword['Dict']['From_spotify'])
    track=phrase[idx1:idx2]
    track = track.replace(custom_action_keyword['Dict']['Play'],'',1)
    track = track.replace(custom_action_keyword['Dict']['From_spotify'],'',1)
    track=track.strip()
    say("Getting music links")
    print(track)
    playlists,num=scan_spotify_playlists()
    if not num==[]:
        for i in range(0,num):
            print(str(playlists['Playlists'][i][1]).lower())
            if track in str(playlists['Playlists'][i][1]).lower():
                trackslist=playlists['Playlists'][i][2]
                break
        if not trackslist==[]:
            vlcplayer.media_manager(trackslist,'Spotify')
            vlcplayer.spotify_player(currenttrackid)
    else:
        say("Unable to find matching playlist")

#----------------------End of Spotify functions---------------------------------

#----------------------Start of Domoticz Control Functions----------------------
def domoticz_control(query,index,devicename):
    global hexcolour,bright,devorder
    try:
        for j in range(0,len(domoticz_devices['result'])):
            if domoticz_devices['result'][j]['idx']==index:
                devorder=j
                break

        if (' ' + custom_action_keyword['Dict']['On'] + ' ') in query or (' ' + custom_action_keyword['Dict']['On']) in query or (custom_action_keyword['Dict']['On'] + ' ') in query:
            devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=switchlight&idx=" + index + "&switchcmd=On",verify=False)
            say('Turning on ' + devicename )
        if custom_action_keyword['Dict']['Off'] in query:
            devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=switchlight&idx=" + index + "&switchcmd=Off",verify=False)
            say('Turning off ' + devicename )
        if 'toggle' in query:
            devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=switchlight&idx=" + index + "&switchcmd=Toggle",verify=False)
            say('Toggling ' + devicename )
        if custom_action_keyword['Dict']['Colour'] in query:
            if 'RGB' in domoticz_devices['result'][devorder]['SubType']:
                rcolour,gcolour,bcolour,hexcolour,colour=getcolours(query)
                hexcolour=hexcolour.replace("#","",1)
                hexcolour=hexcolour.strip()
                print(hexcolour)
                if bright=='':
                    bright=str(domoticz_devices['result'][devorder]['Level'])
                devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=setcolbrightnessvalue&idx=" + index + "&hex=" + hexcolour + "&brightness=" + bright + "&iswhite=false",verify=False)
                say('Setting ' + devicename + ' to ' + colour )
            else:
                say('The requested light is not a colour bulb')
        if custom_action_keyword['Dict']['Brightness'] in query:
            if domoticz_devices['result'][devorder]['HaveDimmer']:
                if 'hundred' in query or 'hundred'.lower() in query or custom_action_keyword['Dict']['Maximum'] in query:
                    bright=str(100)
                elif 'zero' in query or custom_action_keyword['Dict']['Minimum'] in query:
                    bright=str(0)
                else:
                    bright=re.findall('\d+', query)
                    bright=bright[0]
                devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=switchlight&idx=" + index + "&switchcmd=Set%20Level&level=" + bright ,verify=False)
                say('Setting ' + devicename + ' brightness to ' + str(bright) + ' percent.')
            else:
                say('The requested light does not have a dimer')

    except (requests.exceptions.ConnectionError,TypeError) as errors:
        if str(errors)=="'NoneType' object is not iterable":
            print("Type Error")
        else:
            say("Device or Domoticz server is not online")
#------------------------End of Domoticz Control Functions----------------------

#------------------------Start of Gaana Functions-------------------------------
def getgaanaplaylistinfo(playlisturl):
    trackstart=[]
    trackend=[]
    playliststart=[]
    playlistend=[]
    trackdetails=[]
    response=urllib.request.urlopen(playlisturl)
    response=response.read().decode('utf-8')
    for a in re.finditer('{"title":',response):
        trackstart.append(a.start())
    for b in re.finditer('"parental_warning":(.*)}',response):
        trackend.append(b.end())
    for c in re.finditer('{"source":',response):
        playliststart=c.start()
    for d in re.finditer('}</span>',response):
        playlistend=int(d.start())+1
    playlistinfo=json.loads(response[playliststart:playlistend])
    playlistname=playlistinfo['title']
    if len(trackstart)==len(trackend) and len(trackstart)>0:
        for i in range(0,len(trackstart)):
            trackdetails.append(json.loads(response[trackstart[i]:trackend[i]]))
    else:
        trackdetails=[]
    numtracks=len(trackdetails)
    return playlistname,numtracks,trackdetails

def gaana_playlist_select(phrase):
    trackslist=[]
    currenttrackid=0
    idx1=phrase.find(custom_action_keyword['Dict']['Play'])
    idx2=phrase.find(custom_action_keyword['Dict']['From_gaana'])
    track=phrase[idx1:idx2]
    track = track.replace(custom_action_keyword['Dict']['Play'],'',1)
    track = track.replace(custom_action_keyword['Dict']['From_gaana'],'',1)
    track=track.strip()
    playlistnumreq=re.findall(r'\b\d+\b', track)
    if playlistnumreq !=[]:
        playlistnumreq=playlistnumreq[0]
    userplaylists=configuration['Gaana']['Playlist']
    numuserplaylists=len(userplaylists)
    if playlistnumreq !=[] and "top" not in track and int(playlistnumreq) <= int(numuserplaylists):
        print("Getting links for playlist number " + playlistnumreq)
        say("Getting links for playlist number " + playlistnumreq)
        reqplaylist=configuration['Gaana']['Playlist'][(int(playlistnumreq)-1)]
    else:
        print("Searching for " + track +  " in gaana.com")
        say("Searching for " + track +  " in gaana.com")
        page_link=gaana_search(track)
        reqplaylist=page_link['items'][0]['link']
    name,numsongs,tracks= getgaanaplaylistinfo(reqplaylist)
    print(numsongs)
    if not numsongs==[]:
        say("Getting the tracks from " + name)
        for i in range(0,numsongs):
            trackslist.append((tracks[i]['title'] + ' ' + tracks[i]['albumtitle']))
        if not trackslist==[]:
            vlcplayer.media_manager(trackslist,'Gaana')
            vlcplayer.gaana_player(currenttrackid)
    else:
        say("Unable to find matching playlist")

#------------------------End of Gaana Functions-------------------------------

#------------------------Start of Deezer Functions-------------------------------
def deezer_playlist_select(phrase):
    trackslist=[]
    deezer_user_playlists=[]
    currenttrackid=0
    idx1=phrase.find(custom_action_keyword['Dict']['Play'])
    idx2=phrase.find(custom_action_keyword['Dict']['From_deezer'])
    track=phrase[idx1:idx2]
    track = track.replace(custom_action_keyword['Dict']['Play'],'',1)
    track = track.replace(custom_action_keyword['Dict']['From_deezer'],'',1)
    track=track.strip()
    playlistnumreq=re.findall(r'\b\d+\b', track)
    if playlistnumreq !=[]:
        playlistnumreq=playlistnumreq[0]
    deezer_response = requests.get("https://api.deezer.com/user/" + configuration['Deezer']['User_id'] + "/playlists",verify=False)
    deezer_user_playlist_info=json.loads(deezer_response.text)
    if deezer_user_playlist_info['data'] != []:
        for i in range(0,len(deezer_user_playlist_info['data'])):
            deezer_user_playlists.append(deezer_user_playlist_info['data'][i]['tracklist'])
    else:
        say("No playlists found for the user")
    numuserplaylists=len(deezer_user_playlists)
    if playlistnumreq !=[] and "top" not in track and int(playlistnumreq) <= int(numuserplaylists):
        print("Getting links for playlist number " + playlistnumreq)
        say("Getting links for playlist number " + playlistnumreq)
        tracklisturl=deezer_user_playlists[(int(playlistnumreq)-1)]
    else:
        say("No matching playlists found")
    deezer_tracks_response = requests.get(tracklisturl,verify=False)
    deezer_user_playlist_tracks_info=json.loads(deezer_tracks_response.text)
    numsongs=len(deezer_user_playlist_tracks_info['data'])
    if not numsongs==[]:
        say("Getting the tracks from " + deezer_user_playlist_info['data'][int(playlistnumreq)-1]['title'])
        for i in range(0,numsongs):
            trackslist.append((deezer_user_playlist_tracks_info['data'][i]['title'] + ' by ' + deezer_user_playlist_tracks_info['data'][i]['artist']['name'] + ' from ' + deezer_user_playlist_tracks_info['data'][i]['album']['title']))
        if not trackslist==[]:
            vlcplayer.media_manager(trackslist,'Deezer')
            vlcplayer.gaana_player(currenttrackid)
    else:
        say("Unable to find matching tracks")

#------------------------End of Deezer Functions-------------------------------

#-----------------------Start of functions for IR code--------------------------

def binary_aquire(pin, duration):
    t0 = time.time()
    results = []
    while (time.time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results

def on_ir_receive(pinNo, bouncetime=150):
    data = binary_aquire(pinNo, bouncetime/1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        return None

#-----------------------End of functions for IR code--------------------------

#-----------------------Start of functions for Wemo/Emulated Wemo-------------

def wemodiscovery():
    devices = pywemo.discover_devices()
    if devices!=[]:
        with open('{}/wemodevicelist.json'.format(USER_PATH), 'w') as devicelist:
               json.dump(devices, devicelist)
        if len(devices)>1:
            say("Found "+str(len(devices))+" devices.")
        else:
            say("Found "+str(len(devices))+" device.")
    else:
        say("Unable to find any active device.")

def wemocontrol(command):
    if os.path.isfile("{}/wemodevicelist.json".format(USER_PATH)):
        with open('{}/wemodevicelist.json'.format(USER_PATH), 'r') as devicelist:
            wemodevices = json.load(devicelist)
        if wemodevices!=[]:
            for i in range(0,len(wemodevices)):
                if wemodevices[i] in command:
                    if (' ' + custom_action_keyword['Dict']['On'] + ' ') in command or (' ' + custom_action_keyword['Dict']['On']) in query or (custom_action_keyword['Dict']['On'] + ' ') in command:
                        wemodevices[i].on()
                        say("Turning on "+wemodevices[i])
                    elif custom_action_keyword['Dict']['Off'] in command:
                        wemodevices[i].on()
                        say("Turning off "+wemodevices[i])
                    break
        else:
            say("Device list is empty. Try running the device discovery.")
    else:
        say("Unable to find device registry. Try running the device discovery.")

#-----------------------End of functions for Wemo/Emulated Wemo-------------

#Send voicenote to phone
def voicenote(audiofile):
    if pb!=None:
        say("Sending your voicenote")
        with open(audiofile, "rb") as recordedvoicenote:
            file_data = pb.upload_file(recordedvoicenote, 'Voicenote.wav')
        push = pb.push_file(**file_data)
    else:
        say("Pushbullet API key has not been entered.")

#GPIO Device Control
def Action(phrase):
    if 'shutdown' in phrase:
        say('Shutting down Raspberry Pi')
        time.sleep(10)
        os.system("sudo shutdown -h now")
        #subprocess.call(["shutdown -h now"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if 'servo' in phrase:
        for s in re.findall(r'\b\d+\b', phrase):
            SetAngle(int(s))
        if 'zero' in phrase:
            SetAngle(0)
    else:
        if GPIOcontrol:
            for num, name in enumerate(var):
                if name.lower() in phrase:
                    pinout=gpio[num]
                    if custom_action_keyword['Dict']['On'] in phrase:
                        GPIO.output(pinout, 1)
                        say("Turning On " + name)
                    elif custom_action_keyword['Dict']['Off'] in phrase:
                        GPIO.output(pinout, 0)
                        say("Turning Off " + name)
        else:
            say("GPIO controls, is not supported for your device.")


#############lịch âm

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import lun
from lun import S2L
from lun import L2S


def licham(usrcmd):
    print('[ViPi]: XỬ LÝ CÂU LỆNH ÂM LỊCH: '+usrcmd)
    if (custom_action_keyword['Keywords']['request_day'][0]).lower() in str(usrcmd).lower():       
        kiemtra_amlich(check_last_day())    
    elif (custom_action_keyword['Keywords']['request_day'][1]).lower() in str(usrcmd).lower():  
        kiemtra_amlich(check_to_day())    
    elif (custom_action_keyword['Keywords']['request_day'][2]).lower() in str(usrcmd).lower():  
        kiemtra_amlich(check_tomorrow())    
    elif (custom_action_keyword['Keywords']['request_day'][3]).lower() in str(usrcmd).lower():  
        kiemtra_amlich(check_next_day())    
    else:
        kiemtra_amlich(check_last_day())     
        pass
                                   
def check_last_day():
    print ('Âm lịch hôm qua')
    a = 'Hôm qua'
    ngay = datetime.date.today() - timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day    
    return a,ngay,yy,mm,dd

def check_to_day():
    a = 'Hôm nay'
    print ('âm lịch hôm nay')
    ngay = datetime.date.today()
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    list = [a,ngay,yy,mm,dd]
    return list
def check_tomorrow():
    print ('Âm lịch ngày mai')
    a = 'Ngày mai'
    ngay = datetime.date.today() + timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def check_next_day():
    print ('Âm lịch ngày mốt')
    a = 'Ngày mốt'
    ngay = datetime.date.today() + timedelta(2)
    yy = ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def check_other_day(data):
    today=datetime.date.today()
    print ('Âm lịch ngày')
    if 'NGÀY' in data:
        ngay = re.search('NGÀY (.+?)(.+?)', data)
        dd = int(ngay.group(1)+ngay.group(2))
    else: 
        dd = today.day
    if 'THÁNG' in data:
        thang = re.search('THÁNG (.+?)(.+?)', data)
        mm = int(thang.group(1)+thang.group(2)) 
    else:
        mm = today.month    
    yy = today.year     
    a = 'Ngày '+str(dd)+ 'tháng '+str(mm)
    daa = str(yy)+'-'+str(mm)+'-'+str(dd)
    ngay = datetime.datetime.strptime(daa, '%Y-%m-%d')
    a = 'Ngày '+str(dd)+ 'tháng '+str(mm)+' năm nay'
    return a,ngay,yy,mm,dd



def kiemtra_amlich(list):
    a = list[0]
    ngay = list[1]
    yy = list[2]
    mm = list[3]
    dd = list[4]
    lunar_date = S2L(dd, mm, yy)
    ngay_am = str(lunar_date[0])
    list_thang = ["tháng Giêng","tháng Hai","tháng Ba","tháng Tư","tháng Năm","tháng Sáu","tháng Bảy","tháng Tám","tháng Chín","tháng Mười","tháng Mười một","tháng Chạp"]
    thang_am = int(str(lunar_date[1]))-1
    thang_am1 = list_thang[thang_am]
    can = ['Canh ', 'Tân ', 'Nhâm ', 'Quý ', 'Giáp ', 'Ất ', 'Bính ', 'Đinh ','Mậu ','Kỷ ']
    chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
    nam = int(str(lunar_date[2]))
    vitri_can = nam % 10
    vitri_chi = nam % 12
    nam_am = str(lunar_date[2])
    # lunar_text2 = 'Ngày: ' + str(lunar_date[0]) + ' - ' + thang_am1  + ' năm '  + can[vitri_can] + chi[vitri_chi] + ' (' +  str(lunar_date[2]) +')'
    ss = int(ngay_am)
    nam_nhuan = int(str(lunar_date[3])) 
    if ss == 15:
        say(a+" âm lịch là rằm "+ thang_am1 + 'năm ' + can[vitri_can] +' '+ chi[vitri_chi]+' ' + nam_am)
    elif ss == 1:
        say(a+" âm lịch là mùng một "+ thang_am1 + 'năm ' + can[vitri_can] +' '+ chi[vitri_chi]+ ' ' + nam_am)
    elif ss>1 and ss<15:
        days_left = 15 - ss
        say(a+" âm lịch là " + ngay_am +' '+ thang_am1 + ' năm ' + can[vitri_can] +' '+ chi[vitri_chi] +' '+ nam_am + ". Còn " + str(days_left) + " ngày nữa là đến rằm ")
    elif ss>15 and ss<31:
        thang_sau = thang_am + 1
        if thang_am <= 12:
            nam_a = nam_am 
        else:
            nam_a = nam_am + 1
            # ny = yy + 1
            a2d = L2S(28,12,yy,nam_nhuan)
            nd = a2d[0]
            td = a2d[1]
            nmd = a2d[2]
            daa = str(nd)+'-'+str(td)+'-'+str(nmd)
            a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
            ngaytet = a2dnew.day
            thangtet = a2dnew.month
            namtet = a2dnew.year
            nammoi = S2L(ngaytet,thangtet,namtet)
            nam_nhuan = int(str(nammoi[3]))
        next = L2S(1,thang_sau,int(nam_a), nam_nhuan)
        nd = next[0]
        td = next[1]
        nmd = next[2]
        daa = str(nd)+'-'+str(td)+'-'+str(nmd)
        a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
        delta = a2dnew - datetime.datetime.today()
        days_left = delta.days
        thang_am = list_thang[thang_am]
        ngay_am =str(lunar_date[0])
        say(a+' âm lịch là ' + ngay_am +' '+ thang_am + ' năm ' + can[vitri_can]+' ' + chi[vitri_chi]+' ' + nam_am)                   
    else:
        say(str(a)+'  âm lịch là ' + str(ngay_am)+' ' + str(thang_am) + ' năm ' + str(can[vitri_can])+' ' + str(chi[vitri_chi])+ ' ' + str(nam_am))
 
 
 ################################END LỊCH ÂM#########################
 
 #################################ZING.MP3#############################
 	# elif row0_in_db=="ZING":
		# if seed == 1:
			# pixels.speak()
		# import zing, vlc
		# playlist = zing.zing_song(data)
		# player = zing.phat_zing(playlist)
		# speaking.speak('Đang chuẩn bị phát top 100 ca khúc trên Zing')
		# player.play()
		# if 'TIẾP' in data:
			# print ('Next')
			# player.next()
		# if 'TRƯỚC' in data:
			# print ('Prev')
			# player.previous()		
		# if seed == 1:
			# pixels.off()

	# else:
		# if seed == 1:
			# pixels.speak()
		# answer('em không hiểu','em nghe không rõ',' vui lòng nói lại đi')
		# if seed == 1:
			# # pixels.off()
		# execute.run_thread(wt,data)
# # TIN RADIO
	# elif row0_in_db=="TIN VẮN":
		# import zing
		# if seed == 1:
			# pixels.speak()
		# playlist = news.getlink(data)
		# player = zing.phat_zing(playlist)
		# speaking.speak('Đang chuẩn bị phát tin vắn radio')
		# player.play()
		# if 'TIẾP' in data:
			# print ('Next')
			# player.next()
		# if 'TRƯỚC' in data:
			# print ('Prev')
			# player.previous()
		# if seed == 1:
			# pixels.off()            
            
# #Hàm lấy data
# TOP100 = {'pop':'ZWZB96AB', 'country': 'ZWZB96AE', 'rock': 'ZWZB96AC', 'dance': 'ZWZB96C7', 'r&b': 'ZWZB96C8', 'rap': 'ZWZB96AD', 'soundtrack': 'ZWZB96C9',
          # 'nhac tre':'ZWZB969E', 'tru tinh': 'ZWZB969F', 'que huong': 'ZWZB96AU', 'cach mang': 'ZWZB96AO', 'rock viet': 'ZWZB96A0', 'rap viet': 'ZWZB96AI', 'dance viet': 'ZWZB96AW'}
# url_list = 'https://mp3.zing.vn/xhr/media/get-list?op=top100&start=0&length=20&id='
# url_audio = 'https://mp3.zing.vn/xhr/media/get-source?type=audio&key='
# prefix_url = 'https:'

# def get_codes(type_TOP):
	# type_TOP = type_TOP.lower()
	# uri = url_list + TOP100.get(type_TOP)
	# re = requests.get(uri).json()
	# items = re['data']['items']
	# audio_codes = []
	# for item in items:
		# code = item['code']
		# audio_codes.append(code)
	# return audio_codes

# def get_audio_links(type_TOP):
	# alink = []
	# audio_links = {}
	# codes = get_codes(type_TOP)
	# for code in codes:
		# uri = url_audio + code
		# re = requests.get(uri).json()['data']
		# link = prefix_url + re['source']['128']
		# duration =  int(re['duration'])
		# audio_links[link] = duration
		# alink.append(link)
	# return alink
# def zing_song(data):
	# if 'TRỮ TÌNH' in data.upper():
		# type_TOP = 'tru tinh'
	# elif 'NHẠC TRẺ' in data.upper():
		# type_TOP = 'nhac tre'
	# elif 'QUÊ HƯƠNG' in data.upper():
		# type_TOP = 'que huong'
	# elif 'CÁCH MẠNG' in data.upper():
		# type_TOP = 'cach mang'
	# elif 'ROCK VIỆT' in data.upper():
		# type_TOP = 'rock viet'
	# elif 'RAP VIỆT' in data.upper():
		# type_TOP = 'rap viet'
	# elif 'DANCE VIỆT' in data.upper():
		# type_TOP = 'dance viet'
	# if 'POP' in data.upper():
		# type_TOP = 'pop'
	# elif 'ROCK' in data.upper():
		# type_TOP = 'rock'
	# elif 'COUNTRY' in data.upper():
		# type_TOP = 'country'
	# elif 'DANCE' in data.upper():
		# type_TOP = 'dance'
	# elif 'SOUNDTRACK' in data.upper():
		# type_TOP = 'soundtrack'
	# else:
		# type_TOP = 'nhac tre'
	# print (type_TOP)
	# mp3_links = get_audio_links(type_TOP)
	# return mp3_links
# def phat_zing(playlist):
	# inst = vlc.Instance()
	# player = inst.media_list_player_new()
	# mediaList = inst.media_list_new(playlist)
	# player.set_media_list(mediaList)
	# playing = set([1,2,3,4])
	# return player
# #	print (mp3_links)
# # ZING
	# elif row0_in_db=="ZING":
		# import zing
		# playlist = zing.zing_song(data)
		# player = zing.phat_zing(playlist)
		# speaking.speak('Đang chuẩn bị phát top 100 ca khúc trên Zing')
		# player.play()
		# if 'TIẾP' in data:
			# print ('Next')
			# player.next()
		# if 'TRƯỚC' in data:
			# print ('Prev')
			# player.previous()		

	# else:
		# answer('em không hiểu','em nghe không rõ',' vui lòng nói lại đi')
		# if seed == 1:
			# pixels.off()
  
  ##############Zingmp3########



# data ='thôi đừng chiêm bao'

def zingmp3(phrase):
    #print("Tìm bài hát: "+phrase+"...")
    data=phrase
    data=data.replace('zing','')
    data=data.strip()
    result=None
    print("Tìm bài hát trên zingmp3.vn: "+data+"...")
    currenttrackid=0
    try:
        resp = requests.get('http://ac.mp3.zing.vn/complete/desktop?type=song&query='+urllib.parse.quote(data))
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        songID = obj["data"][1]['song'][0]['id']
        songUrl= "https://mp3.zing.vn/bai-hat/"+songID+".html"
        print(songUrl)
        resp = requests.get(songUrl)
        #print(resp.text)
        key = re.findall('data-xml="\/media\/get-source\?type=audio&key=([a-zA-Z0-9]{20,35})', resp.text)
        # # key = re.findall('data-xml="\/media\/get-source\?type=video&key=([a-zA-Z0-9]{20,35})', resp.text)
        songApiUrl = "https://mp3.zing.vn/xhr/media/get-source?type=audio&key="+key[0]
        resp = requests.get(songApiUrl)
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        #print(str(obj))
        mp3Source = "https:"+obj["data"]["source"]["128"]
        realURLdata = requests.get(mp3Source,allow_redirects=False)
        #print(realURLdata)
        realURL = realURLdata.headers['Location']
        file_name, headers = urlretrieve(realURL)
        print(realURL)
        result=file_name
        if result is not None:
            #fullurl=result
            vlcplayer.media_manager(result,'zing')
            vlcplayer.media_player(result)
        else:
            say("Không tìm thấy bài hát yêu cầu trên zin")     
    except (IndexError, ValueError):
        pass        
    return result
##############YOTUBE##############



# def youtube(data):
    # file_name=None
    # print("Tìm bài hát: "+data+"...")
    # data = data.lower()
    # query_string = urllib.parse.urlencode({"search_query" : data})
    # html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    # list_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    # url = "http://www.youtube.com/watch?v="+list_results[0]
    # info = pafy.new(url)
    # title = info.title
    # file_name_m4a ='/tmp/'+data+'.m4a'
    # file_name_mp3 ='mp3/'+data+'.mp3'            
    # audio = info.m4astreams[-1]
    # audio = info.getbestaudio(preftype="m4a")
    # audio.download(file_name_m4a, quiet=True)
    # ouput=None
    # try:
        # track = AudioSegment.from_file(file_name_m4a,'m4a')
        # print('CONVERTING: ' + str(title))
        # file_handle = track.export(file_name_mp3, format='mp3')
        # file_name = file_name_mp3
    # except:
        # print("ERROR CONVERTING " + str(file_name_m4a))
    # return file_name


# ####################Tìm VB##############

# def travanban(data):
    # list_result=''
    # #HTTP Request
    # url = 'https://vanbanphapluat.co/api/search?kwd='+data
    # response = requests.post(url, verify=False)
    # for i in range(len(response.json()['Items'])):
        # ''.join([list_result,'Kết quả thứ '+i+': Văn bản số: '+ response.json()['Items'][i]['SoHieu']+', nội dung '+response.json()['Items'][i]['TrichYeu'].replace('<em>','').replace('</em>','')])
    
    # # for i in range(len(list_result)):
        # # print(list_result[i])
    # say('list_result')#!/usr/bin/env python

#This is different from AIY Kit's actions
#Copying and Pasting AIY Kit's actions commands will not work

# from kodijson import Kodi, PLAYER_VIDEO
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import spotipy.oauth2 as oauth2
from pushbullet import Pushbullet
# from mediaplayer import api
from youtube_search_engine import google_cloud_api_key
from googletrans import Translator
from youtube_search_engine import youtube_search
from youtube_search_engine import youtube_stream_link
from google.cloud import texttospeech
from gtts import gTTS
import requests
import mediaplayer
import os
import os.path
from os import path
import uuid, urllib
try:
    import RPi.GPIO as GPIO
except Exception as e:
    GPIO = None
import time
import re
import subprocess
import aftership
import feedparser
import json
import urllib.request
import pafy
import pychromecast
import spotipy
import pprint
import yaml
import pywemo
import random
import threading
from termcolor import colored
from os import listdir
import urllib
from urllib.request import urlretrieve
ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))


with open('{}/src/config.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    configuration = yaml.load(conf)

with open('{}/src/lang.yaml'.format(ROOT_PATH),'r', encoding='utf8') as lang:
    langlist = yaml.load(lang)

TTSChoice=''
if configuration['TextToSpeech']['Choice']=="Google Cloud":
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""):
        if configuration['TextToSpeech']['Google_Cloud_TTS_Credentials_Path']!="ENTER THE PATH TO YOUR TTS CREDENTIALS FILE HERE":
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = configuration['TextToSpeech']['Google_Cloud_TTS_Credentials_Path']
            TTSChoice='GoogleCloud'
            # Instantiates a client
            client = texttospeech.TextToSpeechClient()
        else:
            print("Set the path to your Google cloud text to speech credentials in the config.yaml file. Using gTTS for now.....")
            TTSChoice='GTTS'
    else:
        TTSChoice='GoogleCloud'
        # Instantiates a client
        client = texttospeech.TextToSpeechClient()
if configuration['TextToSpeech']['Choice']=="VIETTEL":
    TTSChoice='VIETTEL'
else:
    TTSChoice='GTTS'


domoticz_devices=''
Domoticz_Device_Control=False
bright=''
hexcolour=''

keywordfile= '{}/src/keywords_vn.yaml'.format(ROOT_PATH)
with open(keywordfile,'r' , encoding='utf8') as conf:
    custom_action_keyword = yaml.load(conf)


# Get devices list from domoticz server
if configuration['Domoticz']['Domoticz_Control']=='Enabled':
    Domoticz_Device_Control=True
    try:
        domoticz_response = requests.get("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=devices&filter=all&order=Name",verify=False)
        domoticz_devices=json.loads(domoticz_response.text)
        with open('{}/domoticz_device_list.json'.format(USER_PATH), 'w') as devlist:
            json.dump(domoticz_devices, devlist)
    except requests.exceptions.ConnectionError:
        print("Domoticz server not online")
else:
    Domoticz_Device_Control=False

Spotify_credentials=False
Youtube_credentials=False
if configuration['Spotify']['client_id']!= 'ENTER YOUR SPOTIFY CLIENT ID HERE' and configuration['Spotify']['client_secret']!='ENTER YOUR SPOTIFY CLIENT SECRET HERE':
    Spotify_credentials=True
if configuration['Google_cloud_api_key']!='ENTER-YOUR-GOOGLE-CLOUD-API-KEY-HERE':
    Youtube_credentials=True

# Spotify Declarations
# Register with spotify for a developer account to get client-id and client-secret
if Spotify_credentials:
    client_id = configuration['Spotify']['client_id']
    client_secret = configuration['Spotify']['client_secret']
    username=configuration['Spotify']['username']
    credentials = oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify_token = credentials.get_access_token()


#Import VLC player
vlcplayer=mediaplayer.vlcplayer()



#Google Music Declarations
song_ids=[]
track_ids=[]


#Login with default kodi/kodi credentials
#kodi = Kodi("http://localhost:8080/jsonrpc")

#Login with custom credentials
# # Kodi("http://IP-ADDRESS-OF-KODI:8080/jsonrpc", "username", "password")
# kodiurl=("http://"+str(configuration['Kodi']['ip'])+":"+str(configuration['Kodi']['port'])+"/jsonrpc")
# kodi = Kodi(kodiurl, configuration['Kodi']['username'], configuration['Kodi']['password'])
# musicdirectory=configuration['Kodi']['musicdirectory']
# videodirectory=configuration['Kodi']['videodirectory']
# windowcmd=configuration['Kodi']['windowcmd']
# window=configuration['Kodi']['window']

if GPIO!=None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #Number of entities in 'var' and 'PINS' should be the same
    var = configuration['Raspberrypi_GPIO_Control']['lightnames']
    gpio = configuration['Gpios']['picontrol']
    for pin in gpio:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    #Servo pin declaration
    servopin=configuration['Gpios']['servo'][0]
    GPIO.setup(servopin, GPIO.OUT)
    #pwm=GPIO.PWM(servopin, 50)
    #pwm.start(0)

    #Stopbutton
    stoppushbutton=configuration['Gpios']['stopbutton_music_AIY_pushbutton'][0]
    GPIO.setup(stoppushbutton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIOcontrol=True
else:
    GPIOcontrol=False

#Number of scripts and script names should be the same
scriptname=configuration['Script']['scriptname']
scriptcommand=configuration['Script']['scriptcommand']

#Number of station names and station links should be the same
stnname=configuration['Radio_stations']['stationnames']
stnlink=configuration['Radio_stations']['stationlinks']
stnradio=configuration['Radio_stations']['stationradio']

#IP Address of ESP
ip=configuration['ESP']['IP']

#Declaration of ESP names
devname=configuration['ESP']['devicename']
devid=configuration['ESP']['deviceid']

playshell = None

#Initialize colour list
clrlist=[]
clrlistfullname=[]
clrrgblist=[]
clrhexlist=[]
with open('{}/src/colours.json'.format(ROOT_PATH), 'r') as col:
     colours = json.load(col)
for i in range(0,len(colours)):
    clrname=colours[i]["name"]
    clrnameshort=clrname.replace(" ","",1)
    clrnameshort=clrnameshort.strip()
    clrnameshort=clrnameshort.lower()
    clrlist.append(clrnameshort)
    clrlistfullname.append(clrname)
    clrrgblist.append(colours[i]["rgb"])
    clrhexlist.append(colours[i]["hex"])


#Parcel Tracking declarations
aftership.api_key=configuration['AFTERSHIP']['Key']
aftershiptracking=False
if configuration['AFTERSHIP']['Key']=='ENTER YOUR AFTERSHIP KEY HERE':
    aftershiptracking=False
else:
    aftershiptracking=True
    couriers = configuration['AFTERSHIP']['Parcels']['Courier_Name']
    trackingids = configuration['AFTERSHIP']['Parcels']['Tracking_Code']


#RSS feed URLS
worldnews = "http://feeds.bbci.co.uk/news/world/rss.xml"
technews = "http://feeds.bbci.co.uk/news/technology/rss.xml"
topnews = "http://feeds.bbci.co.uk/news/rss.xml"
sportsnews = "http://feeds.feedburner.com/ndtvsports-latest"
quote = "http://feeds.feedburner.com/brainyquote/QUOTEBR"

##Speech and translator declarations
translator = Translator()
femalettsfilename="/tmp/female-say.mp3"
malettsfilename="/tmp/male-say.wav"
ttsfilename="/tmp/gcloud.mp3"
language=configuration['Language']['Choice']
translanguage=language.split('-')[0]
gender=''
if configuration['TextToSpeech']['Voice_Gender']=='Male':
    gender='Male'
elif configuration['TextToSpeech']['Voice_Gender']=='Female':
    gender='Female'
else:
    gender='Female'

if configuration['Pushbullet']['Pushbullet_API_KEY']!='ENTER YOUR PUSHBULLET KEY HERE':
    pb=Pushbullet(configuration['Pushbullet']['Pushbullet_API_KEY'])
else:
    pb=None

#Function for google KS custom search engine
def kickstrater_search(query):
    service = build("customsearch", "v1",
            developerKey=google_cloud_api_key)
    res = service.cse().list(
        q=query,
        cx = '012926744822728151901:gefufijnci4',
        ).execute()
    return res


#Function for google Gaana custom search engine
def gaana_search(query):
    service = build("customsearch", "v1",
            developerKey=google_cloud_api_key)
    res = service.cse().list(
        q=query,
        cx = '012926744822728151901:jzpzbzih5hi',
        ).execute()
    return res

#gTTS
def gttssay(phrase,saylang,specgender):
    tts = gTTS(text=phrase, lang='vi')
    tts.save(femalettsfilename)
    if specgender=='Male':
        os.system('sox ' + femalettsfilename + ' ' + malettsfilename + ' pitch +450')
        os.remove(femalettsfilename)
        os.system('aplay ' + malettsfilename)
        os.remove(malettsfilename)
    elif specgender=='Female':
        os.system("mpg123 "+femalettsfilename)
        os.remove(femalettsfilename)
#tts Viettel
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# import os.path

#from termcolor import colored
#from mutagen.mp3 import MP3


token='HXddsd-TPRwwS4AqRKwTCh-qlyziwWcBOzmbTSzDW3XgT8yY5J-Gx-2BFfz1sW-C'
#speak_volume=1.0
voice_name='hcm-diemmy2'
speed=1.0
pitch=0
def stt_viettel(phrase):
    text=phrase
    #print(colored('[BOT-TTS-VIETTEL]: '+text,'green'))
    #import time            
    #HTTP Request
    url = 'https://viettelgroup.ai/voice/api/tts/v1/rest/syn'
    #Header Parameters
    #hn-quynhanh2, hcm-diemmy2
    headers = {'Content-type': 'application/json', 'token': token}
    # Body Parameters                        
    data = {'text': text, "voice": voice_name, "id": "2", "without_filter": False, "speed": speed, "tts_return_option": 3}
    #Get response from Server  
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    # Open audio file                             
    uniq_filename = '/tmp/tts_vtcc' + str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.') + '.mp3'
    audio_file= open(uniq_filename, 'wb')
    audio_file.write(response.content)
    audio_file.close()
    os.system("mpg123 "+uniq_filename)
    os.remove(uniq_filename)
    # mixer.music.load(uniq_filename)
    # mixer.music.set_volume(speak_volume)            
    # mixer.music.play()                                    
    # audio = MP3(uniq_filename)
    # t = float (audio.info.length)
    # # print ('Time delay :'+ str(t))
    # time.sleep(round(t)+1)
#Google Cloud Text to Speech
def gcloudsay(phrase,lang):
    try:
        if gender=='Male':
            gcloudgender=texttospeech.enums.SsmlVoiceGender.MALE
        else:
            gcloudgender=texttospeech.enums.SsmlVoiceGender.FEMALE

        synthesis_input = texttospeech.types.SynthesisInput(text=phrase)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code=lang,
            ssml_gender=gcloudgender)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open(ttsfilename, 'wb') as out:
            out.write(response.audio_content)
        if gender=='Male' and lang=='vi':
            os.system('sox ' + ttsfilename + ' ' + malettsfilename + ' pitch -450')
            os.remove(ttsfilename)
            os.system('aplay ' + malettsfilename)
            os.remove(malettsfilename)
        else:
            os.system("mpg123 "+ttsfilename)
            os.remove(ttsfilename)
    except google.api_core.exceptions.ResourceExhausted:
        print("Google cloud text to speech quota exhausted. Using GTTS. Make sure to change the choice in config.yaml")
        gttssay(phrase,lang)

#Word translator
def trans(words,destlang,srclang):
    transword= translator.translate(words, dest=destlang, src=srclang)
    transword=transword.text
    transword=transword.replace("Text, ",'',1)
    transword=transword.strip()
    print(transword)
    return transword

#Text to speech converter with translation
def say(words,sourcelang=None,destinationlang=None):
    if sourcelang!=None and destinationlang!=None:
        if TTSChoice=='GoogleCloud':
            sayword=trans(words,destinationlang,sourcelang)
            gcloudsay(sayword,language)
        elif TTSChoice=='GTTS':
            sayword=trans(words,destinationlang,sourcelang)
            gttssay(sayword,translanguage,gender)
        elif TTSChoice=='VIETTEL':
            sayword=trans(words,destinationlang,sourcelang)
            stt_viettel(sayword)
    else:
        if sourcelang==None:
            sourcelanguage='vi'
        else:
            sourcelanguage=sourcelang
        if sourcelanguage!=translanguage:
            sayword=trans(words,translanguage,sourcelanguage)
        else:
            sayword=words
        if TTSChoice=='GoogleCloud':
            gcloudsay(sayword,language)
        elif TTSChoice=='GTTS':
            gttssay(sayword,translanguage,gender)
        elif TTSChoice=='VIETTEL':
            stt_viettel(sayword)


#Function to get HEX and RGB values for requested colour
def getcolours(phrase):
    usrclridx=idx=phrase.find(custom_action_keyword['Dict']['To'])
    usrclr=query=phrase[usrclridx:]
    usrclr=usrclr.replace(custom_action_keyword['Dict']['To'],"",1)
    usrclr=usrclr.replace("'","",1)
    usrclr=usrclr.replace("}","",1)
    usrclr=usrclr.strip()
    usrclr=usrclr.replace(" ","",1)
    usrclr=usrclr.lower()
    print(usrclr)
    try:
        for colournum, colourname in enumerate(clrlist):
            if usrclr in colourname:
               RGB=clrrgblist[colournum]
               red,blue,green=re.findall('\d+', RGB)
               hexcode=clrhexlist[colournum]
               cname=clrlistfullname[colournum]
               print(cname)
               break
        return red,blue,green,hexcode,cname
    except UnboundLocalError:
        say("Sorry unable to find a matching colour")


#Function to convert FBG to XY for Hue Lights
def convert_rgb_xy(red,green,blue):
    try:
        red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else red / 12.92
        green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else green / 12.92
        blue = pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else blue / 12.92
        X = red * 0.664511 + green * 0.154324 + blue * 0.162028
        Y = red * 0.283881 + green * 0.668433 + blue * 0.047685
        Z = red * 0.000088 + green * 0.072310 + blue * 0.986039
        x = X / (X + Y + Z)
        y = Y / (X + Y + Z)
        return x,y
    except UnboundLocalError:
        say("No RGB values given")

#Custom text to speak notification
def notify_tts(phrase):
    word=(custom_action_keyword['Keywords']['notify_TTS'][0]).lower()
    voice_notify = phrase.replace(word, "")
    voice_notify.strip()
    say(voice_notify)

#Run scripts
def script(phrase):
    for num, name in enumerate(scriptname):
        if name.lower() in phrase:
            conv=scriptname[num]
            command=scriptcommand[num]
            print (command)
            say("Running " +conv)
            os.system(command)

#Radio Station Streaming
def radio(phrase):
    conv = None
    for num, name in reversed(list(enumerate(stnname))):
        if name.lower() in phrase:
            station=stnlink[num]
            conv=stnradio[num]
            print (station)
            break
    if conv is not None:
        say("Tuning into " + conv)
        vlcplayer.media_manager(station,'Radio')
        vlcplayer.media_player(station)
    else:
        say("Station not found")


#ESP6266 Devcies control
def ESP(phrase):
    for num, name in enumerate(devname):
        if name.lower() in phrase:
            dev=devid[num]
            if custom_action_keyword['Dict']['On'] in phrase:
                ctrl='=ON'
                say("Turning On " + name)
            elif custom_action_keyword['Dict']['Off'] in phrase:
                ctrl='=OFF'
                say("Turning Off " + name)
            rq = requests.head("http://"+ip + dev + ctrl)


#Stepper Motor control
def SetAngle(angle):
    if GPIOcontrol:
        duty = angle/18 + 2
        GPIO.output(servopin, True)
        say("Moving motor by " + str(angle) + " degrees")
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        pwm.ChangeDutyCycle(0)
        GPIO.output(servopin, False)
    else:
        say("GPIO controls, is not supported for your device.")



def stop():
    vlcplayer.stop_vlc()

#Parcel Tracking
def parcel_tracking(*, tracking_id=None, slug=None, tracking_number=None, fields=None):
    try:
        result = aftership.tracking.get_tracking(tracking_id=tracking_id,
                                                 slug=slug,
                                                 tracking_number=tracking_number,
                                                 fields=','.join(fields))
    except aftership.exception.NotFound:
        return None
    return result['tracking']

def track():
    if aftershiptracking==False:
        say("Aftership API key has not been entered in the config file.")
    else:
        if len(couriers) != len(trackingids):
            say("Number of courier names and the tracking ids are not matching. Please check the config file.")
        else:
            for x in range(0,len(couriers)):
                trackinginfo=parcel_tracking(slug=couriers[x],tracking_number=trackingids[x],fields=[])
                if trackinginfo==None:
                    say("Looks like the details have not been added to the Aftership tracking database.")
                else:
                    numcheck=len(trackinginfo['checkpoints'])
                    description = trackinginfo['checkpoints'][numcheck-1]['message']
                    parcelid=trackinginfo['tracking_number']
                    trackinfo= ("Parcel Number " + str(x+1)+ " with tracking id " + parcelid + " has "+ description)
                    say(trackinfo)
                    #time.sleep(5)



#RSS Feed Reader
def feed(phrase):
    if 'world news' in phrase:
        URL=worldnews
    elif 'top news' in phrase:
        URL=topnews
    elif 'sports news' in phrase:
        URL=sportsnews
    elif 'tech news' in phrase:
        URL=technews
    elif (custom_action_keyword['Keywords']['RSS'][1]).lower() in phrase:
        URL=quote
    numfeeds=10
    feed=feedparser.parse(URL)
    feedlength=len(feed['entries'])
    print(feedlength)
    if feedlength<numfeeds:
        numfeeds=feedlength
    title=feed['feed']['title']
    say(title)
    if GPIOcontrol:
        #To stop the feed, press and hold stop button
        while GPIO.input(stoppushbutton):
            for x in range(0,numfeeds):
                content=feed['entries'][x]['title']
                print(content)
                say(content)
                summary=feed['entries'][x]['summary']
                print(summary)
                say(summary)
                if not GPIO.input(stoppushbutton):
                  break
            if x == numfeeds-1:
                break
            else:
                continue
    else:
        print("GPIO controls, is not supported for your device. You need to wait for feeds to automatically stop")


##--------------Start of send clickatell sms----------------------
#Function to send SMS with Clickatell api
recivernum=configuration['Clickatell']['Reciever']
clickatell_api=configuration['Clickatell']['Clickatell_API']

def sendClickatell(number, message):
    response=requests.get('https://platform.clickatell.com/messages/http/send?apiKey=' + clickatell_api + '&to=' + number + '&content=' + message)
    if response.status_code == 202:
        say("SMS message sent")
    else:
        say("Error sending SMS message. Check your settings")

def sendSMS(query):
    if clickatell_api != 'ENTER_YOUR_CLICKATELL_API':
        for num, name in enumerate(configuration['Clickatell']['Name']):
            if name.lower() in query:
                conv=recivernum[num]
                command=(custom_action_keyword['Keywords']['Send_sms_clickatell'][0]).lower()
                msg=query.replace(command, "")
                message=msg.replace(name.lower(), "")
                message=message.strip()
                print(message + " , " + name + " , " + conv)
                say("Sends SMS message " + message + " to " + name)
                sendClickatell(conv, message)
    else:
        say("You need to enter Clickatell API")





#----------Getting urls for YouTube autoplay-----------------------------------
def fetchautoplaylist(url,numvideos):
    videourl=url
    autonum=numvideos
    autoplay_urls=[]
    autoplay_urls.append(videourl)
    for i in range(0,autonum):
        response=urllib.request.urlopen(videourl)
        webContent = response.read()
        webContent = webContent.decode('utf-8')
        idx=webContent.find("Up next")
        getid=webContent[idx:]
        idx=getid.find('<a href="/watch?v=')
        getid=getid[idx:]
        getid=getid.replace('<a href="/watch?v=',"",1)
        getid=getid.strip()
        idx=getid.find('"')
        videoid=getid[:idx]
        videourl=('https://www.youtube.com/watch?v='+videoid)
        if not videourl in autoplay_urls:
            i=i+1
            autoplay_urls.append(videourl)
        else:
            i=i-1
            continue
##    print(autoplay_urls)
    return autoplay_urls






#-----------------Start of Functions for YouTube Streaming---------------------

def YouTube_Autoplay(phrase):
    try:
        urllist=[]
        currenttrackid=0
        track=phrase
        track = track.replace(custom_action_keyword['Keywords']['YouTube_music_stream'][0],'')
        #track = track.replace(custom_action_keyword['Keywords']['Phatmotbai'][1],'')
        track=track.strip()
        #say("Phát danh sách "+track)
        print(track)
        autourls=youtube_search(track,10) # Maximum of 10 URLS
        print(autourls)
        #say("Adding autoplay links to the playlist")
        for i in range(0,len(autourls)):
            audiostream,videostream=youtube_stream_link(autourls[i])
            streamurl=audiostream
            urllist.append(streamurl)
        if not urllist==[]:
                vlcplayer.media_manager(urllist,'YouTube')
                vlcplayer.youtube_player(currenttrackid)
        else:
            say("Unable to find songs matching your request")
            say('không tìm thấy bài hát ' +track+ 'vui lòng thực hiện lại')

    except Exception as e:
        print(e)
        say('gặp lỗi trong quá trình tìm kiếm, vui lòng kiểm tra cài đặt.')

def YouTube_No_Autoplay(phrase):
    urllist = []
    currenttrackid = 0
    track = phrase
    result = None
    track = track.replace('phát bài hát','')
    track = track.replace('mở bài hát','')
    track = track.replace('zing','')
    track = track.replace(custom_action_keyword['Keywords']['YouTube_music_stream'][0],'')
    track = track.replace(custom_action_keyword['Keywords']['Phat_mot_bai'][0],'')
    track = track.replace(custom_action_keyword['Keywords']['Phat_mot_bai'][1],'')
    track = track.strip()
    print(track)
    #print("Tìm bài hát trên zingmp3.vn: "+data+"...")
    say('phát bài hát '+track+' trên zing.vn')
    try:
        resp = requests.get('http://ac.mp3.zing.vn/complete/desktop?type=song&query='+urllib.parse.quote(track))
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        songID = obj["data"][1]['song'][0]['id']
        songUrl= "https://mp3.zing.vn/bai-hat/"+songID+".html"
        print(songUrl)
        resp = requests.get(songUrl)
        #print(resp.text)
        key = re.findall('data-xml="\/media\/get-source\?type=audio&key=([a-zA-Z0-9]{20,35})', resp.text)
        # # key = re.findall('data-xml="\/media\/get-source\?type=video&key=([a-zA-Z0-9]{20,35})', resp.text)
        songApiUrl = "https://mp3.zing.vn/xhr/media/get-source?type=audio&key="+key[0]
        resp = requests.get(songApiUrl)
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        #print(str(obj))
        mp3Source = "https:"+obj["data"]["source"]["128"]
        realURLdata = requests.get(mp3Source,allow_redirects=False)
        #print(realURLdata)
        realURL = realURLdata.headers['Location']
        file_name, headers = urlretrieve(realURL)
        print(realURL)
        result=file_name
        if result is not None:
            #fullurl=result
            vlcplayer.media_manager(result,'zing')
            vlcplayer.media_player(result)
        else:
            pass
        #say("Phát bài hát "+track)  
    except (IndexError, ValueError):
        print(track)
        say('Không tìm thấy bài hát yêu cầu của bạn trên zing.vn, thực hiện phát bài hát trên yotube') 

        urlid=youtube_search(track)
        if urlid is not None:
            fullurl="https://www.youtube.com/watch?v="+urlid
            audiostream,videostream=youtube_stream_link(fullurl)
            streamurl=audiostream
            urllist.append(streamurl)
            vlcplayer.media_manager(urllist,'YouTube')
            vlcplayer.youtube_player(currenttrackid)
        else:
            say('không tìm thấy bài hát '+ track + 'vui lòng thực hiện lại')  
        pass        
    return result   

#-----------------End of Functions for YouTube Streaming---------------------



#--------------Start of Chromecast functions-----------------------------------

def chromecast_play_video(phrase):
    # Chromecast declarations
    # Do not rename/change "TV" its a variable
    TV = pychromecast.Chromecast("192.168.1.13") #Change ip to match the ip-address of your Chromecast
    mc = TV.media_controller
    idx1=phrase.find(custom_action_keyword['Dict']['Play'])
    idx2=phrase.find('on chromecast')
    query=phrase[idx1:idx2]
    query=query.replace(custom_action_keyword['Dict']['Play'],'',1)
    query=query.replace('on chromecast','',1)
    query=query.strip()
    youtubelinks=youtube_search(query)
    youtubeurl=youtubelinks[0]
    streams=youtube_stream_link(youtubeurl)
    videostream=streams[1]
    TV.wait()
    time.sleep(1)
    mc.play_media(videostream,'video/mp4')

def chromecast_control(action):
    # Chromecast declarations
    # Do not rename/change "TV" its a variable
    TV = pychromecast.Chromecast("192.168.1.13") #Change ip to match the ip-address of your Chromecast
    mc = TV.media_controller
    if 'pause'.lower() in str(action).lower():
        TV.wait()
        time.sleep(1)
        mc.pause()
    if 'resume'.lower() in str(action).lower():
        TV.wait()
        time.sleep(1)
        mc.play()
    if 'end'.lower() in str(action).lower():
        TV.wait()
        time.sleep(1)
        mc.stop()
    if 'volume'.lower() in str(action).lower():
        if 'up'.lower() in str(action).lower():
            TV.wait()
            time.sleep(1)
            TV.volume_up(0.2)
        if 'down'.lower() in str(action).lower():
            TV.wait()
            time.sleep(1)
            TV.volume_down(0.2)

#-------------------End of Chromecast Functions---------------------------------

#-------------------Start of Kickstarter Search functions-----------------------
def campaign_page_parser(campaignname):
    page_link=kickstrater_search(campaignname)
    kicktrackurl=page_link['items'][0]['link']
    response=urllib.request.urlopen(kicktrackurl)
    webContent = response.read()
    webContent = webContent.decode('utf-8')
    return webContent

def kickstarter_get_data(page_source,parameter):
    idx=page_source.find(parameter)
    info=page_source[idx:]
    info=info.replace(parameter,"",1)
    idx=info.find('"')
    info=info[:idx]
    info=info.replace('"',"",1)
    info=info.strip()
    result=info
    return result

def get_campaign_title(campaign):
    campaigntitle=campaign
    campaigntitleidx1=campaigntitle.find('<title>')
    campaigntitleidx2=campaigntitle.find('&mdash;')
    campaigntitle=campaigntitle[campaigntitleidx1:campaigntitleidx2]
    campaigntitle=campaigntitle.replace('<title>',"",1)
    campaigntitle=campaigntitle.replace('&mdash;',"",1)
    campaigntitle=campaigntitle.strip()
    return campaigntitle

def get_pledges_offered(campaign):
    pledgesoffered=campaign
    pledgenum=0
    for num in re.finditer('pledge__reward-description pledge__reward-description--expanded',pledgesoffered):
        pledgenum=pledgenum+1
    return pledgenum

def get_funding_period(campaign):
    period=campaign
    periodidx=period.find('Funding period')
    period=period[periodidx:]
    periodidx=period.find('</p>')
    period=period[:periodidx]
    startperiodidx1=period.find('class="invisible-if-js js-adjust-time">')
    startperiodidx2=period.find('</time>')
    startperiod=period[startperiodidx1:startperiodidx2]
    startperiod=startperiod.replace('class="invisible-if-js js-adjust-time">','',1)
    startperiod=startperiod.replace('</time>','',1)
    startperiod=startperiod.strip()
    period2=period[startperiodidx2+5:]
    endperiodidx1=period2.find('class="invisible-if-js js-adjust-time">')
    endperiodidx2=period2.find('</time>')
    endperiod=period2[endperiodidx1:endperiodidx2]
    endperiod=endperiod.replace('class="invisible-if-js js-adjust-time">','',1)
    endperiod=endperiod.replace('</time>','',1)
    endperiod=endperiod.strip()
    duration=period2[endperiodidx2:]
    duration=duration.replace('</time>','',1)
    duration=duration.replace('(','',1)
    duration=duration.replace(')','',1)
    duration=duration.replace('days','day',1)
    duration=duration.strip()
    return startperiod,endperiod,duration

def kickstarter_tracker(phrase):
    idx=phrase.find('of')
    campaign_name=phrase[idx:]
    campaign_name=campaign_name.replace("kickstarter campaign", "",1)
    campaign_name = campaign_name.replace('of','',1)
    campaign_name=campaign_name.strip()
    campaign_source=campaign_page_parser(campaign_name)
    campaign_title=get_campaign_title(campaign_source)
    campaign_num_rewards=get_pledges_offered(campaign_source)
    successidx=campaign_source.find('to help bring this project to life.')
    if str(successidx)==str(-1):
        backers=kickstarter_get_data(campaign_source,'data-backers-count="')
        totalpledged=kickstarter_get_data(campaign_source,'data-pledged="')
        totaltimerem=kickstarter_get_data(campaign_source,'data-hours-remaining="')
        totaldur=kickstarter_get_data(campaign_source,'data-duration="')
        endtime=kickstarter_get_data(campaign_source,'data-end_time="')
        goal=kickstarter_get_data(campaign_source,'data-goal="')
        percentraised=kickstarter_get_data(campaign_source,'data-percent-raised="')
        percentraised=round(float(percentraised),2)
        if int(totaltimerem)>0:
            #print(campaign_title+" is an ongoing campaign with "+str(totaltimerem)+" hours of fundraising still left." )
            say(campaign_title+" is an ongoing campaign with "+str(totaltimerem)+" hours of fundraising still left." )
            #print("Till now, "+str(backers)+ " backers have pledged for "+str(campaign_num_rewards)+" diferent rewards raising $"+str(totalpledged)+" , which is "+str(percentraised)+" times the requested amount of $"+str(goal))
            say("Till now, "+str(backers)+ " backers have pledged for "+str(campaign_num_rewards)+" diferent rewards raising $"+str(totalpledged)+" , which is "+str(percentraised)+" times the requested amount of $"+str(goal))
        if float(percentraised)<1 and int(totaltimerem)<=0:
            #print(campaign_title+" has already ended")
            say(campaign_title+" has already ended")
            #print(str(backers)+ " backers raised $"+str(totalpledged)+" , which was "+str(percentraised)+" times the requested amount of $"+str(goal))
            say(str(backers)+ " backers raised $"+str(totalpledged)+" , which was "+str(percentraised)+" times the requested amount of $"+str(goal))
            #print(campaign_title+" was unseccessful in raising the requested amount of $"+str(goal)+" ." )
            say(campaign_title+" was unseccessful in raising the requested amount of $"+str(goal)+" ." )
        if float(percentraised)>1 and int(totaltimerem)<=0:
            #print(campaign_title+" has already ended")
            say(campaign_title+" has already ended")
            #print(str(backers)+ " backers raised $"+str(totalpledged)+" , which was "+str(percentraised)+" times the requested amount of $"+str(goal))
            say(str(backers)+ " backers raised $"+str(totalpledged)+" , which was "+str(percentraised)+" times the requested amount of $"+str(goal))
            #print("Though the funding goal was reached, due to reasons undisclosed, the campaign was either cancelled by the creator or Kickstarter.")
            say("Though the funding goal was reached, due to reasons undisclosed, the campaign was either cancelled by the creator or Kickstarter.")
    else:
        [start_day,end_day,numdays]=get_funding_period(campaign_source)
        campaigninfo=campaign_source[(successidx-100):(successidx+35)]
        campaignidx=campaigninfo.find('<b>')
        campaigninfo=campaigninfo[campaignidx:]
        campaigninfo=campaigninfo.replace('<b>',"",1)
        campaigninfo=campaigninfo.replace('</b>',"",1)
        campaigninfo=campaigninfo.replace('<span class="money">',"",1)
        campaigninfo=campaigninfo.replace('</span>',"",1)
        campaigninfo=campaigninfo.strip()
        #print(campaign_title+" was a "+str(numdays)+" campaign launched on "+str(start_day))
        #print(campaigninfo)
        say(campaign_title+" was a "+str(numdays)+" campaign launched on "+str(start_day))
        say(campaigninfo)

#------------------------------End of Kickstarter Search functions---------------------------------------


#----------------------------------Start of Push Message function-----------------------------------------
def pushmessage(title,body):
    if pb!=None:
        push = pb.push_note(title,body)
    else:
        say("Pushbullet API key has not been entered.")
#----------------------------------End of Push Message Function-------------------------------------------


#----------------------------------Start of recipe Function----------------------------------------------
def getrecipe(item):
    appid='ENTER-YOUR-APPID-HERE'
    appkey='ENTER-YOUR-APP-KEY-HERE'
    recipeurl = 'https://api.edamam.com/search?q='+item+'&app_id='+appid+'&app_key='+appkey
    print(recipeurl)
    recipedetails = urllib.request.urlopen(recipeurl)
    recipedetails=recipedetails.read()
    recipedetails = recipedetails.decode('utf-8')
    recipedetails=json.loads(recipedetails)
    recipe_ingredients=str(recipedetails['hits'][0]['recipe']['ingredientLines'])
    recipe_url=recipedetails['hits'][0]['recipe']['url']
    recipe_name=recipedetails['hits'][0]['recipe']['label']
    recipe_ingredients=recipe_ingredients.replace('[','',1)
    recipe_ingredients=recipe_ingredients.replace(']','',1)
    recipe_ingredients=recipe_ingredients.replace('"','',1)
    recipe_ingredients=recipe_ingredients.strip()
    print(recipe_name)
    print("")
    print(recipe_url)
    print("")
    print(recipe_ingredients)
    compiled_recipe_info="\nRecipe Source URL:\n"+recipe_url+"\n\nRecipe Ingredients:\n"+recipe_ingredients
    pushmessage(str(recipe_name),str(compiled_recipe_info))

#---------------------------------End of recipe Function------------------------------------------------


#--------------------------------Start of Hue Control Functions------------------------------------------

def hue_control(phrase,lightindex,lightaddress):
    with open('/opt/hue-emulator/config.json', 'r') as config:
         hueconfig = json.load(config)
    currentxval=hueconfig['lights'][lightindex]['state']['xy'][0]
    currentyval=hueconfig['lights'][lightindex]['state']['xy'][1]
    currentbri=hueconfig['lights'][lightindex]['state']['bri']
    currentct=hueconfig['lights'][lightindex]['state']['ct']
    huelightname=str(hueconfig['lights'][lightindex]['name'])
    try:
        if custom_action_keyword['Dict']['On'] in phrase:
            huereq=requests.head("http://"+lightaddress+"/set?light="+lightindex+"&on=true")
            say("Turning on "+huelightname)
        if custom_action_keyword['Dict']['Off'] in phrase:
            huereq=requests.head("http://"+lightaddress+"/set?light="+lightindex+"&on=false")
            say("Turning off "+huelightname)
        if 'çolor' in phrase:
            rcolour,gcolour,bcolour,hexcolour,colour=getcolours(phrase)
            print(str([rcolour,gcolour,bcolour,hexcolour,colour]))
            xval,yval=convert_rgb_xy(int(rcolour),int(gcolour),int(bcolour))
            print(str([xval,yval]))
            huereq=requests.head("http://"+lightaddress+"/set?light="+lightindex+"&x="+str(xval)+"&y="+str(yval)+"&on=true")
            print("http://"+lightaddress+"/set?light="+lightindex+"&x="+str(xval)+"&y="+str(yval)+"&on=true")
            say("Setting "+huelightname+" to "+colour)
        if (custom_action_keyword['Dict']['Brightness']).lower() in phrase:
            if 'hundred'.lower() in phrase or custom_action_keyword['Dict']['Maximum'] in phrase:
                bright=100
            elif 'zero'.lower() in phrase or custom_action_keyword['Dict']['Minimum'] in phrase:
                bright=0
            else:
                bright=re.findall('\d+', phrase)
            brightval= (bright/100)*255
            huereq=requests.head("http://"+lightaddress+"/set?light="+lightindex+"&on=true&bri="+str(brightval))
            say("Changing "+huelightname+" brightness to "+bright+" percent")
    except (requests.exceptions.ConnectionError,TypeError) as errors:
        if str(errors)=="'NoneType' object is not iterable":
            print("Type Error")
        else:
            say("Device not online")

#------------------------------End of Hue Control Functions---------------------------------------------

#------------------------------Start of Spotify Functions-----------------------------------------------

def show_spotify_track_names(tracks):
    spotify_tracks=[]
    for i, item in enumerate(tracks['items']):
        track = item['track']
##        print ("%d %32.32s %s" % (i, track['artists'][0]['name'],track['name']))
        # print ("%s %s" % (track['artists'][0]['name'],track['name']))
        spotify_tracks.append("%s %s" % (track['artists'][0]['name'],track['name']))
    return spotify_tracks

def scan_spotify_playlists():
    if spotify_token:
        i=0
        playlistdetails=[]
        spotify_tracks_list=[]
        sp = spotipy.Spotify(auth=spotify_token)
        # print(sp.user(username))
        # print("")
        # print("")
        playlists = sp.user_playlists(username)
        print(len(playlists['items']))
        num_playlists=len(playlists['items'])
        spotify_playlists={"Playlists":[0]*(len(playlists['items']))}
        # print(spotify_playlists)
        # print("")
        # print("")
        for playlist in playlists['items']:
            # print (playlist['name'])
            playlist_name=playlist['name']
            # print("")
            # print("")
##            print ('  total tracks', playlist['tracks']['total'])
##            print("")
##            print("")
            results = sp.user_playlist(playlist['owner']['id'], playlist['id'],fields="tracks,next")
            tracks = results['tracks']
            spotify_tracks_list=show_spotify_track_names(tracks)
            playlistdetails.append(i)
            playlistdetails.append(playlist_name)
            playlistdetails.append(spotify_tracks_list)
            spotify_playlists['Playlists'][i]=playlistdetails
            playlistdetails=[]
            i=i+1
        # print("")
        # print("")
        # print(spotify_playlists['Playlists'])
        return spotify_playlists, num_playlists
    else:
        say("Can't get token for, " + username)
        print("Can't get token for ", username)

def spotify_playlist_select(phrase):
    trackslist=[]
    currenttrackid=0
    idx1=phrase.find(custom_action_keyword['Dict']['Play'])
    idx2=phrase.find(custom_action_keyword['Dict']['From_spotify'])
    track=phrase[idx1:idx2]
    track = track.replace(custom_action_keyword['Dict']['Play'],'',1)
    track = track.replace(custom_action_keyword['Dict']['From_spotify'],'',1)
    track=track.strip()
    say("Getting music links")
    print(track)
    playlists,num=scan_spotify_playlists()
    if not num==[]:
        for i in range(0,num):
            print(str(playlists['Playlists'][i][1]).lower())
            if track in str(playlists['Playlists'][i][1]).lower():
                trackslist=playlists['Playlists'][i][2]
                break
        if not trackslist==[]:
            vlcplayer.media_manager(trackslist,'Spotify')
            vlcplayer.spotify_player(currenttrackid)
    else:
        say("Unable to find matching playlist")

#----------------------End of Spotify functions---------------------------------

#----------------------Start of Domoticz Control Functions----------------------
def domoticz_control(query,index,devicename):
    global hexcolour,bright,devorder
    try:
        for j in range(0,len(domoticz_devices['result'])):
            if domoticz_devices['result'][j]['idx']==index:
                devorder=j
                break

        if (' ' + custom_action_keyword['Dict']['On'] + ' ') in query or (' ' + custom_action_keyword['Dict']['On']) in query or (custom_action_keyword['Dict']['On'] + ' ') in query:
            devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=switchlight&idx=" + index + "&switchcmd=On",verify=False)
            say('Turning on ' + devicename )
        if custom_action_keyword['Dict']['Off'] in query:
            devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=switchlight&idx=" + index + "&switchcmd=Off",verify=False)
            say('Turning off ' + devicename )
        if 'toggle' in query:
            devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=switchlight&idx=" + index + "&switchcmd=Toggle",verify=False)
            say('Toggling ' + devicename )
        if custom_action_keyword['Dict']['Colour'] in query:
            if 'RGB' in domoticz_devices['result'][devorder]['SubType']:
                rcolour,gcolour,bcolour,hexcolour,colour=getcolours(query)
                hexcolour=hexcolour.replace("#","",1)
                hexcolour=hexcolour.strip()
                print(hexcolour)
                if bright=='':
                    bright=str(domoticz_devices['result'][devorder]['Level'])
                devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=setcolbrightnessvalue&idx=" + index + "&hex=" + hexcolour + "&brightness=" + bright + "&iswhite=false",verify=False)
                say('Setting ' + devicename + ' to ' + colour )
            else:
                say('The requested light is not a colour bulb')
        if custom_action_keyword['Dict']['Brightness'] in query:
            if domoticz_devices['result'][devorder]['HaveDimmer']:
                if 'hundred' in query or 'hundred'.lower() in query or custom_action_keyword['Dict']['Maximum'] in query:
                    bright=str(100)
                elif 'zero' in query or custom_action_keyword['Dict']['Minimum'] in query:
                    bright=str(0)
                else:
                    bright=re.findall('\d+', query)
                    bright=bright[0]
                devreq=requests.head("https://" + configuration['Domoticz']['Server_IP'][0] + ":" + configuration['Domoticz']['Server_port'][0] + "/json.htm?type=command&param=switchlight&idx=" + index + "&switchcmd=Set%20Level&level=" + bright ,verify=False)
                say('Setting ' + devicename + ' brightness to ' + str(bright) + ' percent.')
            else:
                say('The requested light does not have a dimer')

    except (requests.exceptions.ConnectionError,TypeError) as errors:
        if str(errors)=="'NoneType' object is not iterable":
            print("Type Error")
        else:
            say("Device or Domoticz server is not online")
#------------------------End of Domoticz Control Functions----------------------

#------------------------Start of Gaana Functions-------------------------------
def getgaanaplaylistinfo(playlisturl):
    trackstart=[]
    trackend=[]
    playliststart=[]
    playlistend=[]
    trackdetails=[]
    response=urllib.request.urlopen(playlisturl)
    response=response.read().decode('utf-8')
    for a in re.finditer('{"title":',response):
        trackstart.append(a.start())
    for b in re.finditer('"parental_warning":(.*)}',response):
        trackend.append(b.end())
    for c in re.finditer('{"source":',response):
        playliststart=c.start()
    for d in re.finditer('}</span>',response):
        playlistend=int(d.start())+1
    playlistinfo=json.loads(response[playliststart:playlistend])
    playlistname=playlistinfo['title']
    if len(trackstart)==len(trackend) and len(trackstart)>0:
        for i in range(0,len(trackstart)):
            trackdetails.append(json.loads(response[trackstart[i]:trackend[i]]))
    else:
        trackdetails=[]
    numtracks=len(trackdetails)
    return playlistname,numtracks,trackdetails

def gaana_playlist_select(phrase):
    trackslist=[]
    currenttrackid=0
    idx1=phrase.find(custom_action_keyword['Dict']['Play'])
    idx2=phrase.find(custom_action_keyword['Dict']['From_gaana'])
    track=phrase[idx1:idx2]
    track = track.replace(custom_action_keyword['Dict']['Play'],'',1)
    track = track.replace(custom_action_keyword['Dict']['From_gaana'],'',1)
    track=track.strip()
    playlistnumreq=re.findall(r'\b\d+\b', track)
    if playlistnumreq !=[]:
        playlistnumreq=playlistnumreq[0]
    userplaylists=configuration['Gaana']['Playlist']
    numuserplaylists=len(userplaylists)
    if playlistnumreq !=[] and "top" not in track and int(playlistnumreq) <= int(numuserplaylists):
        print("Getting links for playlist number " + playlistnumreq)
        say("Getting links for playlist number " + playlistnumreq)
        reqplaylist=configuration['Gaana']['Playlist'][(int(playlistnumreq)-1)]
    else:
        print("Searching for " + track +  " in gaana.com")
        say("Searching for " + track +  " in gaana.com")
        page_link=gaana_search(track)
        reqplaylist=page_link['items'][0]['link']
    name,numsongs,tracks= getgaanaplaylistinfo(reqplaylist)
    print(numsongs)
    if not numsongs==[]:
        say("Getting the tracks from " + name)
        for i in range(0,numsongs):
            trackslist.append((tracks[i]['title'] + ' ' + tracks[i]['albumtitle']))
        if not trackslist==[]:
            vlcplayer.media_manager(trackslist,'Gaana')
            vlcplayer.gaana_player(currenttrackid)
    else:
        say("Unable to find matching playlist")

#------------------------End of Gaana Functions-------------------------------

#------------------------Start of Deezer Functions-------------------------------
def deezer_playlist_select(phrase):
    trackslist=[]
    deezer_user_playlists=[]
    currenttrackid=0
    idx1=phrase.find(custom_action_keyword['Dict']['Play'])
    idx2=phrase.find(custom_action_keyword['Dict']['From_deezer'])
    track=phrase[idx1:idx2]
    track = track.replace(custom_action_keyword['Dict']['Play'],'',1)
    track = track.replace(custom_action_keyword['Dict']['From_deezer'],'',1)
    track=track.strip()
    playlistnumreq=re.findall(r'\b\d+\b', track)
    if playlistnumreq !=[]:
        playlistnumreq=playlistnumreq[0]
    deezer_response = requests.get("https://api.deezer.com/user/" + configuration['Deezer']['User_id'] + "/playlists",verify=False)
    deezer_user_playlist_info=json.loads(deezer_response.text)
    if deezer_user_playlist_info['data'] != []:
        for i in range(0,len(deezer_user_playlist_info['data'])):
            deezer_user_playlists.append(deezer_user_playlist_info['data'][i]['tracklist'])
    else:
        say("No playlists found for the user")
    numuserplaylists=len(deezer_user_playlists)
    if playlistnumreq !=[] and "top" not in track and int(playlistnumreq) <= int(numuserplaylists):
        print("Getting links for playlist number " + playlistnumreq)
        say("Getting links for playlist number " + playlistnumreq)
        tracklisturl=deezer_user_playlists[(int(playlistnumreq)-1)]
    else:
        say("No matching playlists found")
    deezer_tracks_response = requests.get(tracklisturl,verify=False)
    deezer_user_playlist_tracks_info=json.loads(deezer_tracks_response.text)
    numsongs=len(deezer_user_playlist_tracks_info['data'])
    if not numsongs==[]:
        say("Getting the tracks from " + deezer_user_playlist_info['data'][int(playlistnumreq)-1]['title'])
        for i in range(0,numsongs):
            trackslist.append((deezer_user_playlist_tracks_info['data'][i]['title'] + ' by ' + deezer_user_playlist_tracks_info['data'][i]['artist']['name'] + ' from ' + deezer_user_playlist_tracks_info['data'][i]['album']['title']))
        if not trackslist==[]:
            vlcplayer.media_manager(trackslist,'Deezer')
            vlcplayer.gaana_player(currenttrackid)
    else:
        say("Unable to find matching tracks")

#------------------------End of Deezer Functions-------------------------------

#-----------------------Start of functions for IR code--------------------------

def binary_aquire(pin, duration):
    t0 = time.time()
    results = []
    while (time.time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results

def on_ir_receive(pinNo, bouncetime=150):
    data = binary_aquire(pinNo, bouncetime/1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        return None

#-----------------------End of functions for IR code--------------------------

#-----------------------Start of functions for Wemo/Emulated Wemo-------------

def wemodiscovery():
    devices = pywemo.discover_devices()
    if devices!=[]:
        with open('{}/wemodevicelist.json'.format(USER_PATH), 'w') as devicelist:
               json.dump(devices, devicelist)
        if len(devices)>1:
            say("Found "+str(len(devices))+" devices.")
        else:
            say("Found "+str(len(devices))+" device.")
    else:
        say("Unable to find any active device.")

def wemocontrol(command):
    if os.path.isfile("{}/wemodevicelist.json".format(USER_PATH)):
        with open('{}/wemodevicelist.json'.format(USER_PATH), 'r') as devicelist:
            wemodevices = json.load(devicelist)
        if wemodevices!=[]:
            for i in range(0,len(wemodevices)):
                if wemodevices[i] in command:
                    if (' ' + custom_action_keyword['Dict']['On'] + ' ') in command or (' ' + custom_action_keyword['Dict']['On']) in query or (custom_action_keyword['Dict']['On'] + ' ') in command:
                        wemodevices[i].on()
                        say("Turning on "+wemodevices[i])
                    elif custom_action_keyword['Dict']['Off'] in command:
                        wemodevices[i].on()
                        say("Turning off "+wemodevices[i])
                    break
        else:
            say("Device list is empty. Try running the device discovery.")
    else:
        say("Unable to find device registry. Try running the device discovery.")

#-----------------------End of functions for Wemo/Emulated Wemo-------------

#Send voicenote to phone
def voicenote(audiofile):
    if pb!=None:
        say("Sending your voicenote")
        with open(audiofile, "rb") as recordedvoicenote:
            file_data = pb.upload_file(recordedvoicenote, 'Voicenote.wav')
        push = pb.push_file(**file_data)
    else:
        say("Pushbullet API key has not been entered.")

#GPIO Device Control
def Action(phrase):
    if 'shutdown' in phrase:
        say('Shutting down Raspberry Pi')
        time.sleep(10)
        os.system("sudo shutdown -h now")
        #subprocess.call(["shutdown -h now"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if 'servo' in phrase:
        for s in re.findall(r'\b\d+\b', phrase):
            SetAngle(int(s))
        if 'zero' in phrase:
            SetAngle(0)
    else:
        if GPIOcontrol:
            for num, name in enumerate(var):
                if name.lower() in phrase:
                    pinout=gpio[num]
                    if custom_action_keyword['Dict']['On'] in phrase:
                        GPIO.output(pinout, 1)
                        say("Turning On " + name)
                    elif custom_action_keyword['Dict']['Off'] in phrase:
                        GPIO.output(pinout, 0)
                        say("Turning Off " + name)
        else:
            say("GPIO controls, is not supported for your device.")


#############lịch âm

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import lun
from lun import S2L
from lun import L2S


def licham(usrcmd):
    print('[ViPi]: XỬ LÝ CÂU LỆNH ÂM LỊCH: '+usrcmd)
    if (custom_action_keyword['Keywords']['request_day'][0]).lower() in str(usrcmd).lower():       
        kiemtra_amlich(check_last_day())    
    elif (custom_action_keyword['Keywords']['request_day'][1]).lower() in str(usrcmd).lower():  
        kiemtra_amlich(check_to_day())    
    elif (custom_action_keyword['Keywords']['request_day'][2]).lower() in str(usrcmd).lower():  
        kiemtra_amlich(check_tomorrow())    
    elif (custom_action_keyword['Keywords']['request_day'][3]).lower() in str(usrcmd).lower():  
        kiemtra_amlich(check_next_day())    
    else:
        kiemtra_amlich(check_last_day())     
        pass
                                   
def check_last_day():
    print ('Âm lịch hôm qua')
    a = 'Hôm qua'
    ngay = datetime.date.today() - timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day    
    return a,ngay,yy,mm,dd

def check_to_day():
    a = 'Hôm nay'
    print ('âm lịch hôm nay')
    ngay = datetime.date.today()
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    list = [a,ngay,yy,mm,dd]
    return list
def check_tomorrow():
    print ('Âm lịch ngày mai')
    a = 'Ngày mai'
    ngay = datetime.date.today() + timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def check_next_day():
    print ('Âm lịch ngày mốt')
    a = 'Ngày mốt'
    ngay = datetime.date.today() + timedelta(2)
    yy = ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def check_other_day(data):
    today=datetime.date.today()
    print ('Âm lịch ngày')
    if 'NGÀY' in data:
        ngay = re.search('NGÀY (.+?)(.+?)', data)
        dd = int(ngay.group(1)+ngay.group(2))
    else: 
        dd = today.day
    if 'THÁNG' in data:
        thang = re.search('THÁNG (.+?)(.+?)', data)
        mm = int(thang.group(1)+thang.group(2)) 
    else:
        mm = today.month    
    yy = today.year     
    a = 'Ngày '+str(dd)+ 'tháng '+str(mm)
    daa = str(yy)+'-'+str(mm)+'-'+str(dd)
    ngay = datetime.datetime.strptime(daa, '%Y-%m-%d')
    a = 'Ngày '+str(dd)+ 'tháng '+str(mm)+' năm nay'
    return a,ngay,yy,mm,dd



def kiemtra_amlich(list):
    a = list[0]
    ngay = list[1]
    yy = list[2]
    mm = list[3]
    dd = list[4]
    lunar_date = S2L(dd, mm, yy)
    ngay_am = str(lunar_date[0])
    list_thang = ["tháng Giêng","tháng Hai","tháng Ba","tháng Tư","tháng Năm","tháng Sáu","tháng Bảy","tháng Tám","tháng Chín","tháng Mười","tháng Mười một","tháng Chạp"]
    thang_am = int(str(lunar_date[1]))-1
    thang_am1 = list_thang[thang_am]
    can = ['Canh ', 'Tân ', 'Nhâm ', 'Quý ', 'Giáp ', 'Ất ', 'Bính ', 'Đinh ','Mậu ','Kỷ ']
    chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
    nam = int(str(lunar_date[2]))
    vitri_can = nam % 10
    vitri_chi = nam % 12
    nam_am = str(lunar_date[2])
    # lunar_text2 = 'Ngày: ' + str(lunar_date[0]) + ' - ' + thang_am1  + ' năm '  + can[vitri_can] + chi[vitri_chi] + ' (' +  str(lunar_date[2]) +')'
    ss = int(ngay_am)
    nam_nhuan = int(str(lunar_date[3])) 
    if ss == 15:
        say(a+" âm lịch là rằm "+ thang_am1 + 'năm ' + can[vitri_can] +' '+ chi[vitri_chi]+' ' + nam_am)
    elif ss == 1:
        say(a+" âm lịch là mùng một "+ thang_am1 + 'năm ' + can[vitri_can] +' '+ chi[vitri_chi]+ ' ' + nam_am)
    elif ss>1 and ss<15:
        days_left = 15 - ss
        say(a+" âm lịch là " + ngay_am +' '+ thang_am1 + ' năm ' + can[vitri_can] +' '+ chi[vitri_chi] +' '+ nam_am + ". Còn " + str(days_left) + " ngày nữa là đến rằm ")
    elif ss>15 and ss<31:
        thang_sau = thang_am + 1
        if thang_am <= 12:
            nam_a = nam_am 
        else:
            nam_a = nam_am + 1
            # ny = yy + 1
            a2d = L2S(28,12,yy,nam_nhuan)
            nd = a2d[0]
            td = a2d[1]
            nmd = a2d[2]
            daa = str(nd)+'-'+str(td)+'-'+str(nmd)
            a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
            ngaytet = a2dnew.day
            thangtet = a2dnew.month
            namtet = a2dnew.year
            nammoi = S2L(ngaytet,thangtet,namtet)
            nam_nhuan = int(str(nammoi[3]))
        next = L2S(1,thang_sau,int(nam_a), nam_nhuan)
        nd = next[0]
        td = next[1]
        nmd = next[2]
        daa = str(nd)+'-'+str(td)+'-'+str(nmd)
        a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
        delta = a2dnew - datetime.datetime.today()
        days_left = delta.days
        thang_am = list_thang[thang_am]
        ngay_am =str(lunar_date[0])
        say(a+' âm lịch là ' + ngay_am +' '+ thang_am + ' năm ' + can[vitri_can]+' ' + chi[vitri_chi]+' ' + nam_am)                   
    else:
        say(str(a)+'  âm lịch là ' + str(ngay_am)+' ' + str(thang_am) + ' năm ' + str(can[vitri_can])+' ' + str(chi[vitri_chi])+ ' ' + str(nam_am))
 
 
 ################################END LỊCH ÂM#########################
 
 #################################ZING.MP3#############################
 	# elif row0_in_db=="ZING":
		# if seed == 1:
			# pixels.speak()
		# import zing, vlc
		# playlist = zing.zing_song(data)
		# player = zing.phat_zing(playlist)
		# speaking.speak('Đang chuẩn bị phát top 100 ca khúc trên Zing')
		# player.play()
		# if 'TIẾP' in data:
			# print ('Next')
			# player.next()
		# if 'TRƯỚC' in data:
			# print ('Prev')
			# player.previous()		
		# if seed == 1:
			# pixels.off()

	# else:
		# if seed == 1:
			# pixels.speak()
		# answer('em không hiểu','em nghe không rõ',' vui lòng nói lại đi')
		# if seed == 1:
			# # pixels.off()
		# execute.run_thread(wt,data)
# # TIN RADIO
	# elif row0_in_db=="TIN VẮN":
		# import zing
		# if seed == 1:
			# pixels.speak()
		# playlist = news.getlink(data)
		# player = zing.phat_zing(playlist)
		# speaking.speak('Đang chuẩn bị phát tin vắn radio')
		# player.play()
		# if 'TIẾP' in data:
			# print ('Next')
			# player.next()
		# if 'TRƯỚC' in data:
			# print ('Prev')
			# player.previous()
		# if seed == 1:
			# pixels.off()            
            
# #Hàm lấy data
# TOP100 = {'pop':'ZWZB96AB', 'country': 'ZWZB96AE', 'rock': 'ZWZB96AC', 'dance': 'ZWZB96C7', 'r&b': 'ZWZB96C8', 'rap': 'ZWZB96AD', 'soundtrack': 'ZWZB96C9',
          # 'nhac tre':'ZWZB969E', 'tru tinh': 'ZWZB969F', 'que huong': 'ZWZB96AU', 'cach mang': 'ZWZB96AO', 'rock viet': 'ZWZB96A0', 'rap viet': 'ZWZB96AI', 'dance viet': 'ZWZB96AW'}
# url_list = 'https://mp3.zing.vn/xhr/media/get-list?op=top100&start=0&length=20&id='
# url_audio = 'https://mp3.zing.vn/xhr/media/get-source?type=audio&key='
# prefix_url = 'https:'

# def get_codes(type_TOP):
	# type_TOP = type_TOP.lower()
	# uri = url_list + TOP100.get(type_TOP)
	# re = requests.get(uri).json()
	# items = re['data']['items']
	# audio_codes = []
	# for item in items:
		# code = item['code']
		# audio_codes.append(code)
	# return audio_codes

# def get_audio_links(type_TOP):
	# alink = []
	# audio_links = {}
	# codes = get_codes(type_TOP)
	# for code in codes:
		# uri = url_audio + code
		# re = requests.get(uri).json()['data']
		# link = prefix_url + re['source']['128']
		# duration =  int(re['duration'])
		# audio_links[link] = duration
		# alink.append(link)
	# return alink
# def zing_song(data):
	# if 'TRỮ TÌNH' in data.upper():
		# type_TOP = 'tru tinh'
	# elif 'NHẠC TRẺ' in data.upper():
		# type_TOP = 'nhac tre'
	# elif 'QUÊ HƯƠNG' in data.upper():
		# type_TOP = 'que huong'
	# elif 'CÁCH MẠNG' in data.upper():
		# type_TOP = 'cach mang'
	# elif 'ROCK VIỆT' in data.upper():
		# type_TOP = 'rock viet'
	# elif 'RAP VIỆT' in data.upper():
		# type_TOP = 'rap viet'
	# elif 'DANCE VIỆT' in data.upper():
		# type_TOP = 'dance viet'
	# if 'POP' in data.upper():
		# type_TOP = 'pop'
	# elif 'ROCK' in data.upper():
		# type_TOP = 'rock'
	# elif 'COUNTRY' in data.upper():
		# type_TOP = 'country'
	# elif 'DANCE' in data.upper():
		# type_TOP = 'dance'
	# elif 'SOUNDTRACK' in data.upper():
		# type_TOP = 'soundtrack'
	# else:
		# type_TOP = 'nhac tre'
	# print (type_TOP)
	# mp3_links = get_audio_links(type_TOP)
	# return mp3_links
# def phat_zing(playlist):
	# inst = vlc.Instance()
	# player = inst.media_list_player_new()
	# mediaList = inst.media_list_new(playlist)
	# player.set_media_list(mediaList)
	# playing = set([1,2,3,4])
	# return player
# #	print (mp3_links)
# # ZING
	# elif row0_in_db=="ZING":
		# import zing
		# playlist = zing.zing_song(data)
		# player = zing.phat_zing(playlist)
		# speaking.speak('Đang chuẩn bị phát top 100 ca khúc trên Zing')
		# player.play()
		# if 'TIẾP' in data:
			# print ('Next')
			# player.next()
		# if 'TRƯỚC' in data:
			# print ('Prev')
			# player.previous()		

	# else:
		# answer('em không hiểu','em nghe không rõ',' vui lòng nói lại đi')
		# if seed == 1:
			# pixels.off()
  
  ##############Zingmp3########



# data ='thôi đừng chiêm bao'

def zingmp3(phrase):
    #print("Tìm bài hát: "+phrase+"...")
    data=phrase
    data=data.replace('zing','')
    data=data.strip()
    result=None
    print("Tìm bài hát trên zingmp3.vn: "+data+"...")
    currenttrackid=0
    try:
        resp = requests.get('http://ac.mp3.zing.vn/complete/desktop?type=song&query='+urllib.parse.quote(data))
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        songID = obj["data"][1]['song'][0]['id']
        songUrl= "https://mp3.zing.vn/bai-hat/"+songID+".html"
        print(songUrl)
        resp = requests.get(songUrl)
        #print(resp.text)
        key = re.findall('data-xml="\/media\/get-source\?type=audio&key=([a-zA-Z0-9]{20,35})', resp.text)
        # # key = re.findall('data-xml="\/media\/get-source\?type=video&key=([a-zA-Z0-9]{20,35})', resp.text)
        songApiUrl = "https://mp3.zing.vn/xhr/media/get-source?type=audio&key="+key[0]
        resp = requests.get(songApiUrl)
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        #print(str(obj))
        mp3Source = "https:"+obj["data"]["source"]["128"]
        realURLdata = requests.get(mp3Source,allow_redirects=False)
        #print(realURLdata)
        realURL = realURLdata.headers['Location']
        file_name, headers = urlretrieve(realURL)
        print(realURL)
        result=file_name
        if result is not None:
            #fullurl=result
            vlcplayer.media_manager(result,'zing')
            vlcplayer.media_player(result)
        else:
            say("Không tìm thấy bài hát yêu cầu trên zing")     
    except (IndexError, ValueError):
        pass        
    return result
##############YOTUBE##############



# def youtube(data):
    # file_name=None
    # print("Tìm bài hát: "+data+"...")
    # data = data.lower()
    # query_string = urllib.parse.urlencode({"search_query" : data})
    # html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    # list_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    # url = "http://www.youtube.com/watch?v="+list_results[0]
    # info = pafy.new(url)
    # title = info.title
    # file_name_m4a ='/tmp/'+data+'.m4a'
    # file_name_mp3 ='mp3/'+data+'.mp3'            
    # audio = info.m4astreams[-1]
    # audio = info.getbestaudio(preftype="m4a")
    # audio.download(file_name_m4a, quiet=True)
    # ouput=None
    # try:
        # track = AudioSegment.from_file(file_name_m4a,'m4a')
        # print('CONVERTING: ' + str(title))
        # file_handle = track.export(file_name_mp3, format='mp3')
        # file_name = file_name_mp3
    # except:
        # print("ERROR CONVERTING " + str(file_name_m4a))
    # return file_name


# ####################Tìm VB##############

# def travanban(data):
    # list_result=''
    # #HTTP Request
    # url = 'https://vanbanphapluat.co/api/search?kwd='+data
    # response = requests.post(url, verify=False)
    # for i in range(len(response.json()['Items'])):
        # ''.join([list_result,'Kết quả thứ '+i+': Văn bản số: '+ response.json()['Items'][i]['SoHieu']+', nội dung '+response.json()['Items'][i]['TrichYeu'].replace('<em>','').replace('</em>','')])
    
    # # for i in range(len(list_result)):
        # # print(list_result[i])
    # say('list_result')