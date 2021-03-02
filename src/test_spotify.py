import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json
import time
import random
#import speaking
import os
from speaking import short_speak, speak
from termcolor import colored
import gih
import os
import random
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre

spotify_client_id = gih.get_config('spotify_client_id')
spotify_client_secret = gih.get_config('spotify_client_secret')
spotify_redirect_url = gih.get_config('spotify_redirect_url')
spotify_device_id = gih.get_config('spotify_device_id')
request_music=gih.get_request('request_music')
request_music=gih.get_request('request_music')
request_offline=gih.get_request('request_offline')
request_online=gih.get_request('request_online')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')

data ='việt nam ơi'
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH NGHE NHẠC BẰNG SPOTIFY: '+data)
    music_command = str([s for s in request_music if s in data])
    music_command = music_command.replace("['", "")
    music_command = music_command.replace("']", "") 
    data = data.replace(music_command,'')
    online_command = str([s for s in request_online if s in data])
    online_command = online_command.replace("['", "")
    online_command = online_command.replace("']", "") 
    data = data.replace(online_command,'')                
    offline_command = str([s for s in request_offline if s in data])
    offline_command = offline_command.replace("['", "")
    offline_command = offline_command.replace("']", "") 
    data = data.replace(offline_command,'')                      
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                   client_secret=spotify_client_secret,
                                                   redirect_uri=spotify_redirect_url,
                                                   scope="user-library-read,user-read-playback-state,user-modify-playback-state"))
    # sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(),auth_manager=SpotifyOAuth(scope="user-library-read,user-read-playback-state,user-modify-playback-state"))                                                   
    
    if search_track(sp,data) is None:
        short_speak('Không tìm thấy bài hát phù hợp')
        if search_playlist(sp,data) is None:
            short_speak('Không tìm thấy danh sách phù hợp')
            pass
        else:
            short_speak('Tìm thấy danh sách phát có tên là ' +search_playlist(sp,data)[0]+ ' phát danh sách')
            go_play(sp,search_playlist(sp,data)[1])
    else:
        short_speak('Tìm thấy bài hát có tên là ' +search_track(sp,data)[0]+ ' phát bài hát')
        go_play(sp,search_track(sp,data)[1])
        
    # print(search_artist(sp,data))        
    # print(search_playlist(sp,data))    
    # print(search_track(sp,data))    
    # print(search_track(sp,data))      
    
def search_artist(sp,data):
    try:
        results = sp.search(q=data, type='artist',limit=1,market='VN')
        total = results['artists']['total']
        if total == 0:
            return None
        else:
            artist_name=''    
            artist_uri=''        
            for i, t in enumerate(results['artists']['items']):
                artist_name =t['name']
                artist_uri =t['uri']        
            return artist_name, artist_uri
    except Exception as e:
        print(e)
        short_speak('Lỗi xảy ra trong việc tìm kiếm nghệ sĩ')
        time.sleep(1)
        return None
    
def search_playlist(sp,data):
    try:
        results = sp.search(q=data, type='playlist',limit=1,market='VN')
        total = results['playlists']['total']
        if total == 0:
            return None
        else:    
            playlist_name=''    
            playlist_uri=''    
            for i, t in enumerate(results['playlists']['items']):
                playlist_name =t['name']
                playlist_uri =t['uri']        
            return playlist_name, playlist_uri    
    except Exception as e:
        print(e)
        short_speak('Lỗi xảy ra trong việc tìm kiếm danh sách')
        time.sleep(1) 
        return None        
def search_track(sp,data):
    try:
        results = sp.search(q=data, type='track',limit=1,market='VN')
        total = results['tracks']['total']
        if total == 0:
            return None
        else:        
            track_name=''    
            track_uri=''    
            for i, t in enumerate(results['tracks']['items']):
                track_name =t['name']
                track_uri =t['uri']        
            return track_name, track_uri
    except Exception as e:
        print(e)
        short_speak('Lỗi xảy ra trong việc tìm kiếm bài hát')
        time.sleep(1)     
        return None        

        
def go_play(sp,data):
    try:
        sp.transfer_playback(spotify_device_id)
        res = sp.devices()        
        print(res)
        sp.start_playback(uris=[data])
        sp.start_playback(device_id=spotify_device_id,uris=[data])
    except Exception as e:
        print(e)
        short_speak('Lỗi xảy ra trong việc thiết lập và phát nhạc trên thiết bị')
        time.sleep(1)         
if __name__ == '__main__':
    main(data)            
