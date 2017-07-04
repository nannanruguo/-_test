#!/usr/bin/env python

pr="""
Enter the number:
"""
num=int(raw_input(pr))
count = num/2
while count >0:
   if num % count ==0:
      print count, 'is the largest factor of',num
      break
   count -=1


