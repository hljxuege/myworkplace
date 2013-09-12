#encoding:utf-8
'''
Created on Sep 11, 2013

@author: liuxue
'''
from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
import tornado.httpserver
import tornado.web
import urllib
class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        http = AsyncHTTPClient()
        p = dict(a=1, b=2)
        request = HTTPRequest('http://192.168.0.36:21010/base/invoice/getCategory', method='POST', body=urllib.urlencode(dict(a=1)))
        
        response = yield gen.Task(http.fetch, request)
        print response
        if response.body:
            a = 1
        self.write('09')
        self.finish()
        
application = tornado.web.Application([
    (r"/", MainHandler),
], **{})

def startup(port=9090):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    startup()