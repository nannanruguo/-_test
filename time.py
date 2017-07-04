#!/bin/python

def changetime(time):
   print "From:   " ,time 
   year=time.split()[0].split('-')[0]
   month= time.split()[0].split('-')[1]
   day = time.split()[0].split('-')[2]
   hour=time.split()[1].split(':')[0]
   minute=time.split()[1].split(':')[1]
   second=time.split()[1].split(':')[2]
   hourint=int(hour)
   dayint=int(day)
   minuteint=int(minute)
   hour2=hourint+1
   day2=dayint+1
   
   
   if minuteint>=5:
      if hourint==23:
         day=str(day2)
         hour='00'
      else:
         hour=str(hour2)
   minute='05'
   second='00'

   print 'To:      %s-%s-%s %s:%s:%s' %(year,month,day,hour,minute,second)
   
      
time_list = ['2017-06-28 23:03:09', '2017-06-28 20:25:30', '2017-06-28 23:19:19']
for time in time_list:
   changetime(time)





