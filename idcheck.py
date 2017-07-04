#!/usr/bin/env python

import string

alphas = string.letters+'_'
nums = string.digits

print 'Welcome to the identifier check v1.0'
print 'Testees must be at least 2chars long.'
myinput = raw_input('Identifier to test?  ')

if len(myinput)>1:
   
   if myinput[0] not in alphas:
      print '''invalid : first symbol must be 
         alphabetic'''
   else:
      for otherchar in myinput[1:]:
         
         if otherchar not in alphas + nums:
            print '''invalid: remaining symbols must
                be alphanumeric'''
            break
         else:
            print '''okay with an identifier'''
