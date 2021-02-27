#import news
import feedparser
from speaking import speak
import random
import gih
import re
from termcolor import colored
import main_process
import untangle
import requests
import xml.dom.minidom as minidom
import datetime
#Read config
re_speaker= gih.get_config('re_speaker')
request_gold_rate_area=gih.get_request('request_gold_rate_area')
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH TỶ GIÁ: '+data)
    read_gold_rate()
def read_gold_rate():
    url = 'https://www.sjc.com.vn/xml/tygiavang.xml'
    response = requests.get(url) 
    xml_response = response.content
    file_name = '/tmp/gold_rate' + str(datetime.datetime.now().time()).replace(':', '.') + '.xml'                    
    xml_file= open(file_name, 'wb')
    xml_file.write(xml_response)
    xml_file.close()
    xmldoc = minidom.parse(file_name)
    itemlist = xmldoc.getElementsByTagName('item')
    speak('Giá vàng miếng JSC tại Hồ Chí Minh, mua vào là: '+ itemlist[0].attributes['buy'].value+' đồng, bán ra là: '+ itemlist[0].attributes['sell'].value+', đồng')
    speak('Giá vàng miếng JSC tại Hà Nội, mua vào là: '+ itemlist[8].attributes['buy'].value+' đồng, bán ra là: '+ itemlist[8].attributes['sell'].value+', đồng')    
    speak('Giá vàng miếng JSC tại Đà Nẵng, mua vào là: '+ itemlist[9].attributes['buy'].value+' đồng, bán ra là: '+ itemlist[9].attributes['sell'].value+', đồng')    
if __name__ == '__main__':
    main(data)
