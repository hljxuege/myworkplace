#encoding:utf-8
'''
Created on May 19, 2013

@author: liuxue
'''
import time
import tornado.web
import tornado.httpserver
settings = {'debug' : True, 'gzip':True} #增加autoreload配置
count = 0
countA = 0
def sendemail():
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
        这是一封系统生成的邮件，请勿回复。'''# % (username, unlocking_code, validTimeDelta)
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = 'No Reply'
    msg['to'] = mailto
    msg['From'] = sender
    
    #连接发送服务器
    smtp = smtplib.SMTP(host, 5)
    smtp.login(user, pwd)
    
    #发送
    smtp.sendmail(sender,mailto,msg.as_string())
    smtp.quit()


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello')

class TestAHandler(tornado.web.RequestHandler):
    countA = 0
    def get(self):
        tornado.ioloop.IOLoop.instance().run_sync(sendemail, 20)
        self.write('1')
                
application = tornado.web.Application([
    (r"/app", TestHandler),
    (r"/A", TestAHandler),
     ], **settings)

def startup(port=9891):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    startup()