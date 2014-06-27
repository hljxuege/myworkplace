#encoding:utf-8
'''
Created on May 13, 2014

@author: liuxue
'''
import smtplib
from email.mime.text import MIMEText
host = '202.85.210.134'
port = 25
user = 'mbanking@infohold.com.cn'
pwd = 'smt_email0416'
sender = user
mailto = '570863597@qq.com'

#邮件信息
content = '''
        您好,%s<br><br>
        您的验证码为：%s<br><br>
        温馨提示：该验证码有效期为%s，如逾期请重新获取验证码。<br><br>
        这是一封系统生成的邮件，请勿回复。'''
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = 'No Reply'
msg['to'] = mailto
msg['From'] = sender

#连接发送服务器
smtp = smtplib.SMTP(host)
smtp.login(user, pwd)

#发送
smtp.sendmail(sender,mailto,msg.as_string())
smtp.quit()
