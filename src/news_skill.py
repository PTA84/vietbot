#import news
import feedparser
import re
import os
from termcolor import colored
import json

list_result=[]
def main(data1,data2):
    newsFeed = feedparser.parse(data2)   
    list_result.append('Tin mới từ '+ data1)
    i =1
    while i < 6: 
        entry = newsFeed.entries[i]
        # print (entry.published)
        clean = re.compile('<.*?>')
        clean_content= re.sub(clean, '', entry.summary)
        list_result.append(', '+clean_content+', ')        
        entry = None
        clean = None
        clean_content = None        
        i += 1
    return ' '.join(list_result)

        
# if __name__ == '__main__':
    # main(data)