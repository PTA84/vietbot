import os
import feedparser

def main(location, url):
    d = feedparser.parse(url)
    # if 'CŨ HƠN' in data:
        # tg = d['entries'][1]['title'] 
        # kq = d['entries'][1]['description']
# #       print(kq)
    # else:
    tg = d['entries'][0]['title'] 
    kq = d['entries'][0]['description']
        # print(kq)
    kq = kq.replace(']',': ')
    kq = kq.replace('ĐB:','Giải đặc biệt:')
    kq = kq.replace('1:','Giải nhất:')
    kq = kq.replace('2:','Giải nhì:')
    kq = kq.replace('3:','Giải ba:')
    kq = kq.replace('4:','Giải tư:')
    kq = kq.replace('5:','Giải năm:')
    kq = kq.replace('6:','Giải sáu:')
    kq = kq.replace('7:','Giải bảy:')
    x = kq.split("[")
    ketqua = '. '.join(x)
    ketqua = ketqua.replace('\n','. ')
    return tg,kq
if __name__ == '__main__':
    main(data)        