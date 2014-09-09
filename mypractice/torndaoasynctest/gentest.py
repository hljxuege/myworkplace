#encoding:utf-8
'''
Created on May 19, 2014

@author: liuxue
'''
from tornado import gen, stack_context
from tornado.httpclient import AsyncHTTPClient
import tornado.httpserver
import tornado.web
from tornadomail.backends.smtp import EmailBackend
from tornadomail.message import EmailMessage


class EmailCaptcha():
    to_email = ''
    def get_email_captcha(self, to_email, username, captcha, time_out):
        '''
        @param to_email: 收件人
        @param time_out: 有效时间秒， int类型
        '''
        self.to_email = to_email
        to_list = [to_email]
        content = 'hao'
        message = EmailMessage(
                    'email_subject',
                    content,
                    'mbanking@infohold.com.cn',
                    to_list,
                    connection=EmailBackend(
                                            '202.85.210.130', 25, 'mbanking@infohold.com.cn', 'smt_email0416',
                                            True
                                            )
                )
        message.content_subtype = "html"
        return message
    
    def send_email(self, message):
        def _finish(num):
            if num >0:
                print 'send email captcha success:%s'% self.to_email
        def error_handler(e, msg, traceback):
            print 'send email captcha fail:%s'% self.to_email, e
            return True
        
        with stack_context.ExceptionStackContext(error_handler):
            message.send(callback=_finish)
    

class TT(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        
        email_captcha = EmailCaptcha()
        message = email_captcha.get_email_captcha('570863597@qq.com', 'hljxuege', 'smt_email0416', 200)
        email_captcha.send_email(message)
        self.finish('over')
        
    def _on_finish(self, *args):
        import time; time.sleep(3)
        print 'process'

def a_call_back(ss):
    return ss

@gen.coroutine
def get_request():
    http_client = AsyncHTTPClient()
    r = gen.Task(http_client.fetch, "http://www.baidu.com/")
    
    import time; time.sleep(3)
    raise gen.Return(r)

def callback(r):
    print r.request
    return r.request

class TT1(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        p = yield get_request()
        self.finish('over')

        
application = tornado.web.Application([
    (r"/t", TT),
    (r"/t1", TT1),
])
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

