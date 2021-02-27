#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import spot

from speaking import speak
import random
import gih
import requests, json, os, time, uuid, urllib, datetime   
from termcolor import colored
from bs4 import BeautifulSoup
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH HỎI BẰNG GOOGLE: '+data)
    if data is None:
        pass
    else:
        data = data.replace(" ","+")        
        url = 'https://www.google.com/search?q='
        _response = requests.get(url+data) 
        html_doc = _response.text.encode('utf-8')
        soup = BeautifulSoup(html_doc, 'html.parser')
        result = soup.find_all("div",class_="BNeawe")
        answer=result[1].text    
        print(answer)
        speak(answer)
if __name__ == '__main__':
    main()