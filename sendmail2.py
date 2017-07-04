#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1581955938@qq.com'
receiver = '13601648153@163.com'
subject = 'haha'
smtpserver = 'smtp.qq.com'
username = '1581955938@qq.com'
password = 'abc1581955938'

msg = MIMEText('哈哈','plain','utf-8')#中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')


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


