#import news
import feedparser
import random
import re
from termcolor import colored
import untangle
import requests
import xml.dom.minidom as minidom
import datetime
#Read config
# data1='hà nội'
# data2=2
def main(data1, data2):
    result=''
    url = 'https://www.sjc.com.vn/xml/tygiavang.xml'
    response = requests.get(url) 
    xml_response = response.content
    file_name = '/tmp/gold_rate' + str(datetime.datetime.now().time()).replace(':', '.') + '.xml'                    
    xml_file= open(file_name, 'wb')
    xml_file.write(xml_response)
    xml_file.close()
    xmldoc = minidom.parse(file_name)
    itemlist = xmldoc.getElementsByTagName('item')
    # print(str(itemlist))    
    result ='Giá vàng miếng JSC tại '+data1+' mua vào là: '+ itemlist[data2].attributes['buy'].value+' đồng, bán ra là: '+ itemlist[data2].attributes['sell'].value+' đồng'
    print(result)
    return result

# if __name__ == '__main__':
    # main(data1, data2)