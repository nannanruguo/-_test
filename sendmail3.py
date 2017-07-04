#!/usr/bin/python
#-*- encoding: gb2312 -*-
import os, sys, string
import smtplib
import base64

# 邮件服务器地址
mailserver = "smtp.qq.com"
# 邮件用户名
username = "1581955938@qq.com"
# 密码
password = "abc1581955938"
# smtp会话过程中的mail from地址
from_addr = "1581955938@qq.com"
# smtp会话过程中的rcpt to地址
to_addr = "13601648153@163.com"
# 信件内容
msg = "hahahaha"

svr = smtplib.SMTP(mailserver)
# 设置为调试模式，就是在会话过程中会有输出信息
svr.set_debuglevel(1)
# ehlo命令，docmd方法包括了获取对方服务器返回信息，如果支持安全邮件，返回值里会有starttls提示
svr.docmd("EHLO server")
svr.starttls()  # <------ 这行就是新加的支持安全邮件的代码！
# auth login 命令
svr.docmd("AUTH LOGIN")
# 发送用户名，是base64编码过的，用send发送的，所以要用getreply获取返回信息
svr.send(base64.encodestring(username))
svr.getreply()
# 发送密码
svr.send(base64.encodestring(password))
svr.getreply()
# mail from, 发送邮件发送者
svr.docmd("MAIL FROM: <%s>" % from_addr)
# rcpt to, 邮件接收者
svr.docmd("RCPT TO: <%s>" % to_addr)
# data命令，开始发送数据
svr.docmd("DATA")
# 发送正文数据
svr.send(msg)
# 比如以 . 作为正文发送结束的标记
svr.send(" . ")
svr.getreply()
# 发送结束，退出
svr.quit()

