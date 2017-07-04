#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#author:Victor Lv   

SENDMAIL = "/usr/sbin/sendmail" #sendmail(可执行程序)所在的路径  
      
sender = "1581955938@qq.com"   
receivers = ["13601648153@163.com"]  
subject = "哈哈"  
text = "哈哈。"  
      
#将这些元素组合成一条message  
message = """\ 
From: %s 
To: %s 
Subject: %s 
     
%s 
""" % (sender, ", ".join(receivers), subject, text)  
      
# Send the mail  
import os  
      
p = os.popen2("%s -t -i" % SENDMAIL, "w")  
p.write(message)  
status = p.close()  
if status:  
    print "Sendmail exit status", status  
