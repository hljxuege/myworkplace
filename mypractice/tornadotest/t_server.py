#encoding:utf-8
'''
Created on May 19, 2013

@author: liuxue
'''
import time
import tornado.web
import tornado.httpserver
settings = {'debug' : True} #增加autoreload配置
count = 0
class TestHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        s = time.time()
        time.sleep(0.3)
        self.write('Hello')
        global count 
        count = count +1
        print count, time.time() - s
        
application = tornado.web.Application([
    (r"/", TestHandler),
     ], **settings)

def startup(port=9090):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    startup()