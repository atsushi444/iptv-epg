#coding=utf-8
import time,datetime


TIME_ZONE=" +0800"
################  str="xx:xx"
'''
start="20180222044300 +0000" stop="20180222071500 +0000"
'''
##获取日期字符串20180222044300
def timeTostrOfsec(hs,d,flag=0):

    tmp=d+datetime.timedelta(days=flag)

    return timetofomat(tmp)+hs.replace(":","")+"00"

##获取结束时间
def stoptime(startime,duration,d):
    duration/=60
    list=startime.split(":")
    hour=int(list[0])
    min=int(list[1])

    min+=duration
    hour=hour+(min/60)

    flag=hour

    min%=60
    hour%=24

    hs="%02d:%02d"%(hour,min)

    return timeTostrOfsec(hs,d,flag=flag/24)
##获取开始时间
def startime(hs,d):
    return timeTostrOfsec(hs,d)

####获取星期几
def isToday():

    today=datetime.datetime.now()

    var=today.weekday()

    return var

def timetofomat(day):
    return day.strftime("%Y%m%d")


def getweeklist():
    days=[]
    monday=datetime.datetime.now()-datetime.timedelta(days=isToday())
    for var in range(0,7):

        nextday=monday+datetime.timedelta(days=var)
        days.append(nextday)

    return days

if __name__=="__main__":

    print stoptime("23:00",4800,datetime.datetime.now())
