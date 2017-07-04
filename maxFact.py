#!/usr/bin/env python
# coding=utf-8
def showMaxFactor(num):
   count = num/2
   while count >1:
      if num % count == 0:
         print'largest factor of %d is %d' %(num,count)
         break
      count -=1
   else:    #与上面的while对其，否则出错
      print num," is prime"

for eachNum in range(10,21):
   showMaxFactor(eachNum)
