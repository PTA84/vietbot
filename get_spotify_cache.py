import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import time
import random
#import speaking
import os
data ='HOA NỞ KHÔNG MÀU'
client_id='client_id'
client_secret='client_secret'
redirect_uri='redirect_uri'
scope="user-library-read,user-read-playback-state,user-modify-playback-state"
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH NGHE NHẠC BẰNG SPOTIFY: '+data)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope))

    results = sp.search(q=data, type='track',limit=1,market='VN')
    for i, t in enumerate(results['tracks']['items']):
        print('Title: ', t['name'])
        print('URI: ', t['uri'])      
    res = sp.devices()        
    print(str(res))
if __name__ == '__main__':
    main(data)             
