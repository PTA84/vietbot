#import news
import feedparser
import random
import re
from termcolor import colored
import untangle
import requests
import datetime
import xml.dom.minidom as minidom

def main(data1,data2):
    url = 'https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx?b=68'
    response = requests.get(url) 
    xml_response = response.content
    file_name = '/tmp/exchange_rate' + str(datetime.datetime.now().time()).replace(':', '.') + '.xml'                    
    xml_file= open(file_name, 'wb')
    xml_file.write(xml_response)
    xml_file.close()
    xmldoc = minidom.parse(file_name)
    itemlist = xmldoc.getElementsByTagName('Exrate')
    for s in itemlist:
        if s.attributes['CurrencyCode'].value ==data2:
            # print('Tỷ giá đồng '+ s.attributes['CurrencyCode'].value+', mua vào là: '+ s.attributes['Buy'].value+' đồng, bán ra là: '+ s.attributes['Sell'].value+', đồng, giao dịch là: '+ s.attributes['Transfer'].value+' đồng')
            result ='Tỷ giá đồng '+ data1+', mua vào là: '+ s.attributes['Buy'].value+' đồng, bán ra là: '+ s.attributes['Sell'].value+', đồng, mua chuyển khoản là: '+ s.attributes['Transfer'].value+' đồng'
            return result
# if __name__ == '__main__':
    # main(data)