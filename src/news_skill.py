#import news
import feedparser
import re
import os
from termcolor import colored
import json

with open('config.json') as config_json:
    config_data = json.load(config_json)
    
news_link=[]
news_name=[]
news_result=[]
for p in config_data['news_skill_data']:
    if p['is_active'] == True:        
        news_link.append(p['link'])
        news_name.append(p['name'].lower())

def main(data1,data2):

    newsFeed = feedparser.parse(news_link[data1])   
    i =1
    while i < 6: 
        entry = newsFeed.entries[i]
        print (entry.published)
        clean = re.compile('<.*?>')
        clean_content= re.sub(clean, '', entry.summary)
        news_result.append('Tin mới thứ '+ str(i)+ ' từ '+ news_name[data2] +" "+clean_content)        
        entry = None
        clean = None
        clean_content = None        
        i += 1
    return news_result
        
# if __name__ == '__main__':
    # main(data)