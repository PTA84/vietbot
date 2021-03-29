import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

import time
import random
import os
from termcolor import colored


with open('config.json') as config_json:
    config_data = json.load(config_json)

spotify_client_id =''
spotify_client_secret =''
spotify_redirect_url=''
spotify_scope="user-library-read,user-read-playback-state,user-modify-playback-state"

for p in config_data['spotify_skill']:
    if p['is_active'] == True:
        spotify_client_id =p['spotify_client_id']
        spotify_client_secret = p['spotify_client_secret']
        spotify_redirect_url=p['spotify_redirect_ur']

def main(data):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                   client_secret=spotify_client_secret,
                                                   redirect_uri=spotify_redirect_url,
                                                   scope=spotify_scope))

    results = sp.search(q=data, type='track',limit=1,market='VN')
    uri_link =''
    track_uri=''
    for i, t in enumerate(results['tracks']['items']):
        track_title=t['name']
        print('Tựa đề: ', track_title)        
        track_uri =t['uri']
        print('Link: ', track_uri)      
    # sp.volume(50)        
    if track_uri =='' or track_uri == None :
        pass
    else: 
        sp.start_playback(uris=[track_uri])
        # res = sp.devices()        
        # print(str(res))

def play_spotify_artist(sp,data):
    results = sp.search(q=data, type='artist',limit=1,market='VN')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['uri'])
    sp.start_playback(id,artist['uri'])
def play_spotify_track(sp,data):
    results = sp.search(q=data, type='track',limit=1,market='VN')
    items = results['tracks']['items']
    if len(items) > 0:
        track = items[0]
        print(artist)
    # sp.start_playback(id,artist['uri'])
# def pause_spotity(self,sp):
def devices(self,sp):
    a=sp.devices()
    a=a['devices']
    device_list=[]
    i=1
    for ass in a:
        name=ass['name']
        id=ass['id']
        volume_cur=ass['volume_percent']
        ee=[i,name,id,volume_cur]
        device_list.append(ee)
        print(device_list) 
        i+=1
    if len(device_list)>1:
        print('em tìm thấy '+str(len(device_list))+ ' thiết bị đang chạy Spotify, anh cần chạy trên thiết bị nào')
        for ii in device_list:
            print('Thiết bị số '+ str(ii[0])+ ' là '+str(ii[1]) )
        # hoi_lai=re_ask()
        print(hoi_lai)
        for iis in device_list:
            if str(iis[0]).upper() in str(hoi_lai).upper() or str(iis[1]).upper() in str(hoi_lai).upper():
                id=iis[2]
                namen=iis[1]
                volume_cur=iis[3]
                print(str(id))
                break
            else:
                id=device_list[0][2]
                namen=device_list[0][1]
                volume_cur=device_list[0][3]
                print(str(id))
        return id,namen,volume_cur
    elif len(device_list)==1:
        id=device_list[0][2]
        namen=device_list[0][1]
        volume_cur=device_list[0][3]
        return id,namen,volume_cur
    else:
        sai='no'
        return sai
def pause(self,sp,id=None):
    sp.pause_playback(id)
def next_track(self,sp,id=None):
    sp.next_track(id)
def previous_track(self,sp,id=None):
    sp.previous_track(id)
def shuffle(self,sp,state,id=None):
    sp.shuffle(state,id)
def play_spotify_playlist(self,sp,id=None):
    aaa=sp.current_user_playlists()
    ofsset=aaa['items'][0]['tracks']['total']
    aaa=aaa['items'][0]['uri']
    offset={'position':random.randint(0,offset)}
    print(offset)
    sp.start_playback(id,aaa,offset=offset)
    print(aaa)
def current_track(self,sp):
    b=sp.current_user_playing_track()
    c=b['item']['name']
    d=b['item']['artists'][0]['name']
    resu=str(c) + " "+ str(d)
    print(resu)
    print("đang phát bài "+str(c) + " trong playlist mặc định do ca sĩ " + str(d) +" trình bày.")
    return result
        
if __name__ == '__main__':
    main(data)   