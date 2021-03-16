from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import lun
from lun import S2L
from lun import L2S
import random
import os

    # if int(dayleft) < 7 :
    # elif int(dayleft) < 30:  
        # result = random.choice(gih.get_response('response_day_within_month'))+ ' ngày ' +a +' '+random.choice(gih.get_response('response_finish_sentense'))
    # else: 
        # result= random.choice(gih.get_response('response_day_over'))+ ' ngày ' +a +' '+random.choice(gih.get_response('response_finish_sentense'))
    
def main(name, day, month, day_type):

    now = datetime.datetime.today()
    dd = now.day
    mm = now.month
    yy = now.year
    result=''
    if day_type == 'calendar':    
        if day == 1 and month ==1:      
            xx = yy + 1
            ev = datetime.datetime(xx,1,1)
            d = ev - now    
            dayleft = d.days
            result= 'Còn '+str(dayleft)+' ngày nữa là đến ngày ' +name
            # print(result)            
            return result
        else:        
            ev = datetime.datetime(yy,month,day)
            d = ev - now
            dayleft = d.days
            result= 'Còn '+str(dayleft)+' ngày nữa là đến ngày ' +name
            # print(result)
            return result    
    elif day_type =='lunar_calendar':    
        lunar = S2L(dd,mm,yy)
        nam_am = int(lunar[2])
        thang_am  = int(lunar[1])
        nam_nhuan = int(lunar[3])   
        if day == 1 and month ==1:          
            nam_a = nam_am + 1
            a2d = L2S(28,12,yy,nam_nhuan) #Đổi sag nggayf dương 28/12
            nd = a2d[0]
            td = a2d[1]
            nmd = a2d[2]
            daa = str(nd)+'-'+str(td)+'-'+str(nmd) #Đổi sag ddihj dạng ngày
            a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
            a2d = a2dnew + timedelta(3)         
            nnm = a2d.day
            tnm = a2d.month
            nnm = a2d.year
            nammoi = S2L(nnm,tnm,nnm)
            nam_nhuan = int(str(nammoi[3]))
            ev = L2S(1,1,nam_a,nam_nhuan)
            n = str(ev[0])
            t = str(ev[1])
            nm = str(ev[2])
            daa = str(n)+'-'+str(t)+'-'+str(nm)
            a2d = datetime.datetime.strptime(daa, '%d-%m-%Y')
            d = a2d - now
            dayleft = d.days
            result= 'Còn '+str(dayleft)+' ngày nữa là đến ngày ' +name
            # print(result)
            return result
        else:
            ev = L2S(day,month,nam_am,nam_nhuan)
            daa = str(n)+'-'+str(t)+'-'+str(nm)
            a2d = datetime.datetime.strptime(daa, '%d-%m-%Y')
            d = a2d - now
            dayleft = d.days
            result= 'Còn '+str(dayleft)+' ngày nữa là đến ngày ' +name
            # print(result)
            return result   



# if __name__ == '__main__':
    # main(name,day, month, is_lunar_calendar)    