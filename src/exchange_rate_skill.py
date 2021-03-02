#import news
import feedparser
from speaking import speak
import random
import gih
import re
from termcolor import colored
import untangle
import requests
import datetime
import xml.dom.minidom as minidom
#Read config
request_exchange_rate_type=gih.get_request('request_exchange_rate_type')
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH TỶ GIÁ: '+data)
    read_exchange_rate()
def read_exchange_rate():
    url = 'https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx?b=68'
    response = requests.get(url) 
    xml_response = response.content
    file_name = '/tmp/exchange_rate' + str(datetime.datetime.now().time()).replace(':', '.') + '.xml'                    
    xml_file= open(file_name, 'wb')
    xml_file.write(xml_response)
    xml_file.close()
    xmldoc = minidom.parse(file_name)
    itemlist = xmldoc.getElementsByTagName('Exrate')
    for x in range(len(request_exchange_rate_type)): 
        for s in itemlist:
            if s.attributes['CurrencyCode'].value ==request_exchange_rate_type[x]:
                # print('Tỷ giá đồng '+ s.attributes['CurrencyCode'].value+', mua vào là: '+ s.attributes['Buy'].value+' đồng, bán ra là: '+ s.attributes['Sell'].value+', đồng, giao dịch là: '+ s.attributes['Transfer'].value+' đồng')
                speak('Tỷ giá đồng '+ s.attributes['CurrencyCode'].value+', mua vào là: '+ s.attributes['Buy'].value+' đồng, bán ra là: '+ s.attributes['Sell'].value+', đồng, mua chuyển khoản là: '+ s.attributes['Transfer'].value+' đồng')

if __name__ == '__main__':
    main(data)