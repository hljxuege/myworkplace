#encoding:utf-8
'''
Created on Sep 11, 2013

@author: liuxue
'''
from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from web import http
import tornado.httpserver
import tornado.web
import urllib
@gen.engine
def _process(url='', p=''):
    request = HTTPRequest('http://192.168.0.36:21010/base/invoice/getCategory', method='POST', body=urllib.urlencode(dict(a=1)))
    http = AsyncHTTPClient()    
    yield gen.Task(http.fetch, request)
        
class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
#     @gen.engine
    def get(self):
        p = dict(a=1, b=2)
        response = _process()
#         request = HTTPRequest('http://192.168.0.36:21010/base/invoice/getCategory', method='POST', body=urllib.urlencode(dict(a=1)))
#         http = AsyncHTTPClient()    
#         response = yield gen.Task(http.fetch, request)
        print response
        if response:
            self.write(response.body)
        self.write('-')
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