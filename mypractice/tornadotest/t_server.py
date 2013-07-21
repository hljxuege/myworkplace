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
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        s = time.time()
        time.sleep(0.5)
        self.write('Hello')
        global count 
        count = count +1
        print 'count', count, time.time() - s

class TestAHandler(tornado.web.RequestHandler):
    countA = 0
    def get(self):
         
        s = time.time()
        time.sleep(0.5)
        self.write('Hello')
        self.countA = self.countA +1
        print 'countA', self.countA, time.time() - s
                
application = tornado.web.Application([
    (r"/", TestHandler),
    (r"/A", TestAHandler),
     ], **settings)

def startup(port=9090):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    startup()